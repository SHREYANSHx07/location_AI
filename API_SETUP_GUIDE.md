# 🔑 API Key Setup Guide

## Where to Add Your SerpAPI Key

You have **3 secure options** to add your SerpAPI key. **Never add API keys directly in the code!**

### Option 1: Environment Variable (Recommended)

```bash
# Set the environment variable
export SERPAPI_KEY="your_actual_serpapi_key_here"

# Then run the app
python run.py
```

### Option 2: .env File (Easiest)

1. **Create a `.env` file** in your project root:
```bash
# Copy the template
cp env_template.txt .env
```

2. **Edit the `.env` file** and replace the placeholder:
```bash
# Open the file
nano .env

# Or use any text editor and change this line:
SERPAPI_KEY=your_actual_serpapi_key_here
```

3. **Run the app**:
```bash
python run.py
```

### Option 3: Through the Streamlit UI

1. **Run the app** without setting the environment variable
2. **Enter your SerpAPI key** in the sidebar of the Streamlit app
3. **The app will use the key** you enter in the UI

## 🔍 How to Get Your SerpAPI Key

1. **Go to** https://serpapi.com/
2. **Sign up** for a free account
3. **Get your API key** from the dashboard
4. **Copy the key** and use one of the methods above

## ✅ Testing Your API Key

Run this command to test if your key works:

```bash
# Set your key
export SERPAPI_KEY="your_key_here"

# Test the key
python demo.py
```

## 🔒 Security Best Practices

- ✅ **Use environment variables** or `.env` files
- ✅ **Never commit API keys** to version control
- ✅ **Use different keys** for development and production
- ❌ **Never hardcode keys** in your source code
- ❌ **Never share your keys** publicly

## 📁 File Structure

```
ai_location/
├── .env                    # Your API keys (create this)
├── env_template.txt        # Template for .env file
├── app/                    # Application code
├── demo_leads.csv          # Demo data
└── README.md              # Documentation
```

## 🚀 Quick Start

1. **Get your SerpAPI key** from https://serpapi.com/
2. **Create `.env` file**:
   ```bash
   cp env_template.txt .env
   ```
3. **Edit `.env`** and add your key
4. **Run the app**:
   ```bash
   python run.py
   ```

## 🆘 Troubleshooting

### "API key not found" error
- Check if you set the environment variable correctly
- Verify the `.env` file exists and has the correct format
- Make sure there are no extra spaces in the `.env` file

### "Invalid API key" error
- Verify your SerpAPI key is correct
- Check if you have sufficient API credits
- Ensure the key is active in your SerpAPI dashboard

### "No results found" error
- Try different search terms
- Check if your API key has search permissions
- Verify your SerpAPI account is active 