#!/usr/bin/env python3
"""
Lead Finder Automation - Demo Script

This script demonstrates the core functionality of the Lead Finder Automation
without requiring the full Streamlit UI. It shows how to:
1. Search for leads using SerpAPI
2. Extract structured data
3. Save to Google Sheets (if configured)
"""

import os
import sys
from pathlib import Path

# Add app directory to path
app_dir = Path(__file__).parent / "app"
sys.path.insert(0, str(app_dir))

from lead_search import LeadFinder
from config import Config

def demo_lead_search():
    """Demonstrate lead search functionality"""
    print("🔍 Lead Finder Automation - Demo")
    print("="*50)
    
    # Check if SerpAPI key is available
    serpapi_key = os.getenv('SERPAPI_KEY')
    if not serpapi_key:
        print("❌ SERPAPI_KEY not found in environment variables")
        print("Please set your SerpAPI key:")
        print("export SERPAPI_KEY='your_serpapi_key_here'")
        return
    
    # Initialize lead finder
    lead_finder = LeadFinder(serpapi_key)
    
    # Demo search parameters
    niche = "Digital Marketing Agencies"
    location = "Mumbai"
    num_results = 10
    
    print(f"🔎 Searching for: {niche} in {location}")
    print(f"📊 Number of results: {num_results}")
    print("-" * 50)
    
    try:
        # Search for leads
        leads = lead_finder.search_leads(niche, location, num_results)
        
        if leads:
            print(f"✅ Found {len(leads)} leads!")
            print("\n📋 Lead Details:")
            print("-" * 50)
            
            for i, lead in enumerate(leads, 1):
                print(f"\n{i}. {lead.get('business_name', 'N/A')}")
                print(f"   Website: {lead.get('website', 'N/A')}")
                print(f"   Contact: {lead.get('contact_info', 'N/A')}")
                print(f"   Location: {lead.get('location', 'N/A')}")
                print(f"   Description: {lead.get('description', 'N/A')[:100]}...")
            
            # Show data structure
            print("\n📊 Data Structure:")
            print(f"Total leads: {len(leads)}")
            print(f"Fields per lead: {len(leads[0].keys()) if leads else 0}")
            
            # List all available fields
            if leads:
                print("\n📝 Available fields:")
                for field in leads[0].keys():
                    print(f"   - {field}")
        
        else:
            print("❌ No leads found. This could be due to:")
            print("   - Invalid SerpAPI key")
            print("   - No results for the search terms")
            print("   - API rate limits exceeded")
    
    except Exception as e:
        print(f"❌ Error during search: {str(e)}")
        print("\n💡 Troubleshooting tips:")
        print("   - Check your SerpAPI key is valid")
        print("   - Ensure you have sufficient API credits")
        print("   - Try different search terms")

def demo_configuration():
    """Show configuration status"""
    print("\n⚙️ Configuration Status:")
    print("-" * 30)
    
    config_status = Config.get_api_keys_status()
    
    for key, status in config_status.items():
        status_icon = "✅" if status else "❌"
        print(f"{status_icon} {key}: {'Configured' if status else 'Not configured'}")
    
    print("\n📋 Required Setup:")
    print("1. Get SerpAPI key from https://serpapi.com/")
    print("2. Set environment variable: export SERPAPI_KEY='your_key'")
    print("3. For Google Sheets integration:")
    print("   - Set up Google Cloud project")
    print("   - Enable Google Sheets API")
    print("   - Create service account and download credentials")
    print("   - Set GOOGLE_SHEETS_CREDENTIALS_PATH")

def main():
    """Main demo function"""
    print("🚀 Lead Finder Automation Demo")
    print("="*50)
    
    # Show configuration status
    demo_configuration()
    
    # Demo lead search
    demo_lead_search()
    
    print("\n" + "="*50)
    print("🎉 Demo completed!")
    print("\n💡 To run the full application:")
    print("   source venv/bin/activate")
    print("   cd app")
    print("   streamlit run app.py")
    print("\n📖 For more information, see README.md")

if __name__ == "__main__":
    main() 