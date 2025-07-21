#!/usr/bin/env python3
"""
Quick Demo for Lead Finder Automation

This script provides a quick way to test the Lead Finder application
with existing demo data and helps set up Google Sheets integration.
"""

import os
import sys
import pandas as pd
from pathlib import Path
import webbrowser

def show_demo_data():
    """Show the existing demo data"""
    
    print("📊 Demo Data Overview")
    print("="*50)
    
    # Check if demo CSV exists
    csv_file = Path("demo_leads.csv")
    if csv_file.exists():
        df = pd.read_csv(csv_file)
        
        print(f"✅ Found demo data: {csv_file}")
        print(f"📊 Total leads: {len(df)}")
        print(f"📋 Columns: {', '.join(df.columns)}")
        
        print("\n📋 Sample Leads:")
        print("-" * 50)
        
        for i, row in df.head(5).iterrows():
            print(f"{i+1}. {row['business_name']}")
            print(f"   Website: {row['website']}")
            print(f"   Niche: {row['niche']}")
            print(f"   Location: {row['location']}")
            print(f"   Phone: {row['phone']}")
            print()
        
        return df
    else:
        print("❌ Demo CSV file not found")
        return None

def create_google_sheet_guide():
    """Create a simple guide for Google Sheets setup"""
    
    print("\n🔧 Quick Google Sheets Setup")
    print("="*50)
    
    print("\n📋 Quick Steps:")
    print("1. Go to https://console.cloud.google.com/")
    print("2. Create a new project")
    print("3. Enable Google Sheets API")
    print("4. Create a service account")
    print("5. Download JSON credentials")
    print("6. Save as 'google_credentials.json' in this folder")
    print("7. Run: export GOOGLE_SHEETS_CREDENTIALS_PATH='./google_credentials.json'")
    
    print("\n🎯 Alternative: Use the demo CSV file")
    print("The demo CSV file can be imported into Google Sheets manually:")
    print("1. Open Google Sheets")
    print("2. File → Import → Upload → Select 'demo_leads.csv'")
    print("3. Import as new sheet")
    
    # Offer to open Google Sheets
    open_sheets = input("\n🌐 Would you like to open Google Sheets? (y/n): ")
    if open_sheets.lower() in ['y', 'yes']:
        webbrowser.open("https://sheets.google.com")

def test_lead_finder():
    """Test the lead finder functionality"""
    
    print("\n🧪 Testing Lead Finder Components")
    print("="*50)
    
    # Test imports
    try:
        app_dir = Path(__file__).parent / "app"
        sys.path.insert(0, str(app_dir))
        
        from lead_search import LeadFinder
        from sheets_writer import GoogleSheetsWriter
        from config import Config
        
        print("✅ All modules imported successfully")
        
        # Test configuration
        config_status = Config.get_api_keys_status()
        print("\n📊 Configuration Status:")
        for key, status in config_status.items():
            status_icon = "✅" if status else "❌"
            print(f"   {status_icon} {key}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing components: {str(e)}")
        return False

def show_usage_examples():
    """Show usage examples"""
    
    print("\n💡 Usage Examples")
    print("="*50)
    
    print("\n🎯 Example 1: Search for Interior Designers in Mumbai")
    print("   Niche: Interior Designers")
    print("   Location: Mumbai")
    print("   Expected Results: Interior design studios, decorators, etc.")
    
    print("\n🎯 Example 2: Search for Digital Marketing Agencies in Delhi")
    print("   Niche: Digital Marketing Agencies")
    print("   Location: Delhi")
    print("   Expected Results: SEO agencies, social media marketers, etc.")
    
    print("\n🎯 Example 3: Search for Web Developers in Bangalore")
    print("   Niche: Web Developers")
    print("   Location: Bangalore")
    print("   Expected Results: Web development companies, freelancers, etc.")
    
    print("\n💡 Tips:")
    print("   • Be specific with your niche")
    print("   • Use city names for better results")
    print("   • Try different variations of business types")
    print("   • Check the results and refine your search")

def main():
    """Main demo function"""
    
    print("🚀 Lead Finder Automation - Quick Demo")
    print("="*60)
    
    # Show demo data
    demo_df = show_demo_data()
    
    # Test components
    components_ok = test_lead_finder()
    
    # Show usage examples
    show_usage_examples()
    
    # Google Sheets setup
    create_google_sheet_guide()
    
    print("\n" + "="*60)
    print("🎉 Demo Overview Complete!")
    print("\n💡 Next Steps:")
    print("1. Get SerpAPI key from https://serpapi.com/")
    print("2. Set up Google Sheets (optional)")
    print("3. Run the app: python run.py")
    print("4. Start searching for leads!")
    
    print("\n📁 Files Available:")
    print("   • demo_leads.csv - Sample data")
    print("   • app/ - Main application")
    print("   • README.md - Complete documentation")
    
    print("\n🔗 Quick Links:")
    print("   • SerpAPI: https://serpapi.com/")
    print("   • Google Cloud Console: https://console.cloud.google.com/")
    print("   • Google Sheets: https://sheets.google.com")

if __name__ == "__main__":
    main() 