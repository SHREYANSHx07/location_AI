#!/usr/bin/env python3
"""
Google Sheets Setup Guide for Lead Finder Automation

This script helps users set up Google Sheets API credentials and create
a real demo Google Sheet for testing the Lead Finder application.
"""

import os
import sys
import json
import webbrowser
from pathlib import Path
from datetime import datetime

def print_setup_instructions():
    """Print detailed Google Sheets setup instructions"""
    
    print("🔧 Google Sheets API Setup Guide")
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
    print("   • Move the file to your project directory")
    
    print("\n5️⃣  Set Environment Variable")
    print("   • Rename the downloaded file to 'google_credentials.json'")
    print("   • Set environment variable:")
    print("     export GOOGLE_SHEETS_CREDENTIALS_PATH='./google_credentials.json'")
    
    print("\n6️⃣  Create Demo Sheet")
    print("   • Run this script again after setup")
    print("   • It will create a real Google Sheet with demo data")
    
    print("\n" + "="*60)

def create_real_demo_sheet():
    """Create a real Google Sheet with demo data"""
    
    print("🚀 Creating Real Google Sheet...")
    print("="*50)
    
    # Check for credentials
    credentials_path = os.getenv('GOOGLE_SHEETS_CREDENTIALS_PATH')
    
    if not credentials_path:
        print("❌ No Google Sheets credentials found")
        print("Please follow the setup instructions above first.")
        return False
    
    # Check if credentials file exists
    if not Path(credentials_path).exists():
        print(f"❌ Credentials file not found: {credentials_path}")
        print("Please ensure the credentials file exists and path is correct.")
        return False
    
    try:
        # Import after checking credentials
        app_dir = Path(__file__).parent / "app"
        sys.path.insert(0, str(app_dir))
        
        from sheets_writer import GoogleSheetsWriter
        from create_demo_sheet import create_sample_leads
        
        # Initialize Google Sheets writer
        sheets_writer = GoogleSheetsWriter(credentials_path)
        
        # Create sample leads
        sample_leads = create_sample_leads()
        
        # Create a new spreadsheet
        spreadsheet_title = f"Lead Finder Demo - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        spreadsheet_id = sheets_writer.create_spreadsheet(spreadsheet_title)
        
        print(f"✅ Created Google Sheet: {spreadsheet_title}")
        print(f"📊 Spreadsheet ID: {spreadsheet_id}")
        print(f"🔗 URL: https://docs.google.com/spreadsheets/d/{spreadsheet_id}")
        
        # Save sample leads to the sheet
        success = sheets_writer.save_leads(sample_leads, spreadsheet_id, "Demo Leads")
        
        if success:
            print(f"✅ Added {len(sample_leads)} sample leads to the sheet")
            print("\n📋 Sample data includes:")
            for i, lead in enumerate(sample_leads[:5], 1):
                print(f"   {i}. {lead['business_name']} - {lead['niche']}")
            print("   ... and more")
            
            # Save spreadsheet ID to environment
            env_file = Path(".env")
            if env_file.exists():
                with open(env_file, "a") as f:
                    f.write(f"\nDEFAULT_SPREADSHEET_ID={spreadsheet_id}\n")
            else:
                with open(env_file, "w") as f:
                    f.write(f"DEFAULT_SPREADSHEET_ID={spreadsheet_id}\n")
            
            print(f"\n💾 Spreadsheet ID saved to .env file")
            print(f"🎯 You can now use this spreadsheet for testing the Lead Finder app")
            
            # Offer to open the sheet
            open_sheet = input("\n🌐 Would you like to open the Google Sheet in your browser? (y/n): ")
            if open_sheet.lower() in ['y', 'yes']:
                webbrowser.open(f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}")
            
            return True
        else:
            print("❌ Failed to save leads to Google Sheets")
            return False
        
    except Exception as e:
        print(f"❌ Error creating Google Sheet: {str(e)}")
        print("\n💡 Common issues:")
        print("   - Check if Google Sheets API is enabled")
        print("   - Verify service account has proper permissions")
        print("   - Ensure credentials file is valid JSON")
        return False

def check_setup_status():
    """Check the current setup status"""
    
    print("🔍 Checking Setup Status...")
    print("="*40)
    
    # Check environment variables
    serpapi_key = os.getenv('SERPAPI_KEY')
    credentials_path = os.getenv('GOOGLE_SHEETS_CREDENTIALS_PATH')
    
    print(f"🔑 SerpAPI Key: {'✅ Set' if serpapi_key else '❌ Not set'}")
    print(f"📄 Google Credentials: {'✅ Set' if credentials_path else '❌ Not set'}")
    
    if credentials_path:
        creds_file = Path(credentials_path)
        if creds_file.exists():
            print(f"📁 Credentials File: ✅ Found at {creds_file}")
        else:
            print(f"📁 Credentials File: ❌ Not found at {creds_file}")
    
    # Check for .env file
    env_file = Path(".env")
    if env_file.exists():
        print(f"⚙️  .env File: ✅ Found")
    else:
        print(f"⚙️  .env File: ❌ Not found")
    
    print("\n" + "="*40)

def main():
    """Main function"""
    
    print("🚀 Lead Finder Automation - Google Sheets Setup")
    print("="*60)
    
    # Check current status
    check_setup_status()
    
    # Ask user what they want to do
    print("\n🎯 What would you like to do?")
    print("1. Show setup instructions")
    print("2. Create demo Google Sheet (if credentials are ready)")
    print("3. Check setup status")
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        print_setup_instructions()
        
        # Ask if they want to proceed with sheet creation
        proceed = input("\n🤔 Have you completed the setup? Ready to create demo sheet? (y/n): ")
        if proceed.lower() in ['y', 'yes']:
            create_real_demo_sheet()
    
    elif choice == "2":
        create_real_demo_sheet()
    
    elif choice == "3":
        check_setup_status()
    
    elif choice == "4":
        print("👋 Goodbye!")
        return
    
    else:
        print("❌ Invalid choice. Please try again.")
        main()
    
    print("\n" + "="*60)
    print("🎉 Setup process completed!")
    print("\n💡 Next steps:")
    print("1. Get your SerpAPI key from https://serpapi.com/")
    print("2. Run the application: python run.py")
    print("3. Test with the demo data")
    print("\n📖 For detailed instructions, see README.md")

if __name__ == "__main__":
    main() 