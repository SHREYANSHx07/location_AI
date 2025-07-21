#!/bin/bash

# Lead Finder Automation - Deployment Script
# This script helps you deploy to Streamlit Cloud

echo "🚀 Lead Finder Automation - Deployment Script"
echo "=============================================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing git repository..."
    git init
fi

# Check if files are staged
if [ -z "$(git status --porcelain)" ]; then
    echo "✅ All files are committed"
else
    echo "📝 Staging files..."
    git add .
    
    echo "💬 Enter commit message (or press Enter for default):"
    read commit_message
    
    if [ -z "$commit_message" ]; then
        commit_message="Deploy Lead Finder Automation to Streamlit Cloud"
    fi
    
    git commit -m "$commit_message"
fi

# Check if remote is set
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "🔗 Setting up GitHub remote..."
    echo "Please enter your GitHub repository URL:"
    echo "Format: https://github.com/YOUR_USERNAME/lead-finder-automation.git"
    read repo_url
    
    if [ -n "$repo_url" ]; then
        git remote add origin "$repo_url"
    else
        echo "❌ No repository URL provided. Please set up manually:"
        echo "git remote add origin YOUR_REPO_URL"
        exit 1
    fi
fi

# Push to GitHub
echo "📤 Pushing to GitHub..."
git push -u origin main

echo ""
echo "✅ Repository pushed to GitHub!"
echo ""
echo "🎯 Next Steps:"
echo "1. Go to https://share.streamlit.io/"
echo "2. Sign in with your GitHub account"
echo "3. Click 'New app'"
echo "4. Select your repository: lead-finder-automation"
echo "5. Set main file path: streamlit_app.py"
echo "6. Click 'Deploy!'"
echo ""
echo "🔑 Don't forget to set environment variables in Streamlit Cloud:"
echo "   - SERPAPI_KEY: Your SerpAPI key"
echo ""
echo "🌐 Your app will be available at:"
echo "   https://YOUR_APP_NAME-YOUR_USERNAME.streamlit.app" 