# Question-and-Answering System with LLM API

A complete Q&A system built with Python that connects to Google's Gemini API, featuring both a CLI application and a modern web interface.

**Author:** Michael Ebube  
**Course:** CSC415 - AI Practicals  
**Date:** November 2025

---

## 📋 Project Overview

This project implements a Question-and-Answering system with the following components:

1. **Python CLI Application** (`LLM_QA_CLI.py`) - Command-line interface for asking questions
2. **Web GUI Application** (`app.py`) - Flask-based web interface
3. **Deployment-ready** - Can be hosted on Render, PythonAnywhere, or other platforms

---

## 🚀 Features

### CLI Application

- ✅ Natural language question processing
- ✅ Text preprocessing (lowercasing, tokenization, punctuation removal)
- ✅ Integration with Google Gemini API (free tier available)
- ✅ Interactive command-line interface
- ✅ Error handling and user-friendly messages

### Web Application

- ✅ Modern, responsive UI with dark theme
- ✅ Real-time question processing
- ✅ Display of original and preprocessed questions
- ✅ LLM-generated answers
- ✅ API key management (localStorage)
- ✅ Loading states and error handling

---

## 📁 Project Structure

```
LLM_QA_Project_MichaelEbube_MATRICNO/
├── LLM_QA_CLI.py                    # CLI application
├── app.py                            # Flask web application
├── requirements.txt                  # Python dependencies
├── LLM_QA_hosted_webGUI_link.txt    # Deployment info
├── README.md                         # This file
├── DEPLOYMENT.md                     # Deployment guide
├── .env.example                      # Environment variables template
├── static/
│   └── style.css                     # CSS styling
└── templates/
    └── index.html                    # HTML template
```

---

## 🔧 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Google Gemini API key (free at [Google AI Studio](https://makersuite.google.com/app/apikey))

### Step 1: Clone or Download the Project

```bash
git clone https://github.com/yourusername/LLM_QA_Project_MichaelEbube_MATRICNO.git
cd LLM_QA_Project_MichaelEbube_MATRICNO
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set Up API Key

#### Option A: Environment Variable (Recommended)

```bash
# Windows PowerShell
$env:GEMINI_API_KEY = "your_api_key_here"

# Windows Command Prompt
set GEMINI_API_KEY=your_api_key_here

# Linux/Mac
export GEMINI_API_KEY="your_api_key_here"
```

#### Option B: Create .env File

```bash
# Create a .env file in the project root
GEMINI_API_KEY=your_api_key_here
```

---

## 💻 Usage

### Running the CLI Application

```bash
python LLM_QA_CLI.py
```

**Commands:**

- Type your question and press Enter
- Type `help` for available commands
- Type `quit` or `exit` to close

**Example:**

```
Your Question: What is the capital of France?

[Processing...]
Preprocessed: what is the capital of france?

[Querying LLM API...]

======================================================================
ANSWER:
======================================================================
The capital of France is Paris. It is the country's largest city and
serves as the center of government, culture, and commerce.
======================================================================
```

### Running the Web Application

```bash
python app.py
```

Then open your browser to: `http://localhost:5000`

**Features:**

- Enter your Groq API key (or use environment variable)
- Type your question in the text area
- Click "Get Answer" or press Enter
- View original question, preprocessed version, and AI answer

---

## 🌐 Deployment

### Deploy to Render.com (Recommended)

1. **Create account** at [render.com](https://render.com)
2. **Connect GitHub** repository
3. **Create new Web Service**
4. **Configure:**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Add Environment Variable: `GEMINI_API_KEY`
5. **Deploy** and get your live URL

### Deploy to PythonAnywhere

1. **Create account** at [pythonanywhere.com](https://www.pythonanywhere.com)
2. **Upload files** via Files tab
3. **Install dependencies** in Bash console:
   ```bash
   pip install --user -r requirements.txt
   ```
4. **Create Web App** (Flask)
5. **Configure WSGI** file to point to `app.py`
6. **Add API key** in environment variables
7. **Reload** web app

### Deploy to Streamlit Cloud (Alternative)

If you prefer Streamlit, create `streamlit_app.py`:

```bash
streamlit run streamlit_app.py
```

Then deploy via [streamlit.io/cloud](https://streamlit.io/cloud)

See `DEPLOYMENT.md` for detailed deployment instructions.

---

## 🔑 Getting Your Free Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Select or create a Google Cloud project
5. Copy and save your API key securely

**Note:** Google Gemini offers generous free tier limits perfect for this project!

---

## 🧪 Testing

### Test CLI Application

```bash
python LLM_QA_CLI.py
```

### Test Web Application Locally

```bash
python app.py
# Open http://localhost:5000 in your browser
```

### Test Preprocessing

```python
from LLM_QA_CLI import QuestionProcessor

processor = QuestionProcessor()
result = processor.preprocess("What's the weather like?")
print(result)  # Output: "whats the weather like?"
```

---

## 📝 Technical Details

### Preprocessing Steps

1. **Lowercasing** - Convert all text to lowercase
2. **Whitespace Normalization** - Remove extra spaces
3. **Punctuation Removal** - Remove all punctuation except `?`
4. **Tokenization** - Split into words
5. **Reconstruction** - Join tokens back into string

### LLM Configuration

- **Provider:** Google Gemini
- **Model:** gemini-pro
- **Temperature:** 0.7
- **Max Output Tokens:** 1024

### Tech Stack

- **Backend:** Flask (Python 3.8+)
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **API:** Google Gemini API
- **Deployment:** Gunicorn (WSGI server)

---

## 🐛 Troubleshooting

### "API key not found" Error

- Ensure `GEMINI_API_KEY` environment variable is set
- Or enter API key in web interface
- Check `.env` file if using python-dotenv

### "Module not found" Error

```bash
pip install -r requirements.txt
```

### Port Already in Use

```bash
# Change port in app.py
app.run(debug=True, host='0.0.0.0', port=8000)
```

### Import Errors

```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

---

## 📚 Project Requirements Checklist

### Part A - CLI Application ✅

- [x] Accept natural-language questions
- [x] Apply preprocessing (lowercasing, tokenization, punctuation removal)
- [x] Construct prompt and send to LLM API
- [x] Display final answer

### Part B - Web GUI ✅

- [x] Enter questions via web interface
- [x] View processed question
- [x] See LLM API response
- [x] Display generated answer
- [x] Flask + HTML/CSS implementation

### Part C - Deployment ✅

- [x] Deployment-ready configuration
- [x] `LLM_QA_hosted_webGUI_link.txt` file
- [x] Name, matric number, live URL, GitHub link

### Part D - GitHub Submission ✅

- [x] Correct folder structure
- [x] All required files
- [x] Documentation

---

## 📄 License

This project is created for educational purposes as part of CSC415 coursework.

---

## 👤 Contact

**Michael Ebube**  
Matric No: [YOUR_MATRIC_NUMBER]  
Course: CSC415 - AI Practicals  
Institution: [YOUR_UNIVERSITY]

---

## 🙏 Acknowledgments

- Google for providing free Gemini API access
- Flask framework and community
- CSC415 course instructors

---

**Happy Coding! 🚀**
