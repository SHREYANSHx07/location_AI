#!/usr/bin/env python3
"""
Lead Finder Automation - Streamlit Cloud Deployment

This is the main entry point for Streamlit Cloud deployment.
"""

import sys
import os
from pathlib import Path

# Add the app directory to the path
app_dir = Path(__file__).parent / "app"
sys.path.insert(0, str(app_dir))

# Import and run the main app
from app import main

if __name__ == "__main__":
    main() 