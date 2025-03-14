import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import whisper
import time
import ffmpeg

# Function to create directories on the Desktop
def create_folders():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")  # Get Desktop path
    transcript_folder = os.path.join(desktop_path, "transcript")  # Folder for transcript and models

    # Create 'transcript' folder if it doesn't exist
    if not os.path.exists(transcript_folder):
        os.makedirs(transcript_folder)

    model_folder = os.path.join(transcript_folder, "model")  # Folder for storing models
    # Create 'model' folder inside 'transcript' folder if it doesn't exist
    if not os.path.exists(model_folder):
        os.makedirs(model_folder)

    return model_folder, transcript_folder

# Function to download the selected model (no need to save it manually)
def download_model(model_name, model_folder):
    model_path = os.path.join(model_folder, f"{model_name}.pt")  # Set a custom path to store the model if needed
    print(f"Downloading Whisper model: {model_name}...")
    model = whisper.load_model(model_name)  # This will download the model and load it
    return model  # Return the loaded model

# Function to convert mp4 to mp3
def convert_mp4_to_mp3(mp4_file, output_folder):
    mp3_file = os.path.join(output_folder, os.path.splitext(os.path.basename(mp4_file))[0] + ".mp3")
    try:
        ffmpeg.input(mp4_file).output(mp3_file).run()
        return mp3_file
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while converting the file: {e}")
        return None

# Function to convert Whisper segments to VTT format
def segments_to_vtt(segments):
    vtt_output = "WEBVTT\n\n"
    for segment in segments:
        start_time = segment['start']
        end_time = segment['end']
        text = segment['text']
        vtt_output += f"{format_timestamp(start_time)} --> {format_timestamp(end_time)}\n{text}\n\n"
    return vtt_output

# Function to format timestamp into VTT-compatible format (HH:MM:SS.mmm)
def format_timestamp(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}.{int((seconds - int(seconds)) * 1000):03}"

# Function to run the whisper command
def transcribe_audio():
    audio_file = audio_file_entry.get()
    model_choice = model_var.get()  # Get the selected model choice from the dropdown
    convert_to_mp3 = convert_mp3_var.get()  # Check if the checkbox is checked
    format_choice = format_var.get()  # Get the selected format (.vtt or .txt)

    if not audio_file:
        messagebox.showerror("Error", "Please select an audio file")
        return

    if not os.path.isfile(audio_file):
        messagebox.showerror("Error", "The selected file does not exist")
        return

    # Automatically create folders on the desktop
    model_folder, output_folder = create_folders()

    # Download and load the selected model from the chosen folder
    model = download_model(model_choice, model_folder)  # Download the selected model

    # If the file is an MP4 and the user wants to convert it
    if convert_to_mp3 and audio_file.lower().endswith(".mp4"):
        audio_file = convert_mp4_to_mp3(audio_file, output_folder)
        if not audio_file:
            return  # If conversion failed, stop the transcription

    # Set the base output directory (where the transcript will be saved)
    subfolder_name = os.path.splitext(os.path.basename(audio_file))[0]
    subfolder_path = os.path.join(output_folder, subfolder_name + f"_{int(time.time())}")

    # Ensure the subfolder exists
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)

    # Start timing the transcription process
    start_time = time.time()

    try:
        # Perform transcription using the Whisper model object
        result = model.transcribe(audio_file, verbose=True)

        # If the user selected VTT, convert segments to VTT format
        if format_choice == "VTT":
            vtt_content = segments_to_vtt(result['segments'])
            output_file = os.path.join(subfolder_path, os.path.basename(audio_file) + ".vtt")
            with open(output_file, 'w') as output:
                output.write(vtt_content)

        # If the user selected TXT, save the basic text transcription
        elif format_choice == "TXT":
            output_file = os.path.join(subfolder_path, os.path.basename(audio_file) + ".txt")
            with open(output_file, 'w') as output:
                output.write(result['text'])

        # Save the mp3 file (if converted)
        if convert_to_mp3 and audio_file.lower().endswith(".mp3"):
            mp3_output_file = os.path.join(subfolder_path, os.path.basename(audio_file))
            os.rename(audio_file, mp3_output_file)

        # Calculate elapsed time and convert it to minutes
        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_minutes = elapsed_time / 60

        # Show the success message with the time taken
        result_message = f"Transcription complete! Output saved to {subfolder_path}\nTime taken: {elapsed_minutes:.2f} minutes"
        response = messagebox.askyesno("Success", result_message + "\n\nDo you want to transcribe another file?")

        if response:
            reset_fields()  # Reset fields to allow the user to run the program again

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while transcribing: {e}")

# Function to open a file dialog and select an audio file
def browse_audio_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.flac *.mp3 *.wav *.mp4")])
    if file_path:
        audio_file_entry.delete(0, tk.END)
        audio_file_entry.insert(0, file_path)

# Function to reset the fields and allow the user to run the program again
def reset_fields():
    audio_file_entry.delete(0, tk.END)
    model_var.set("medium")
    convert_mp3_var.set(False)  # Reset the checkbox
    format_var.set("TXT")  # Reset format to TXT

# Create the main window
root = tk.Tk()
root.title("Whisper Transcription Tool")

# Create the UI elements
audio_file_label = tk.Label(root, text="Select Audio File:")
audio_file_label.grid(row=0, column=0, padx=10, pady=10)

audio_file_entry = tk.Entry(root, width=40)
audio_file_entry.grid(row=0, column=1, padx=10, pady=10)

browse_button = tk.Button(root, text="Browse", command=browse_audio_file)
browse_button.grid(row=0, column=2, padx=10, pady=10)

model_label = tk.Label(root, text="Select Model:")
model_label.grid(row=1, column=0, padx=10, pady=10)

# Model selection dropdown (small, medium, large)
model_var = tk.StringVar(value="medium")  # Default model is "medium"
model_menu = tk.OptionMenu(root, model_var, "small", "medium", "large")
model_menu.grid(row=1, column=1, padx=10, pady=10)

# Checkbox to ask if the user wants to convert mp4 to mp3
convert_mp3_var = tk.BooleanVar()
convert_mp3_checkbox = tk.Checkbutton(root, text="Convert to MP3 (if MP4 file selected)", variable=convert_mp3_var)
convert_mp3_checkbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Dropdown to select the transcription format: VTT or TXT
format_label = tk.Label(root, text="Select Output Format:")
format_label.grid(row=3, column=0, padx=10, pady=10)

format_var = tk.StringVar(value="TXT")  # Default format is TXT
format_menu = tk.OptionMenu(root, format_var, "TXT", "VTT")
format_menu.grid(row=3, column=1, padx=10, pady=10)

transcribe_button = tk.Button(root, text="Transcribe", command=transcribe_audio)
transcribe_button.grid(row=4, column=0, columnspan=3, pady=20)

# Run the Tkinter event loop
root.mainloop()
