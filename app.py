from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from openai import OpenAI

import os
import openai

# Initialize the Flask app
app = Flask(__name__)

# Load configuration
app.config.from_object('config.Config')



# Optional: OpenAI setup
client = None
if not app.config.get('TESTING', False):
    client = OpenAI(api_key=app.config.get('DALLE_API_KEY', 'optional-default-key'))

# Define routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_started')
def get_started():
    return redirect(url_for('thumbnail_generator'))
    

@app.route('/thumbnail_generator', methods=['GET', 'POST'])
def thumbnail_generator():
    if request.method == 'POST':
        data = request.get_json()
        prompt = data.get('prompt')
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400
        try:
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                n=1
            )
            image_url = response.data[0].url
            return jsonify({'image_url': image_url})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return render_template('thumbnail_generator.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    # Run the app
    app.run(debug=True, port=5004)
