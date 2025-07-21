# 🚀 Streamlit Cloud Deployment Guide

## 📋 Prerequisites

1. **GitHub Account**: You need a GitHub account
2. **Streamlit Cloud Account**: Sign up at https://share.streamlit.io/
3. **SerpAPI Key**: Get your API key from https://serpapi.com/

## 🔧 Step-by-Step Deployment

### Step 1: Prepare Your Repository

1. **Create a GitHub repository**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Lead Finder Automation"
   ```

2. **Push to GitHub**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/lead-finder-automation.git
   git push -u origin main
   ```

### Step 2: Set Up Streamlit Cloud

1. **Go to** https://share.streamlit.io/
2. **Sign in** with your GitHub account
3. **Click** "New app"
4. **Select your repository**: `lead-finder-automation`
5. **Set the main file path**: `streamlit_app.py`
6. **Click** "Deploy!"

### Step 3: Configure Environment Variables

In Streamlit Cloud dashboard:

1. **Go to** your deployed app settings
2. **Add environment variables**:
   - `SERPAPI_KEY`: Your SerpAPI API key
   - `GOOGLE_SHEETS_CREDENTIALS_PATH`: Path to credentials (optional)

### Step 4: Test Your Deployment

1. **Visit your app URL** (provided by Streamlit Cloud)
2. **Test the functionality**:
   - Enter niche: "Digital Marketing Agencies"
   - Enter location: "Mumbai"
   - Click "Find Leads"

## 📁 Required Files for Deployment

Your repository should contain:

```
lead-finder-automation/
├── streamlit_app.py          # Main entry point
├── app/
│   ├── app.py               # Main application
│   ├── lead_search.py       # Lead search logic
│   ├── sheets_writer.py     # Google Sheets integration
│   ├── config.py            # Configuration
│   └── __init__.py          # Package init
├── requirements.txt          # Dependencies
├── .streamlit/
│   └── config.toml          # Streamlit config
├── README.md                # Documentation
└── .gitignore               # Git ignore rules
```

## 🔑 Environment Variables

Set these in Streamlit Cloud:

| Variable | Description | Required |
|----------|-------------|----------|
| `SERPAPI_KEY` | Your SerpAPI key | ✅ Yes |
| `GOOGLE_SHEETS_CREDENTIALS_PATH` | Path to Google credentials | ❌ No |

## 🚨 Important Notes

### Security
- **Never commit API keys** to your repository
- **Use environment variables** for sensitive data
- **The .gitignore file** protects sensitive files

### Limitations
- **File uploads** (Google Sheets credentials) work differently in cloud
- **Local file access** is restricted
- **Environment variables** are the preferred method

### Google Sheets Integration
For Google Sheets in cloud deployment:

1. **Upload credentials** through the Streamlit UI
2. **Or use environment variables** for the credentials path
3. **Share your Google Sheet** with the service account

## 🎯 Quick Deployment Commands

```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit changes
git commit -m "Deploy Lead Finder Automation"

# Add remote (replace with your GitHub repo URL)
git remote add origin https://github.com/YOUR_USERNAME/lead-finder-automation.git

# Push to GitHub
git push -u origin main
```

## 🔍 Troubleshooting

### "Module not found" errors
- Ensure all files are in the correct structure
- Check that `requirements.txt` includes all dependencies

### API key not working
- Verify the environment variable is set correctly in Streamlit Cloud
- Check that your SerpAPI key is valid and has credits

### App not loading
- Check the main file path in Streamlit Cloud settings
- Ensure `streamlit_app.py` exists and is correct

## 🎉 Success!

Once deployed, your app will be available at:
`https://YOUR_APP_NAME-YOUR_USERNAME.streamlit.app`

## 📞 Support

- **Streamlit Cloud Docs**: https://docs.streamlit.io/streamlit-community-cloud
- **SerpAPI Docs**: https://serpapi.com/docs
- **Google Sheets API**: https://developers.google.com/sheets/api 