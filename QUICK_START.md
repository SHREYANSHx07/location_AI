# 🚀 Quick Start Guide

## ✅ Your SerpAPI Key is Set!

I can see you've already set your SerpAPI key: `a1b74d41b1564537886ff610b084f23a73d0619c03ce31744e72e6190dacd009`

## 🔧 How to Run the Application

### Step 1: Activate Virtual Environment
```bash
source venv/bin/activate
```

### Step 2: Set Your API Key
```bash
export SERPAPI_KEY="a1b74d41b1564537886ff610b084f23a73d0619c03ce31744e72e6190dacd009"
```

### Step 3: Run the Application
```bash
python run.py
```

## 🎯 One-Line Command

Or run everything in one line:
```bash
source venv/bin/activate && export SERPAPI_KEY="a1b74d41b1564537886ff610b084f23a73d0619c03ce31744e72e6190dacd009" && python run.py
```

## 📱 Access the Application

Once running, the app will be available at:
- **Local URL**: http://localhost:8501
- **Network URL**: http://10.24.51.19:8501

## 🎯 How to Use the App

1. **Open your browser** and go to http://localhost:8501
2. **Enter your search details**:
   - Niche: e.g., "Interior Designers"
   - Location: e.g., "Mumbai"
3. **Click "Find Leads"** to search
4. **View results** in the data table
5. **Save to Google Sheets** (optional)
6. **Download as CSV** (optional)

## 🔍 Test Examples

Try these search combinations:
- **Niche**: "Digital Marketing Agencies", **Location**: "Mumbai"
- **Niche**: "Web Developers", **Location**: "Delhi"
- **Niche**: "SEO Services", **Location**: "Bangalore"

## 🛠️ Troubleshooting

### If you get "No module named streamlit"
Make sure you're in the virtual environment:
```bash
source venv/bin/activate
```

### If the app doesn't start
Check if the port is available:
```bash
lsof -ti:8501
```

### If you get API errors
Verify your SerpAPI key is correct and has credits.

## 📊 Demo Data Available

The app includes demo data in `demo_leads.csv` with 10 sample leads for testing.

## 🎉 You're Ready!

Your Lead Finder Automation app is now running with your SerpAPI key configured! 🚀 