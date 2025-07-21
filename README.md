# 🔍 Lead Finder Automation

A powerful automation tool that finds business leads using Google Search API and automatically saves them to Google Sheets. Built with Streamlit for a beautiful, user-friendly interface.

## ✨ Features

- **🔍 Smart Lead Search**: Search for businesses by niche and location
- **📊 Structured Data Extraction**: Extract business names, websites, contact info, and addresses
- **📈 Google Sheets Integration**: Automatically save leads to Google Sheets
- **🎨 Beautiful UI**: Modern Streamlit interface with real-time feedback
- **📥 CSV Export**: Download leads as CSV files
- **🔄 Data Cleaning**: Remove duplicates and clean extracted data
- **⚡ Fast & Efficient**: Optimized for quick lead generation

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd ai_location
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up API Keys

#### SerpAPI Key
1. Sign up at [SerpAPI](https://serpapi.com/)
2. Get your API key from the dashboard
3. Set environment variable:
```bash
export SERPAPI_KEY="your_serpapi_key_here"
```

#### Google Sheets Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable Google Sheets API and Google Drive API
4. Create a Service Account:
   - Go to "IAM & Admin" > "Service Accounts"
   - Click "Create Service Account"
   - Download the JSON credentials file
5. Share your Google Sheet with the service account email
6. Set environment variable:
```bash
export GOOGLE_SHEETS_CREDENTIALS_PATH="path/to/your/credentials.json"
export DEFAULT_SPREADSHEET_ID="your_spreadsheet_id_here"
```

### 4. Run the Application
```bash
cd app
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📋 Usage Guide

### Basic Usage
1. **Enter API Keys**: Input your SerpAPI key and upload Google Sheets credentials
2. **Configure Settings**: Set number of results and spreadsheet details
3. **Search for Leads**: Enter niche (e.g., "Interior Designers") and location (e.g., "Mumbai")
4. **Review Results**: View extracted leads in the data table
5. **Save to Sheets**: Click "Save to Google Sheets" to store the data
6. **Download CSV**: Optionally download leads as CSV file

### Advanced Features
- **Multiple Searches**: Run multiple searches and append to the same sheet
- **Data Validation**: Automatic cleaning and duplicate removal
- **Custom Formatting**: Google Sheets are automatically formatted for readability

## 🏗️ Project Structure

```
ai_location/
├── app/
│   ├── app.py              # Main Streamlit application
│   ├── lead_search.py      # Lead search and extraction logic
│   ├── sheets_writer.py    # Google Sheets integration
│   └── config.py           # Configuration and settings
├── requirements.txt         # Python dependencies
└── README.md              # This file
```

## 🔧 Configuration

### Environment Variables
```bash
# Required
export SERPAPI_KEY="your_serpapi_key"
export GOOGLE_SHEETS_CREDENTIALS_PATH="path/to/credentials.json"
export DEFAULT_SPREADSHEET_ID="your_spreadsheet_id"

# Optional
export DEFAULT_SHEET_NAME="Leads"
export DEFAULT_NUM_RESULTS="20"
export SEARCH_DELAY="1.0"
export OPENAI_API_KEY="your_openai_key"  # For advanced data cleaning
```

### Google Sheets Setup
1. Create a new Google Sheet
2. Copy the spreadsheet ID from the URL
3. Share the sheet with your service account email (found in credentials JSON)
4. The app will automatically create a "Leads" sheet if it doesn't exist

## 📊 Data Format

The app extracts and saves the following data fields:

| Field | Description |
|-------|-------------|
| Business Name | Extracted business name |
| Website | Business website URL |
| Address | Physical address (if available) |
| Phone | Contact phone number |
| Contact Info | Additional contact information |
| Niche | Original search niche |
| Location | Original search location |
| Description | Business description from search |
| Source URL | Original search result URL |
| Search Date | Date and time of search |

## 🛠️ API Integration

### SerpAPI
- **Purpose**: Google search results
- **Rate Limits**: 100 searches/month (free), 5000 searches/month (paid)
- **Features**: Local search, organic results, contact extraction

### Google Sheets API
- **Purpose**: Data storage and management
- **Authentication**: Service Account (OAuth 2.0)
- **Features**: Automatic formatting, duplicate handling, real-time updates

## 🔒 Privacy & Security

- **Data Privacy**: All data is processed locally, no data is stored on external servers
- **API Security**: API keys are handled securely and not exposed in the UI
- **Google Sheets**: Uses secure OAuth 2.0 authentication
- **Temporary Files**: Credentials are temporarily saved and automatically cleaned up

## 🚨 Troubleshooting

### Common Issues

1. **"Failed to authenticate with Google Sheets"**
   - Check if credentials JSON file is valid
   - Ensure service account has access to the spreadsheet
   - Verify Google Sheets API is enabled

2. **"No leads found"**
   - Check SerpAPI key is valid
   - Try different search terms
   - Verify location format

3. **"Error during search"**
   - Check internet connection
   - Verify SerpAPI key and quota
   - Try reducing number of results

### Debug Mode
Run with debug logging:
```bash
streamlit run app.py --logger.level=debug
```

## 📈 Performance Tips

- **Batch Processing**: Process multiple niches in sequence
- **Data Cleaning**: Enable automatic duplicate removal
- **Caching**: Results are cached for faster subsequent searches
- **Rate Limiting**: Respect API rate limits to avoid throttling

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue on GitHub
- Check the troubleshooting section above
- Review API documentation for SerpAPI and Google Sheets

---

**Made with ❤️ for lead generation automation** 