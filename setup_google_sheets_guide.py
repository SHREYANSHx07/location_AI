#!/usr/bin/env python3
"""
Google Sheets Setup Guide for Lead Finder Automation

This script provides step-by-step instructions for setting up Google Sheets integration.
"""

import webbrowser
import json
from pathlib import Path

def print_setup_instructions():
    """Print detailed Google Sheets setup instructions"""
    
    print("🔧 Google Sheets Integration Setup")
    print("="*60)
    
    print("\n📋 Step-by-Step Instructions:")
    
    print("\n1️⃣  Create Google Cloud Project")
    print("   • Go to https://console.cloud.google.com/")
    print("   • Click 'Select a project' → 'New Project'")
    print("   • Name it 'Lead Finder Demo'")
    print("   • Click 'Create'")
    
    print("\n2️⃣  Enable Google Sheets API")
    print("   • In your project, go to 'APIs & Services' → 'Library'")
    print("   • Search for 'Google Sheets API'")
    print("   • Click on it and press 'Enable'")
    print("   • Also enable 'Google Drive API' (for creating sheets)")
    
    print("\n3️⃣  Create Service Account")
    print("   • Go to 'APIs & Services' → 'Credentials'")
    print("   • Click 'Create Credentials' → 'Service Account'")
    print("   • Name: 'lead-finder-service'")
    print("   • Description: 'Service account for Lead Finder Automation'")
    print("   • Click 'Create and Continue'")
    print("   • Skip role assignment, click 'Done'")
    
    print("\n4️⃣  Download Credentials")
    print("   • Click on your service account")
    print("   • Go to 'Keys' tab")
    print("   • Click 'Add Key' → 'Create new key'")
    print("   • Choose 'JSON' format")
    print("   • Click 'Create' (downloads automatically)")
    print("   • Rename the file to 'google_credentials.json'")
    print("   • Move it to your project directory")
    
    print("\n5️⃣  Create Google Sheet")
    print("   • Go to https://sheets.google.com/")
    print("   • Create a new spreadsheet")
    print("   • Copy the spreadsheet ID from the URL")
    print("   • URL format: https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit")
    
    print("\n6️⃣  Share the Sheet")
    print("   • Click 'Share' in your Google Sheet")
    print("   • Add your service account email (from JSON file)")
    print("   • Give it 'Editor' permissions")
    
    print("\n7️⃣  Configure the App")
    print("   • Upload 'google_credentials.json' in the app sidebar")
    print("   • Enter your spreadsheet ID")
    print("   • Start searching and saving leads!")
    
    print("\n" + "="*60)

def open_google_console():
    """Open Google Cloud Console"""
    print("\n🌐 Opening Google Cloud Console...")
    webbrowser.open("https://console.cloud.google.com/")

def open_google_sheets():
    """Open Google Sheets"""
    print("\n📊 Opening Google Sheets...")
    webbrowser.open("https://sheets.google.com/")

def create_sample_credentials():
    """Create a sample credentials file for reference"""
    
    sample_creds = {
        "type": "service_account",
        "project_id": "your-project-id",
        "private_key_id": "your-private-key-id",
        "private_key": "-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY_HERE\n-----END PRIVATE KEY-----\n",
        "client_email": "your-service-account@your-project.iam.gserviceaccount.com",
        "client_id": "your-client-id",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your-service-account%40your-project.iam.gserviceaccount.com"
    }
    
    # Create credentials directory
    creds_dir = Path("credentials")
    creds_dir.mkdir(exist_ok=True)
    
    # Save sample file
    sample_file = creds_dir / "sample_credentials.json"
    with open(sample_file, "w") as f:
        json.dump(sample_creds, f, indent=2)
    
    print(f"📝 Sample credentials file created: {sample_file}")
    print("💡 Use this as a reference for the format")

def main():
    """Main function"""
    
    print("🚀 Lead Finder Automation - Google Sheets Setup")
    print("="*60)
    
    print("\n🎯 What would you like to do?")
    print("1. Show setup instructions")
    print("2. Open Google Cloud Console")
    print("3. Open Google Sheets")
    print("4. Create sample credentials file")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    if choice == "1":
        print_setup_instructions()
        
        # Ask if they want to proceed
        proceed = input("\n🤔 Would you like to open the required websites? (y/n): ")
        if proceed.lower() in ['y', 'yes']:
            open_google_console()
            open_google_sheets()
    
    elif choice == "2":
        open_google_console()
    
    elif choice == "3":
        open_google_sheets()
    
    elif choice == "4":
        create_sample_credentials()
    
    elif choice == "5":
        print("👋 Goodbye!")
        return
    
    else:
        print("❌ Invalid choice. Please try again.")
        main()
    
    print("\n" + "="*60)
    print("🎉 Setup guide completed!")
    print("\n💡 Next steps:")
    print("1. Follow the setup instructions above")
    print("2. Get your credentials JSON file")
    print("3. Create a Google Sheet and get its ID")
    print("4. Upload credentials in the app sidebar")
    print("5. Start saving leads to Google Sheets!")

if __name__ == "__main__":
    main() 