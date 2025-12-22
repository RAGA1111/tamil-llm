## Tamil LLM

This project is a Tamil Large Language Model setup built using the Tamil LLaMA model by Abhinand from Hugging Face.
The model is connected through LM Studio and integrated with a Python backend, with an HTML/CSS frontend for interaction.

## Overview

The project uses:

* Tamil LLaMA from Hugging Face (by Abhinand)
* LM Studio for local model inference
* Python (Flask or FastAPI) for backend API handling
* HTML for frontend interface

This allows users to interact with a locally running Tamil language model directly through a web browser.

## Architecture

Tamil LLaMA (Hugging Face by Abhinand)
↓
LM Studio (local inference)
↓
Python backend (app.py)
↓
HTML frontend (templates)

## Setup Instructions

1. Clone the repository
   git clone [https://github.com/RAGA1111/tamil-llm.git](https://github.com/RAGA1111/tamil-llm.git)
   cd tamil-llm

2. Install dependencies
   If using Flask:
   pip install flask

   Or, if using FastAPI:
   pip install fastapi uvicorn

3. Start LM Studio

   * Open LM Studio
   * Load the Tamil LLaMA model by Abhinand from Hugging Face
   * Start the local server (default: localhost:1234)

4. Run the backend
   For Flask:
   python app.py

   For FastAPI:
   uvicorn app:app --reload

5. Open the frontend
   In your browser, go to:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Folder Structure

tamil-llm/
│
├── app.py
├── templates/
    └── index.html
├── static/ (optional)
└── README.md

## Features

* Tamil language understanding and generation
* Runs entirely offline through LM Studio
* Simple and extendable Python backend
* Clean HTML frontend interface

## Model Credits

Model: Tamil LLaMA
Author: Abhinand
Source: Hugging Face
Used through LM Studio for local inference

## Future Plans

* Add streaming output for faster responses
* English to Tamil translation toggle
* Chat history storage
* Voice input and text-to-speech.

## Author

RAGA1111
GitHub: [https://github.com/RAGA1111](https://github.com/RAGA1111)
