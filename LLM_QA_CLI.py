"""
Question-and-Answering CLI Application
Author: Michael Ebube
Description: CLI application that accepts natural-language questions,
             processes them, and sends them to an LLM API for answers.
"""

import os
import re
import string
from typing import Optional
import sys

# Install required packages if not available
try:
    import google.generativeai as genai
except ImportError:
    print("Installing required packages...")
    os.system("pip install google-generativeai")
    import google.generativeai as genai


class QuestionProcessor:
    """Handles preprocessing of user questions."""
    
    @staticmethod
    def preprocess(question: str) -> str:
        """
        Apply basic preprocessing to the question:
        - Lowercasing
        - Tokenization
        - Punctuation removal (except ?)
        
        Args:
            question: Raw question string
            
        Returns:
            Preprocessed question string
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


class LLMClient:
    """Handles interaction with the LLM API."""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the LLM client.
        
        Args:
            api_key: API key for the LLM service (Gemini)
        """
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        
        if not self.api_key:
            raise ValueError(
                "API key not found. Please set GEMINI_API_KEY environment variable "
                "or pass api_key parameter."
            )
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')  # Latest Gemini model
    
    def get_answer(self, question: str) -> str:
        """
        Send question to LLM API and get the answer.
        
        Args:
            question: The question to ask
            
        Returns:
            The LLM's answer
        """
        try:
            # Construct the prompt
            prompt = f"""You are a helpful AI assistant that provides clear, accurate, and concise answers to questions.

Question: {question}

Answer:"""
            
            # Make API call using Gemini
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                    max_output_tokens=1024,
                )
            )
            
            # Extract and return the answer
            answer = response.text
            return answer.strip()
            
        except Exception as e:
            return f"Error communicating with LLM API: {str(e)}"


class LLMQACLI:
    """Main CLI application class."""
    
    def __init__(self):
        """Initialize the CLI application."""
        self.processor = QuestionProcessor()
        self.llm_client = None
    
    def setup_api(self):
        """Set up the LLM API connection."""
        print("=" * 70)
        print("Question-and-Answering CLI Application")
        print("=" * 70)
        print("\nSetting up LLM API connection...")
        
        # Check for API key in environment
        api_key = os.getenv('GEMINI_API_KEY')
        
        if not api_key:
            print("\nNo GEMINI_API_KEY found in environment variables.")
            print("Please enter your Gemini API key (or press Enter to exit):")
            api_key = input("API Key: ").strip()
            
            if not api_key:
                print("No API key provided. Exiting...")
                sys.exit(0)
        
        try:
            self.llm_client = LLMClient(api_key=api_key)
            print("✓ API connection established successfully!\n")
        except Exception as e:
            print(f"✗ Error setting up API: {e}")
            sys.exit(1)
    
    def display_help(self):
        """Display help information."""
        print("\nCommands:")
        print("  - Type your question and press Enter")
        print("  - Type 'help' to see this message")
        print("  - Type 'quit' or 'exit' to close the application")
        print()
    
    def run(self):
        """Run the CLI application."""
        self.setup_api()
        self.display_help()
        
        while True:
            try:
                # Get user input
                print("-" * 70)
                question = input("\nYour Question: ").strip()
                
                # Handle special commands
                if not question:
                    continue
                
                if question.lower() in ['quit', 'exit', 'q']:
                    print("\nThank you for using the Q&A system. Goodbye!")
                    break
                
                if question.lower() == 'help':
                    self.display_help()
                    continue
                
                # Process the question
                print("\n[Processing...]")
                processed_question = self.processor.preprocess(question)
                print(f"Preprocessed: {processed_question}")
                
                # Get answer from LLM
                print("\n[Querying LLM API...]")
                answer = self.llm_client.get_answer(question)
                
                # Display the answer
                print("\n" + "=" * 70)
                print("ANSWER:")
                print("=" * 70)
                print(answer)
                print("=" * 70)
                
            except KeyboardInterrupt:
                print("\n\nInterrupted by user. Exiting...")
                break
            except Exception as e:
                print(f"\n✗ Error: {e}")
                print("Please try again.")


def main():
    """Main entry point for the CLI application."""
    app = LLMQACLI()
    app.run()


if __name__ == "__main__":
    main()
