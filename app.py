"""
Question-and-Answering Web GUI Application
Author: Michael Ebube
Description: Flask web application for Q&A system with LLM API integration
"""

import os
import string
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure the LLM client
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')


class QuestionProcessor:
    """Handles preprocessing of user questions."""
    
    @staticmethod
    def preprocess(question: str) -> str:
        """
        Apply basic preprocessing to the question:
        - Lowercasing
        - Tokenization
        - Punctuation removal (except ?)
        """
        # Lowercase
        processed = question.lower()
        
        # Remove extra whitespace
        processed = ' '.join(processed.split())
        
        # Remove punctuation except question marks
        processed = ''.join(
            char for char in processed 
            if char not in string.punctuation or char == '?'
        )
        
        # Tokenization (split into words)
        tokens = processed.split()
        
        # Reconstruct the question
        processed = ' '.join(tokens)
        
        return processed


def get_llm_answer(question: str, api_key: str) -> dict:
    """
    Send question to LLM API and get the answer.
    
    Args:
        question: The question to ask
        api_key: API key for Gemini
        
    Returns:
        Dictionary with status and result
    """
    try:
        if not api_key:
            return {
                'success': False,
                'error': 'API key not configured. Please set GEMINI_API_KEY environment variable.'
            }
        
        # Configure Gemini
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Construct prompt
        prompt = f"""You are a helpful AI assistant that provides clear, accurate, and concise answers to questions.

Question: {question}

Answer:"""
        
        # Make API call
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                max_output_tokens=1024,
            )
        )
        
        # Extract answer
        answer = response.text.strip()
        
        return {
            'success': True,
            'answer': answer
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': f'Error communicating with LLM API: {str(e)}'
        }


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask_question():
    """Handle question submission."""
    try:
        data = request.get_json()
        
        if not data or 'question' not in data:
            return jsonify({
                'success': False,
                'error': 'No question provided'
            }), 400
        
        question = data['question'].strip()
        
        if not question:
            return jsonify({
                'success': False,
                'error': 'Question cannot be empty'
            }), 400
        
        # Get API key from request or environment
        api_key = data.get('api_key', GEMINI_API_KEY)
        
        # Preprocess the question
        processor = QuestionProcessor()
        processed_question = processor.preprocess(question)
        
        # Get answer from LLM
        result = get_llm_answer(question, api_key)
        
        if result['success']:
            return jsonify({
                'success': True,
                'original_question': question,
                'processed_question': processed_question,
                'answer': result['answer']
            })
        else:
            return jsonify({
                'success': False,
                'error': result['error']
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    # Check if API key is set
    if not GEMINI_API_KEY:
        print("WARNING: GEMINI_API_KEY environment variable not set.")
        print("Users will need to provide their API key through the web interface.")
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
