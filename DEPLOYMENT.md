# Deployment Guide for LLM Q&A System

This guide provides step-by-step instructions for deploying your Q&A system to various hosting platforms.

---

## 🌐 Deployment Options

1. **Render.com** (Recommended - Free tier available)
2. **PythonAnywhere** (Easy for beginners)
3. **Streamlit Cloud** (If using Streamlit)
4. **Vercel** (For advanced users)

---

## 1️⃣ Deploy to Render.com (Recommended)

### Why Render?

- Free tier available
- Automatic deployments from GitHub
- Easy environment variable management
- Good performance

### Prerequisites

- GitHub account
- Render account (free at [render.com](https://render.com))
- Your code pushed to GitHub

### Step-by-Step Instructions

#### A. Prepare Your Repository

1. **Push your code to GitHub:**

   ```bash
   git init
   git add .
   git commit -m "Initial commit: LLM Q&A System"
   git branch -M main
   git remote add origin https://github.com/yourusername/LLM_QA_Project.git
   git push -u origin main
   ```

2. **Verify these files exist:**
   - `app.py`
   - `requirements.txt`
   - `templates/index.html`
   - `static/style.css`

#### B. Create Render Web Service

1. **Sign in to Render:**

   - Go to [dashboard.render.com](https://dashboard.render.com)
   - Sign up or log in

2. **Create New Web Service:**

   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select your LLM_QA_Project repository

3. **Configure Build Settings:**

   ```
   Name: llm-qa-system (or your preferred name)
   Environment: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app
   ```

4. **Add Environment Variables:**

   - Click "Environment" tab
   - Add variable:
     - Key: `GEMINI_API_KEY`
     - Value: `your_actual_gemini_api_key`

5. **Deploy:**
   - Click "Create Web Service"
   - Wait for deployment (2-5 minutes)
   - Your app will be live at: `https://llm-qa-system.onrender.com`

#### C. Verify Deployment

1. Open your Render URL
2. Enter a test question
3. Verify the answer appears correctly

---

## 2️⃣ Deploy to PythonAnywhere

### Why PythonAnywhere?

- Beginner-friendly
- Free tier available
- No credit card required
- Good for educational projects

### Step-by-Step Instructions

#### A. Create PythonAnywhere Account

1. Go to [pythonanywhere.com](https://www.pythonanywhere.com)
2. Sign up for free account
3. Verify your email

#### B. Upload Your Files

1. **Go to Files Tab:**

   - Click "Files" in dashboard
   - Create new directory: `LLM_QA_System`

2. **Upload Files:**
   - Upload `app.py`
   - Upload `requirements.txt`
   - Create `templates` folder and upload `index.html`
   - Create `static` folder and upload `style.css`

#### C. Install Dependencies

1. **Open Bash Console:**

   - Click "Consoles" → "Bash"

2. **Navigate to your project:**

   ```bash
   cd LLM_QA_System
   ```

3. **Install dependencies:**
   ```bash
   pip3.10 install --user -r requirements.txt
   ```

#### D. Configure Web App

1. **Go to Web Tab:**

   - Click "Web" in dashboard
   - Click "Add a new web app"

2. **Select Flask:**

   - Choose "Flask"
   - Select Python 3.10

3. **Configure WSGI File:**

   - Click on WSGI configuration file link
   - Replace content with:

   ```python
   import sys
   import os

   # Add your project directory
   project_home = '/home/yourusername/LLM_QA_System'
   if project_home not in sys.path:
       sys.path.insert(0, project_home)

   # Set environment variable
   os.environ['GROQ_API_KEY'] = 'your_actual_groq_api_key'

   # Import Flask app
   from app import app as application
   ```

4. **Set Static Files:**

   - URL: `/static/`
   - Directory: `/home/yourusername/LLM_QA_System/static`

5. **Reload Web App:**
   - Click green "Reload" button

#### E. Access Your App

Your app will be available at:
`https://yourusername.pythonanywhere.com`

---

## 3️⃣ Deploy to Streamlit Cloud

### Create Streamlit Version (Optional)

If you prefer Streamlit, create `streamlit_app.py`:

```python
import streamlit as st
import os
from groq import Groq
import string

st.set_page_config(
    page_title="Q&A System",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Question & Answer System")
st.markdown("Ask me anything using AI-powered assistance")

# API Key input
api_key = st.text_input(
    "Enter your Groq API Key:",
    type="password",
    help="Get your free API key at console.groq.com"
)

# Question input
question = st.text_area(
    "Your Question:",
    placeholder="Type your question here...",
    height=100
)

if st.button("Get Answer", type="primary"):
    if not api_key:
        st.error("Please enter your Groq API key")
    elif not question:
        st.error("Please enter a question")
    else:
        with st.spinner("Processing..."):
            # Preprocess
            processed = question.lower()
            processed = ''.join(
                char for char in processed
                if char not in string.punctuation or char == '?'
            )

            # Get answer
            try:
                client = Groq(api_key=api_key)
                response = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful AI assistant."
                        },
                        {
                            "role": "user",
                            "content": question
                        }
                    ],
                    model="llama-3.1-70b-versatile",
                )

                answer = response.choices[0].message.content

                # Display results
                st.success("Answer received!")

                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("📝 Original Question")
                    st.write(question)

                with col2:
                    st.subheader("🔧 Preprocessed")
                    st.code(processed)

                st.subheader("💡 Answer")
                st.info(answer)

            except Exception as e:
                st.error(f"Error: {str(e)}")
```

### Deploy to Streamlit Cloud

1. **Push to GitHub** (including `streamlit_app.py`)

2. **Go to Streamlit Cloud:**

   - Visit [streamlit.io/cloud](https://streamlit.io/cloud)
   - Sign in with GitHub

3. **Deploy:**

   - Click "New app"
   - Select your repository
   - Main file: `streamlit_app.py`
   - Click "Deploy"

4. **Add Secrets:**
   - Go to app settings
   - Add secret:
     ```toml
     GROQ_API_KEY = "your_api_key"
     ```

Your app will be live at:
`https://yourusername-llm-qa-system.streamlit.app`

---

## 4️⃣ Deploy to Vercel (Advanced)

### Prerequisites

- Vercel account
- Vercel CLI installed

### Steps

1. **Install Vercel CLI:**

   ```bash
   npm install -g vercel
   ```

2. **Create `vercel.json`:**

   ```json
   {
     "builds": [
       {
         "src": "app.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "app.py"
       }
     ]
   }
   ```

3. **Deploy:**

   ```bash
   vercel
   ```

4. **Add Environment Variables:**
   ```bash
   vercel env add GROQ_API_KEY
   ```

---

## 🔒 Security Best Practices

1. **Never commit API keys to GitHub:**

   ```bash
   # Add to .gitignore
   .env
   *.key
   secrets.txt
   ```

2. **Use environment variables** for sensitive data

3. **Rotate API keys** regularly

4. **Monitor usage** to prevent abuse

---

## 🧪 Testing Your Deployment

### Checklist

- [ ] App loads without errors
- [ ] Can enter questions
- [ ] Preprocessed question displays correctly
- [ ] LLM returns answers
- [ ] Error handling works (try without API key)
- [ ] Mobile responsive (check on phone)
- [ ] HTTPS enabled (secure connection)

### Test Questions

1. "What is Python?"
2. "Explain machine learning in simple terms"
3. "What is the capital of Nigeria?"

---

## 📊 Monitoring & Maintenance

### Render.com

- View logs in dashboard
- Monitor usage under "Metrics"
- Set up auto-deploy on git push

### PythonAnywhere

- Check error logs in "Error log" tab
- Monitor CPU usage
- Upgrade plan if needed

### Streamlit Cloud

- View logs in app dashboard
- Monitor uptime
- Check resource usage

---

## 🐛 Common Deployment Issues

### Issue: "Application Error"

**Solution:**

- Check logs for specific error
- Verify all dependencies in `requirements.txt`
- Ensure `GROQ_API_KEY` is set

### Issue: "Module not found"

**Solution:**

```bash
# Make sure requirements.txt includes all dependencies
flask==3.0.0
groq==0.4.2
gunicorn==21.2.0
```

### Issue: "Port already in use"

**Solution:**

- Remove `port=5000` from `app.py` for production
- Let hosting platform assign port

### Issue: "Static files not loading"

**Solution:**

- Verify folder structure: `/static/style.css`
- Check Flask static_folder configuration
- Clear browser cache

---

## 📝 Update LLM_QA_hosted_webGUI_link.txt

After successful deployment, update the file:

```
Name: Michael Ebube
Matric Number: YOUR_ACTUAL_MATRIC_NUMBER

Live URL: https://your-actual-deployed-url.com

GitHub Repository: https://github.com/yourusername/LLM_QA_Project_MichaelEbube_MATRICNO

Deployment Platform: Render.com
Deployment Date: November 21, 2025
```

---

## 🎉 Next Steps

1. ✅ Test your deployed application
2. ✅ Update `LLM_QA_hosted_webGUI_link.txt`
3. ✅ Push final changes to GitHub
4. ✅ Submit your project

---

**Congratulations on deploying your Q&A system! 🚀**
