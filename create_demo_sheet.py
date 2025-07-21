#!/usr/bin/env python3
"""
Demo Google Sheet Creator for Lead Finder Automation

This script automatically creates a Google Sheet for testing and demo purposes.
It includes sample lead data and proper formatting to showcase the application.
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime, timedelta
import random

# Add app directory to path
app_dir = Path(__file__).parent / "app"
sys.path.insert(0, str(app_dir))

from sheets_writer import GoogleSheetsWriter

def create_sample_leads():
    """Create sample lead data for demo purposes"""
    
    sample_businesses = [
        {
            "name": "Digital Dynamics Agency",
            "website": "https://digitaldynamics.com",
            "phone": "+91-98765-43210",
            "address": "Bandra West, Mumbai, Maharashtra",
            "niche": "Digital Marketing Agencies",
            "location": "Mumbai"
        },
        {
            "name": "Interior Elegance Studio",
            "website": "https://interiorelegance.in",
            "phone": "+91-87654-32109",
            "address": "Andheri West, Mumbai, Maharashtra",
            "niche": "Interior Designers",
            "location": "Mumbai"
        },
        {
            "name": "Tech Solutions Pro",
            "website": "https://techsolutionspro.com",
            "phone": "+91-76543-21098",
            "address": "Powai, Mumbai, Maharashtra",
            "niche": "IT Services",
            "location": "Mumbai"
        },
        {
            "name": "Creative Brand Studio",
            "website": "https://creativebrandstudio.com",
            "phone": "+91-65432-10987",
            "address": "Worli, Mumbai, Maharashtra",
            "niche": "Branding Agencies",
            "location": "Mumbai"
        },
        {
            "name": "Web Development Hub",
            "website": "https://webdevhub.in",
            "phone": "+91-54321-09876",
            "address": "Khar West, Mumbai, Maharashtra",
            "niche": "Web Development",
            "location": "Mumbai"
        },
        {
            "name": "SEO Masters India",
            "website": "https://seomastersindia.com",
            "phone": "+91-43210-98765",
            "address": "Juhu, Mumbai, Maharashtra",
            "niche": "SEO Services",
            "location": "Mumbai"
        },
        {
            "name": "Social Media Experts",
            "website": "https://socialmediaexperts.in",
            "phone": "+91-32109-87654",
            "address": "Santacruz West, Mumbai, Maharashtra",
            "niche": "Social Media Marketing",
            "location": "Mumbai"
        },
        {
            "name": "Content Creation Pro",
            "website": "https://contentcreationpro.com",
            "phone": "+91-21098-76543",
            "address": "Vile Parle West, Mumbai, Maharashtra",
            "niche": "Content Marketing",
            "location": "Mumbai"
        },
        {
            "name": "E-commerce Solutions",
            "website": "https://ecommercesolutions.in",
            "phone": "+91-10987-65432",
            "address": "Goregaon West, Mumbai, Maharashtra",
            "niche": "E-commerce Development",
            "location": "Mumbai"
        },
        {
            "name": "Mobile App Studio",
            "website": "https://mobileappstudio.com",
            "phone": "+91-09876-54321",
            "address": "Malad West, Mumbai, Maharashtra",
            "niche": "Mobile App Development",
            "location": "Mumbai"
        }
    ]
    
    leads = []
    base_date = datetime.now() - timedelta(days=7)
    
    for i, business in enumerate(sample_businesses):
        # Add some variation to search dates
        search_date = base_date + timedelta(hours=i*2)
        
        lead = {
            'business_name': business['name'],
            'website': business['website'],
            'address': business['address'],
            'phone': business['phone'],
            'contact_info': f"Phone: {business['phone']}, Address: {business['address']}",
            'niche': business['niche'],
            'location': business['location'],
            'description': f"Professional {business['niche'].lower()} services in {business['location']}. Specializing in modern solutions and innovative approaches.",
            'source_url': business['website'],
            'search_date': search_date.strftime('%Y-%m-%d %H:%M:%S')
        }
        leads.append(lead)
    
    return leads

def create_credentials_template():
    """Create a template credentials file for demo purposes"""
    
    credentials_template = {
        "type": "service_account",
        "project_id": "lead-finder-demo",
        "private_key_id": "demo_key_id",
        "private_key": "-----BEGIN PRIVATE KEY-----\nDEMO_PRIVATE_KEY\n-----END PRIVATE KEY-----\n",
        "client_email": "demo-service-account@lead-finder-demo.iam.gserviceaccount.com",
        "client_id": "123456789",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/demo-service-account%40lead-finder-demo.iam.gserviceaccount.com"
    }
    
    # Create credentials directory if it doesn't exist
    credentials_dir = Path("credentials")
    credentials_dir.mkdir(exist_ok=True)
    
    # Save template credentials
    credentials_file = credentials_dir / "demo_credentials.json"
    with open(credentials_file, "w") as f:
        json.dump(credentials_template, f, indent=2)
    
    return credentials_file

def create_demo_sheet():
    """Create a demo Google Sheet with sample data"""
    
    print("🔧 Creating Demo Google Sheet...")
    print("="*50)
    
    # Check if we have Google Sheets credentials
    credentials_path = os.getenv('GOOGLE_SHEETS_CREDENTIALS_PATH')
    
    if not credentials_path:
        print("⚠️  No Google Sheets credentials found")
        print("Creating template credentials file...")
        credentials_path = create_credentials_template()
        print(f"📝 Template credentials created: {credentials_path}")
        print("\n💡 To use real Google Sheets:")
        print("1. Go to https://console.cloud.google.com/")
        print("2. Create a project and enable Google Sheets API")
        print("3. Create a service account and download credentials")
        print("4. Set GOOGLE_SHEETS_CREDENTIALS_PATH environment variable")
        print("\nFor now, we'll create a demo CSV file instead.")
        
        # Create demo CSV instead
        create_demo_csv()
        return
    
    try:
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
            for i, lead in enumerate(sample_leads[:3], 1):
                print(f"   {i}. {lead['business_name']} - {lead['niche']}")
            print("   ... and more")
        else:
            print("❌ Failed to save leads to Google Sheets")
        
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
        
    except Exception as e:
        print(f"❌ Error creating Google Sheet: {str(e)}")
        print("\n💡 Creating demo CSV file instead...")
        create_demo_csv()

def create_demo_csv():
    """Create a demo CSV file with sample data"""
    
    import pandas as pd
    
    sample_leads = create_sample_leads()
    
    # Convert to DataFrame
    df = pd.DataFrame(sample_leads)
    
    # Save to CSV
    csv_file = "demo_leads.csv"
    df.to_csv(csv_file, index=False)
    
    print(f"✅ Created demo CSV file: {csv_file}")
    print(f"📊 Contains {len(sample_leads)} sample leads")
    print(f"📁 File location: {Path(csv_file).absolute()}")
    
    # Show sample data
    print("\n📋 Sample data preview:")
    print(df.head(3).to_string(index=False))

def main():
    """Main function to create demo sheet"""
    
    print("🚀 Lead Finder Automation - Demo Sheet Creator")
    print("="*60)
    
    # Create demo sheet
    create_demo_sheet()
    
    print("\n" + "="*60)
    print("🎉 Demo setup completed!")
    print("\n💡 Next steps:")
    print("1. Get your SerpAPI key from https://serpapi.com/")
    print("2. Set up Google Sheets API credentials")
    print("3. Run the application: python run.py")
    print("4. Test with the demo data")
    print("\n📖 For detailed instructions, see README.md")

if __name__ == "__main__":
    main() 