#!/usr/bin/env python3
"""
Lead Finder Automation - Main Runner Script

This script provides a convenient way to run the Lead Finder Automation app
from the root directory of the project.
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    """Main function to run the Lead Finder Automation app"""
    
    # Get the current directory
    current_dir = Path(__file__).parent
    app_dir = current_dir / "app"
    
    # Check if app directory exists
    if not app_dir.exists():
        print("❌ Error: App directory not found!")
        print("Please ensure you're running this from the project root directory.")
        sys.exit(1)
    
    # Check if app.py exists
    app_file = app_dir / "app.py"
    if not app_file.exists():
        print("❌ Error: app.py not found in the app directory!")
        sys.exit(1)
    
    # Change to app directory
    os.chdir(app_dir)
    
    print("🚀 Starting Lead Finder Automation...")
    print("📱 The app will open in your browser at http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the application")
    print("-" * 50)
    
    try:
        # Run streamlit app
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", "8501",
            "--server.address", "localhost"
        ])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error running the application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 