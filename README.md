# Generative AI CLI App using Google (Gemini)

A small CLI app that lets users register/login and run three Gemini-powered tasks:
sentiment analysis, language translation, and language detection.

## Features

- Simple register/login flow (in-memory database)
- Sentiment analysis
- Language translation
- Language detection

## Requirements

- Python 3.11+
- A Gemini API key

## Setup

```
conda create -n geminiapp python=3.11 -y
conda activate geminiapp
pip install -r requirements.txt
```

## Configuration

Set your Gemini API key as an environment variable:

```
set GEMINI_API_KEY=YOUR_API_KEY
```

If `GEMINI_API_KEY` is not set, the app will fall back to the default value in
the code. For security, keep the key out of source control and use the env var.

## Run

```
python ai_main.py
```

Follow the on-screen prompts to register/login and choose a task.

## Project Structure

```
.
readme.md
requirements.txt
ai_main.py
```

## Notes

- User data is stored in memory and resets on each run.
- This is a CLI demo; no persistent storage is used.
