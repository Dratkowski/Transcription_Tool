import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import whisper
import time

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

# Function to run the whisper command
def transcribe_audio():
    audio_file = audio_file_entry.get()
    model_choice = model_var.get()  # Get the selected model choice from the dropdown

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
        result = model.transcribe(audio_file)

        # Write the transcription to a text file (Whisper's default output format)
        output_file = os.path.join(subfolder_path, f"{os.path.splitext(os.path.basename(audio_file))[0]}.txt")
        with open(output_file, 'w') as output:
            output.write(result['text'])

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
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.flac *.mp3 *.wav")])
    if file_path:
        audio_file_entry.delete(0, tk.END)
        audio_file_entry.insert(0, file_path)

# Function to reset the fields and allow the user to run the program again
def reset_fields():
    audio_file_entry.delete(0, tk.END)
    model_var.set("medium")

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
model_label.grid(row=2, column=0, padx=10, pady=10) 

# Model selection dropdown (small, medium, large) 
model_var = tk.StringVar(value="medium")  # Default model is "medium" 
model_menu = tk.OptionMenu(root, model_var, "small", "medium", "large") 
model_menu.grid(row=2, column=1, padx=10, pady=10) 

transcribe_button = tk.Button(root, text="Transcribe", command=transcribe_audio) 
transcribe_button.grid(row=3, column=0, columnspan=3, pady=20) 

# Run the Tkinter event loop 
root.mainloop()
