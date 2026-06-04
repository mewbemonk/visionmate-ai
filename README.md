# VisionMate AI

An AI-powered visual assistant that can scan real-world objects, extract text, understand context, answer user questions, and retrieve additional information from the web using OCR, LLMs, memory, speech recognition, and AI agents.

## Features

### Object Scanning

* Captures information from physical objects using a webcam.
* Extracts text using EasyOCR.
* Collects multiple OCR readings for higher accuracy.

### OCR Correction Agent

* Combines multiple OCR outputs.
* Corrects noisy OCR results using an LLM.
* Preserves important information such as product names, brands, and numerical values.

### Context Memory

* Stores detected information.
* Allows users to ask follow-up questions without rescanning.

### Question Answering Agent

* Answers questions using detected object information.
* Provides concise and context-aware responses.

### Search Agent

* Automatically performs web search when information is not available in the detected context.
* Uses DuckDuckGo Search and an LLM to generate short answers.

### Voice Interaction

* Speech-to-text using Whisper.
* Text-to-speech using pyttsx3.
* Hands-free interaction through voice commands.

### Streamlit Dashboard

* Object scanning interface.
* Context viewer.
* Voice-based question answering.
* Conversation history.

## Tech Stack

### AI & LLM

* OpenRouter
* GPT-OSS-120B
* LangChain

### Computer Vision

* OpenCV
* EasyOCR

### Speech

* OpenAI Whisper
* pyttsx3

### Frontend

* Streamlit

### Search

* DuckDuckGo Search

## Architecture

Webcam
↓
EasyOCR
↓
OCR Correction Agent
↓
Context Memory
↓
Question Agent
↓
Search Agent (Fallback)
↓
Voice + UI Response

## Example Workflow

1. User scans a product using webcam.
2. OCR extracts text from the object.
3. OCR Correction Agent reconstructs the most accurate text.
4. Context is stored in memory.
5. User asks a question by voice.
6. Question Agent attempts to answer using detected context.
7. If information is unavailable, Search Agent retrieves information from the web.
8. Answer is displayed and spoken back to the user.

## Use Cases

* Product Information Assistant
* Medicine Identification
* Educational Learning Assistant
* Smart Shopping Assistant
* Packaging & Label Reader
* Accessibility Support
* Visual Knowledge Assistant

## Future Improvements

* Live webcam streaming inside Streamlit
* Multi-language support
* Product ingredient analysis
* Barcode and QR detection
* Object detection integration
* RAG-based long-term memory
* Mobile deployment

## Installation

```bash
git clone https://github.com/mewbemonk/visionmate-ai.git

cd visionmate-ai

pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app.py
```

## Author

Rishabh

VisionMate AI is an Agentic Visual Assistant that combines Computer Vision, Generative AI, Voice AI, and Web Search to help users understand and interact with real-world objects.
