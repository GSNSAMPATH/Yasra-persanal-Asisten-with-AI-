# Yasra – AI Voice Assistant

A Python voice assistant that listens to speech, answers using the Google Gemini API, and replies with text-to-speech.

## Features
- Speech recognition (SpeechRecognition + Google speech API)
- Gen AI answers via Google Gemini API (short answers, or longer when you say "please explain")
- Text-to-speech replies (pyttsx3)
- Simple built-in commands (greetings, name, etc.)

## Setup
1. `pip install google-generativeai pyttsx3 SpeechRecognition pyaudio googletrans gTTS`
2. Set your key: `set GOOGLE_API_KEY=your_key` (Windows) or `export GOOGLE_API_KEY=your_key`
3. Run: `python speech.py`

## Tech
Python, Google Gemini API, SpeechRecognition, pyttsx3
 
