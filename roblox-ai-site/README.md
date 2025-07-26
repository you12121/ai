# Roblox AI Script Generator

This project is a web-based AI script generator for Roblox Studio. It uses OpenAI's GPT-4 to generate Lua scripts based on user prompts.

## Features

- **AI-Powered Script Generation:**  Generates Roblox Lua scripts using natural language prompts.
- **Roblox Developer Hub Integration:**  Uses the Roblox Developer Hub to provide context for more accurate script generation.
- **Search History:**  Saves your recent prompts for easy access.

## How to Run the Project

### Prerequisites

- Python 3.6+
- pip

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone <repository_url>
cd roblox-ai-site
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r backend/requirements.txt
```

### 3. Set OpenAI API Key

You need to set your OpenAI API key as an environment variable. Replace `<your_api_key>` with your actual key.

**On macOS/Linux:**

```bash
export OPENAI_API_KEY="<your_api_key>"
```

**On Windows:**

```bash
set OPENAI_API_KEY="<your_api_key>"
```

### 4. Run the Application

Start the Flask server:

```bash
python backend/app.py
```

### 5. Access the Website

Open your web browser and go to the following address:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

You can now start generating Roblox scripts!
