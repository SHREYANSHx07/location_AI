import os
from typing import Optional

class Config:
    """Configuration class for the Lead Finder Automation app"""
    
    # API Keys
    SERPAPI_KEY: Optional[str] = None
    OPENAI_API_KEY: Optional[str] = None
    
    # Google Sheets Configuration
    GOOGLE_SHEETS_CREDENTIALS_PATH: Optional[str] = None
    DEFAULT_SPREADSHEET_ID: Optional[str] = None
    DEFAULT_SHEET_NAME: str = "Leads"
    
    # Search Configuration
    DEFAULT_NUM_RESULTS: int = 20
    MAX_NUM_RESULTS: int = 100
    SEARCH_DELAY: float = 1.0  # Delay between searches in seconds
    
    # Data Processing
    ENABLE_DATA_CLEANING: bool = True
    ENABLE_DUPLICATE_REMOVAL: bool = True
    ENABLE_OPENAI_CLEANING: bool = False  # Optional OpenAI data cleaning
    
    # UI Configuration
    APP_TITLE: str = "Lead Finder Automation"
    APP_ICON: str = "🔍"
    PAGE_LAYOUT: str = "wide"
    
    @classmethod
    def load_from_env(cls):
        """Load configuration from environment variables"""
        cls.SERPAPI_KEY = os.getenv('SERPAPI_KEY')
        cls.OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
        cls.GOOGLE_SHEETS_CREDENTIALS_PATH = os.getenv('GOOGLE_SHEETS_CREDENTIALS_PATH')
        cls.DEFAULT_SPREADSHEET_ID = os.getenv('DEFAULT_SPREADSHEET_ID')
        
        # Optional settings
        if os.getenv('DEFAULT_SHEET_NAME'):
            cls.DEFAULT_SHEET_NAME = os.getenv('DEFAULT_SHEET_NAME')
        
        if os.getenv('DEFAULT_NUM_RESULTS'):
            try:
                cls.DEFAULT_NUM_RESULTS = int(os.getenv('DEFAULT_NUM_RESULTS'))
            except ValueError:
                pass
        
        if os.getenv('SEARCH_DELAY'):
            try:
                cls.SEARCH_DELAY = float(os.getenv('SEARCH_DELAY'))
            except ValueError:
                pass
    
    @classmethod
    def validate_config(cls) -> bool:
        """Validate that required configuration is present"""
        missing_keys = []
        
        if not cls.SERPAPI_KEY:
            missing_keys.append("SERPAPI_KEY")
        
        if not cls.GOOGLE_SHEETS_CREDENTIALS_PATH:
            missing_keys.append("GOOGLE_SHEETS_CREDENTIALS_PATH")
        
        if missing_keys:
            print(f"Missing required configuration: {', '.join(missing_keys)}")
            return False
        
        return True
    
    @classmethod
    def get_api_keys_status(cls) -> dict:
        """Get status of API keys configuration"""
        return {
            'serpapi_key': bool(cls.SERPAPI_KEY),
            'openai_key': bool(cls.OPENAI_API_KEY),
            'google_sheets_creds': bool(cls.GOOGLE_SHEETS_CREDENTIALS_PATH),
            'spreadsheet_id': bool(cls.DEFAULT_SPREADSHEET_ID)
        }

# Load configuration from environment variables
Config.load_from_env()

# Example environment variables to set:
# export SERPAPI_KEY="your_serpapi_key_here"
# export OPENAI_API_KEY="your_openai_key_here"  # Optional
# export GOOGLE_SHEETS_CREDENTIALS_PATH="path/to/credentials.json"
# export DEFAULT_SPREADSHEET_ID="your_spreadsheet_id_here" 