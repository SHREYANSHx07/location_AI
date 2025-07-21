#!/usr/bin/env python3
"""
API Key Setup Helper for Lead Finder Automation

This script helps you set up your SerpAPI key securely.
"""

import os
from pathlib import Path

def setup_api_key():
    """Help user set up their SerpAPI key"""
    
    print("🔑 SerpAPI Key Setup")
    print("="*40)
    
    # Check if key already exists
    existing_key = os.getenv('SERPAPI_KEY')
    if existing_key:
        print(f"✅ SerpAPI key already set: {existing_key[:10]}...")
        return True
    
    # Check for .env file
    env_file = Path(".env")
    if env_file.exists():
        print("📁 Found .env file")
        with open(env_file, "r") as f:
            content = f.read()
            if "SERPAPI_KEY=your_serpapi_key_here" in content:
                print("⚠️  API key not configured in .env file")
            elif "SERPAPI_KEY=" in content:
                print("✅ API key found in .env file")
                return True
    
    print("\n📋 Setup Options:")
    print("1. Create .env file with your API key")
    print("2. Set environment variable")
    print("3. Get SerpAPI key (if you don't have one)")
    print("4. Test existing setup")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        create_env_file()
    elif choice == "2":
        set_environment_variable()
    elif choice == "3":
        get_serpapi_key()
    elif choice == "4":
        test_setup()
    else:
        print("❌ Invalid choice")
        return False
    
    return True

def create_env_file():
    """Create .env file with user's API key"""
    
    print("\n📝 Creating .env file...")
    
    # Get API key from user
    api_key = input("Enter your SerpAPI key: ").strip()
    
    if not api_key:
        print("❌ API key cannot be empty")
        return False
    
    # Create .env file
    env_content = f"""# Lead Finder Automation - Environment Variables
# Add your API keys here

# Required API Keys
SERPAPI_KEY={api_key}
GOOGLE_SHEETS_CREDENTIALS_PATH=./google_credentials.json

# Optional Settings
DEFAULT_SHEET_NAME=Leads
DEFAULT_NUM_RESULTS=20
SEARCH_DELAY=1.0
"""
    
    with open(".env", "w") as f:
        f.write(env_content)
    
    print("✅ .env file created successfully!")
    print("🔒 Your API key is now stored securely")
    
    return True

def set_environment_variable():
    """Set environment variable"""
    
    print("\n🔧 Setting environment variable...")
    
    api_key = input("Enter your SerpAPI key: ").strip()
    
    if not api_key:
        print("❌ API key cannot be empty")
        return False
    
    # Set environment variable
    os.environ['SERPAPI_KEY'] = api_key
    
    print("✅ Environment variable set successfully!")
    print("💡 Note: This is temporary. For permanent setup, use .env file")
    
    return True

def get_serpapi_key():
    """Guide user to get SerpAPI key"""
    
    print("\n🔍 Getting SerpAPI Key")
    print("="*30)
    
    print("📋 Steps to get your SerpAPI key:")
    print("1. Go to https://serpapi.com/")
    print("2. Click 'Sign Up' or 'Get Started'")
    print("3. Create a free account")
    print("4. Go to your dashboard")
    print("5. Copy your API key")
    print("6. Come back and run this script again")
    
    print("\n💡 Free Plan includes:")
    print("   • 100 searches per month")
    print("   • Google search results")
    print("   • Local search results")
    
    input("\nPress Enter when you have your API key...")
    
    return True

def test_setup():
    """Test the current setup"""
    
    print("\n🧪 Testing Setup...")
    print("="*30)
    
    # Check environment variable
    env_key = os.getenv('SERPAPI_KEY')
    if env_key:
        print(f"✅ Environment variable: {env_key[:10]}...")
    else:
        print("❌ Environment variable not set")
    
    # Check .env file
    env_file = Path(".env")
    if env_file.exists():
        print("✅ .env file exists")
        with open(env_file, "r") as f:
            content = f.read()
            if "SERPAPI_KEY=your_serpapi_key_here" in content:
                print("⚠️  API key not configured in .env file")
            elif "SERPAPI_KEY=" in content:
                print("✅ API key found in .env file")
    else:
        print("❌ .env file not found")
    
    print("\n💡 To test with real API calls:")
    print("   python demo.py")

def main():
    """Main function"""
    
    print("🚀 Lead Finder Automation - API Key Setup")
    print("="*50)
    
    setup_api_key()
    
    print("\n" + "="*50)
    print("🎉 Setup completed!")
    print("\n💡 Next steps:")
    print("1. Run the app: python run.py")
    print("2. Test the API: python demo.py")
    print("3. Start searching for leads!")

if __name__ == "__main__":
    main() 