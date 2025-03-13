# Whisper GUI
This tool is based on the OpenAI transcription tool (https://github.com/openai/whisper). This repo is an easy set up process for people who are not familiar with python and libraries. 
The GUI makes using Whisper easier and once the program is set up, it will be much more user-friendly than the original set up of Whisper.

STEP 1:
Make sure Python (https://www.python.org/) is installed on your computer. It is a good idea to ensure that Python is in you PATH. Generally, speacking the default installation will do this but you should double check. You may have to restart you computer to have it show up in your PATH

  Step 1A: Python in PATH
   In your search bar, type PATH. Open "Edit the System Environment Variables" in the control panel (likely will be the first thing in the search). Then open "Environment Variables" (lower right on the system properties-Advanced tab). You will see two sections "User Variables" and "System Variables." Find the variable labled PATH in both section and make sure that the Python File path is in there. If it is not, find where Python is installed on your computer (likely C:\Users\COMPUTER_NAME\AppData\Local\Programs\Python) and copy the file path into both PATH variables 

STEP 2: Creat a Virtual Environment
When creating a new program, it is a good idea to make a virtual enviornment to run the program. This environment is where all of the libraries and dependencies will be installed. It Keep things seperate from other programs so dependencies are not impacted by other tools. 
      Dependencies/Libraries: Simply put these are tools that other programers and coders have developed to run sertain things with         the code. These help you do a wide variety of things so you do not have to do all the coding yourself. 
      
  STEP 2A: Set up a virtual environment (venv)
  
  1) Create a new folder on your C: drive labled "Whipser" (or something like that)
  2) Right click within that new folder, and "OPEN IN TERMINAL" (You can also open PowerShell and type: cd "C:file\path\to\your\new\folder"). "cd" is the command to open a folder directory
       path.
       
         cd "C:file\path\to\your\new\folder"
     
  4) Now create the virtual environment by typing in terminal:

         python -m venv NAME_YOUR_VENV
     
      Example:
     
         python -m venv whisper_venv
          
  5) Once the venv is created in your directory, you need to activate the venv. This opens the venv and will store all of your dependencies within the venv. You will know you are in the venv when you see the name of your venv in green before your directory file path.
       Acttivate your venv:

         YOUR_VENV\Scripts\activate
     Example:

         whisper_venv\Scripts\activate
STEP 3) 
Now that your venv is active, you can install Whisper within this venv. NOTE: if you close the terminal you will need to reactivate the venv. Make sure that you have downloaded the file "requirements.txt" and place it in your directory
      Installing dependencies:

    pip install -r requirements.txt

  "pip" is the code you will use to install most python libraries and dependencies.
  
  1) Verify that all the dependencies installed correctly. This list should have all the same things as the requierments.txt

         pip list
  2) Next, verify that Whisper is working properly.

     Type:

         whisper

You will know it is working when you see:

usage: whisper [-h] [--model MODEL] [--model_dir MODEL_DIR] [--device DEVICE] [--output_dir OUTPUT_DIR] [--output_format {txt,vtt,srt,tsv,json,all}] [--verbose VERBOSE] [--task {transcribe,translate}] [--language {af,am,ar,as,az,ba,be,bg,bn,bo,br,bs,ca,cs,cy,da,de,el,en,es,et,eu,fa,fi,fo,fr,gl,gu,ha,haw,he,hi,hr,ht,hu,hy,id,is,it,ja,jw,ka,kk,km,kn,ko,la,lb,ln,lo,lt,lv,mg,mi,mk,ml,mn,mr,ms,mt,my,ne,nl,nn,no,oc,pa,pl,ps,pt,ro,ru,sa,sd,si,sk,sl,sn,so,sq,sr,su,sv,sw,ta,te,tg,th,tk,tl,tr,tt,uk,ur,uz,vi,yi,yo,yue,zh,Afrikaans,Albanian,Amharic,Arabic,Armenian,Assamese,Azerbaijani,Bashkir,Basque,Belarusian,Bengali,Bosnian,Breton,Bulgarian,Burmese,Cantonese,Castilian,Catalan,Chinese,Croatian,Czech,Danish,Dutch,English,Estonian,Faroese,Finnish,Flemish,French,Galician,Georgian,German,Greek,Gujarati,Haitian,Haitian Creole, Hausa,H awaiian, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Italian, Japanese, Javanese, Kannada, Kazakh, Khmer, Korean, Lao, Latin, Latvian, Letzeburgesch, Lingala, Lithuanian, Luxembourgish, Macedonian, Malagasy, Malay, Malayalam, Maltese, Mandarin, Maori, Marathi, Moldavian, Moldovan, Mongolian, Myanmar, Nepali, Norwegian, Nynorsk, Occitan, Panjabi, Pashto, Persian, Polish, Portuguese, Punjabi, Pushto, Romanian, Russian, Sanskrit, Serbian, Shona, Sindhi, Sinhala, Sinhalese, Slovak, Slovenian, Somali, Spanish, Sundanese, Swahili, Swedish, Tagalog, Tajik, Tamil, Tatar, Telugu, Thai, Tibetan, Turkish, Turkmen, Ukrainian, Urdu, Uzbek, Valencian, Vietnamese, Welsh, Yiddish, Yoruba}]
               [--temperature TEMPERATURE] [--best_of BEST_OF] [--beam_size BEAM_SIZE] [--patience PATIENCE]
               [--length_penalty LENGTH_PENALTY] [--suppress_tokens SUPPRESS_TOKENS] [--initial_prompt INITIAL_PROMPT]
               [--carry_initial_prompt CARRY_INITIAL_PROMPT] [--condition_on_previous_text CONDITION_ON_PREVIOUS_TEXT]
               [--fp16 FP16] [--temperature_increment_on_fallback TEMPERATURE_INCREMENT_ON_FALLBACK]
               [--compression_ratio_threshold COMPRESSION_RATIO_THRESHOLD] [--logprob_threshold LOGPROB_THRESHOLD]
               [--no_speech_threshold NO_SPEECH_THRESHOLD] [--word_timestamps WORD_TIMESTAMPS]
               [--prepend_punctuations PREPEND_PUNCTUATIONS] [--append_punctuations APPEND_PUNCTUATIONS]
               [--highlight_words HIGHLIGHT_WORDS] [--max_line_width MAX_LINE_WIDTH] [--max_line_count MAX_LINE_COUNT]
               [--max_words_per_line MAX_WORDS_PER_LINE] [--threads THREADS] [--clip_timestamps CLIP_TIMESTAMPS]
               [--hallucination_silence_threshold HALLUCINATION_SILENCE_THRESHOLD]
               audio [audio ...]
whisper: error: the following arguments are required: audio

This shows you all of the languages that whisper recognizes and the general terminal script you can run

If you see in RED:

    whisper : The term 'whisper' is not recognized as the name of a cmdlet, function, script file, or operable program.
    Check the spelling of the name, or if a path was included, verify that the path is correct and try again.

Something went wrong and you may need to start over or do some research on the Whisper Github repo.

RUNNING WHISPER:
1)You can run whisper directly from terminal/PowerShell

       whisper audio.flac audio.mp3 audio.wav --model medium

   Example:

       whisper audio.flac "C:\LOCATION\OF\YOUR\AUDIO.mp3" audio.wav --model medium

   Note: .mp4 files work the best but .mp4 can be used. Just check the box:
        
        Convert to MP# (if MP$ file selected)
  This will convert the MP4 to a MP3. The MP3 will be stored in the created file on the desktop.
  
Note: There are a few different models that you can use to transcribe the audio. These models are AI (Large Language Models-LLMs) models that Whisper uses in the transcription. 
   Feel free to change the model that best fits your computer.

       tiny (requires 1GB RAM)
       base (requires 1GB RAM)
       small (requires 2GB RAM)
       medium (requires 5GB RAM)
       large (requires 10GB RAM)
       turbo (requires 6GB RAM)
   The larger the model the more accurate the transcription will be. Generally, small and medium will work.

Select Output Format:
This feature is defaulted to a basic .txt. This will transcribe the audio in as one big paragraph. This is generally a faster transcription. 

If VTT is selected, the audio will be transcribed with timestamps. This feature is really good for conversation transcriptions. 

WHISPER GUI

For those who do not want to run everything through Terminal/PowerShell, There is a general user interface (GUI) that is run through a python script. Ensure that the python script "whisper.py" is downloaded and place in your directory. 

Running a python script in Terminal/Power Shell:
  Ensure that the whisper_venv is activated before running the script.
  
    Python whisper.py

Running a python script through a .bat (or desktop icon)
  Either download the .bat file and place it on your desktop. Remember to change the directory in the file.

  OR

  Open a Notepad and copy and paste

     @echo off

    :: Change directory to the Whisper folder
    cd C:TYPE\YOUR\WHISPER\DIRECTORY

    :: Check if the virtual environment exists
    IF NOT EXIST whisper_venv\Scripts\activate.bat (
        echo Virtual environment not found! Exiting...
        pause
        exit /b
    )

    :: Activate the virtual environment
    call whisper_venv\Scripts\activate.bat

    :: Run the Python script
    python whisper.py

    :: Pause to keep the window open
    pause

Save the file to your desktop as a NAME_THE_FILE.bat
This will open the Whisper GUI by just clicking on the icon.
