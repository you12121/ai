import os
import logging
from flask import Flask, request, jsonify, send_from_directory
import openai  # ← تعديل هنا

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, static_folder='../frontend')

# Configure OpenAI API
try:
    openai.api_key = os.environ["OPENAI_API_KEY"]  # ← تعديل هنا
except KeyError:
    logging.error("OPENAI_API_KEY environment variable not set.")
    openai.api_key = None

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/generate-script', methods=['POST'])
def generate_script():
    if not openai.api_key:
        return jsonify({'error': 'OpenAI API key not configured'}), 500

    data = request.json
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    try:
        logging.debug(f"Received prompt: {prompt}")

        search_url = f"https://developer.roblox.com/en-us/search#stq={prompt.replace(' ', '%20')}"

        enhanced_prompt = f"""
        Please generate a Roblox Lua script for the user's request.
        You can use the following URL to find relevant information on the Roblox Developer Hub: {search_url}

        User's Request:
        {prompt}
        """

        response = openai.ChatCompletion.create(  # ← تعديل هنا
            model="gpt-3.5-turbo",  # تأكد أن هذا متاح لحسابك
            messages=[
                {"role": "system", "content": "You are a helpful assistant specialized in writing Roblox Lua scripts. Use your knowledge and the provided Roblox Developer Hub search URL to generate accurate and high-quality scripts."},
                {"role": "user", "content": enhanced_prompt}
            ]
        )
        script = response.choices[0].message['content']  # ← تعديل بسيط هنا لأن `message` dict
        logging.debug(f"Generated script: {script}")
        return jsonify({'script': script})
    except Exception as e:
        logging.error(f"Error generating script: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
