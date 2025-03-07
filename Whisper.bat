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
