# ✅ Streamlit Cloud Deployment Checklist

## 🚀 Quick Deployment Steps

### 1. Prepare Your Code
- [ ] All files are in the correct structure
- [ ] `streamlit_app.py` exists (main entry point)
- [ ] `requirements.txt` includes all dependencies
- [ ] `.gitignore` protects sensitive files

### 2. GitHub Setup
- [ ] Create GitHub repository
- [ ] Run deployment script: `./deploy.sh`
- [ ] Or manually:
  ```bash
  git init
  git add .
  git commit -m "Deploy Lead Finder Automation"
  git remote add origin YOUR_REPO_URL
  git push -u origin main
  ```

### 3. Streamlit Cloud Setup
- [ ] Go to https://share.streamlit.io/
- [ ] Sign in with GitHub
- [ ] Click "New app"
- [ ] Select repository: `lead-finder-automation`
- [ ] Set main file: `streamlit_app.py`
- [ ] Click "Deploy!"

### 4. Environment Variables (Optional)
- [ ] In Streamlit Cloud dashboard, add (optional):
  - `SERPAPI_KEY`: Your SerpAPI key (default key is pre-configured)
  - `GOOGLE_SHEETS_CREDENTIALS_PATH`: (optional)

### 5. Test Deployment
- [ ] Visit your app URL
- [ ] Test search functionality
- [ ] Verify API key works
- [ ] Test CSV download

## 📁 Required Files

```
✅ streamlit_app.py          # Main entry point
✅ app/app.py               # Main application
✅ app/lead_search.py       # Lead search logic
✅ app/sheets_writer.py     # Google Sheets integration
✅ app/config.py            # Configuration
✅ app/__init__.py          # Package init
✅ requirements.txt          # Dependencies
✅ .streamlit/config.toml   # Streamlit config
✅ README.md                # Documentation
✅ .gitignore               # Git ignore rules
```

## 🔑 Environment Variables

| Variable | Value | Required |
|----------|-------|----------|
| `SERPAPI_KEY` | Your SerpAPI key | ✅ Yes |

## 🎯 Your App URL

Once deployed, your app will be at:
`https://YOUR_APP_NAME-YOUR_USERNAME.streamlit.app`

## 🚨 Common Issues

- **"Module not found"**: Check file structure and requirements.txt
- **"API key not working"**: Verify environment variable in Streamlit Cloud
- **"App not loading"**: Check main file path in Streamlit Cloud settings

## 🎉 Success!

Your Lead Finder Automation will be live and accessible to anyone with the URL! 