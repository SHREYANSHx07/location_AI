#!/usr/bin/env python3
"""
Setup script for Lead Finder Automation

This script helps users set up the Lead Finder Automation application
by installing dependencies and providing guidance for configuration.
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required!")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def create_env_template():
    """Create a template .env file"""
    env_template = """# Lead Finder Automation - Environment Variables
# Copy this file to .env and fill in your API keys

# Required API Keys
SERPAPI_KEY=your_serpapi_key_here
GOOGLE_SHEETS_CREDENTIALS_PATH=path/to/your/credentials.json
DEFAULT_SPREADSHEET_ID=your_spreadsheet_id_here

# Optional Settings
DEFAULT_SHEET_NAME=Leads
DEFAULT_NUM_RESULTS=20
SEARCH_DELAY=1.0
OPENAI_API_KEY=your_openai_key_here  # Optional for advanced data cleaning
"""
    
    env_file = Path(".env")
    if not env_file.exists():
        with open(env_file, "w") as f:
            f.write(env_template)
        print("📝 Created .env template file")
        print("⚠️  Please edit .env file with your API keys")
    else:
        print("📝 .env file already exists")

def check_directories():
    """Check if required directories exist"""
    app_dir = Path("app")
    if not app_dir.exists():
        print("❌ Error: App directory not found!")
        return False
    
    required_files = ["app.py", "lead_search.py", "sheets_writer.py", "config.py"]
    for file in required_files:
        if not (app_dir / file).exists():
            print(f"❌ Error: {file} not found in app directory!")
            return False
    
    print("✅ All required files found")
    return True

def print_setup_instructions():
    """Print setup instructions"""
    print("\n" + "="*60)
    print("🚀 Lead Finder Automation Setup Complete!")
    print("="*60)
    print("\n📋 Next Steps:")
    print("1. Get your SerpAPI key from https://serpapi.com/")
    print("2. Set up Google Sheets API credentials:")
    print("   - Go to https://console.cloud.google.com/")
    print("   - Create a project and enable Google Sheets API")
    print("   - Create a service account and download credentials")
    print("3. Edit the .env file with your API keys")
    print("4. Run the application:")
    print("   python run.py")
    print("   or")
    print("   cd app && streamlit run app.py")
    print("\n📖 For detailed instructions, see README.md")
    print("="*60)

def main():
    """Main setup function"""
    print("🔧 Lead Finder Automation Setup")
    print("="*40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check directories and files
    if not check_directories():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Create environment template
    create_env_template()
    
    # Print instructions
    print_setup_instructions()

if __name__ == "__main__":
    main() 