import streamlit as st
import pandas as pd
from lead_search import LeadFinder
from sheets_writer import GoogleSheetsWriter
import os
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Lead Finder Automation",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-header">🔍 Lead Finder Automation</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Find business leads and automatically save them to Google Sheets</p>', unsafe_allow_html=True)
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # API Keys
        st.subheader("API Keys")
        
        # Use the default SerpAPI key
        serpapi_key = "a1b74d41b1564537886ff610b084f23a73d0619c03ce31744e72e6190dacd009"
        st.success(f"✅ SerpAPI Key configured (Primary Key)")
        
        google_sheets_creds = st.file_uploader("Google Sheets Credentials JSON", type="json", help="Upload your Google Sheets service account credentials (optional)")
        
        # Search Settings
        st.subheader("Search Settings")
        num_results = st.slider("Number of results to fetch", min_value=5, max_value=50, value=20)
        
        # Google Sheets Settings
        st.subheader("Google Sheets Settings")
        spreadsheet_id = st.text_input("Spreadsheet ID", help="Enter your Google Sheets spreadsheet ID")
        sheet_name = st.text_input("Sheet Name", value="Leads", help="Name of the sheet to save data")
        
        st.markdown("---")
        st.markdown("### 📋 Instructions")
        st.markdown("""
        1. SerpAPI key is pre-configured ✅
        2. Enter niche and location below
        3. Click 'Find Leads' to start
        4. Google Sheets integration is optional
        """)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("🎯 Lead Search")
        
        # Input fields
        niche = st.text_input("Niche", placeholder="e.g., Interior Designers, Digital Marketing Agencies, etc.")
        location = st.text_input("Location", placeholder="e.g., Mumbai, New York, London, etc.")
        
        # Search button
        if st.button("🔍 Find Leads", type="primary", use_container_width=True):
            if not all([niche, location]):
                st.error("Please fill in Niche and Location to search for leads.")
                return
            
            try:
                # Initialize lead finder
                lead_finder = LeadFinder(serpapi_key)
                
                # Show progress
                with st.spinner("Searching for leads..."):
                    leads = lead_finder.search_leads(niche, location, num_results)
                
                if leads:
                    st.success(f"✅ Found {len(leads)} leads!")
                    
                    # Display results
                    st.subheader("📊 Found Leads")
                    df = pd.DataFrame(leads)
                    st.dataframe(df, use_container_width=True)
                    
                    # Save to Google Sheets
                    if st.button("💾 Save to Google Sheets", type="secondary"):
                        with st.spinner("Saving to Google Sheets..."):
                            # Save credentials temporarily
                            creds_path = "temp_creds.json"
                            with open(creds_path, "w") as f:
                                f.write(google_sheets_creds.getvalue().decode())
                            
                            try:
                                sheets_writer = GoogleSheetsWriter(creds_path)
                                sheets_writer.save_leads(leads, spreadsheet_id, sheet_name)
                                st.success("✅ Leads saved to Google Sheets successfully!")
                                
                                # Clean up temp file
                                os.remove(creds_path)
                                
                            except Exception as e:
                                st.error(f"❌ Error saving to Google Sheets: {str(e)}")
                                if os.path.exists(creds_path):
                                    os.remove(creds_path)
                    
                    # Download CSV option
                    csv = df.to_csv(index=False)
                    st.download_button(
                        label="📥 Download as CSV",
                        data=csv,
                        file_name=f"leads_{niche}_{location}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        mime="text/csv"
                    )
                    
                else:
                    st.warning("No leads found. Try adjusting your search terms.")
                    
            except Exception as e:
                st.error(f"❌ Error during search: {str(e)}")
    
    with col2:
        st.header("📋 Quick Tips")
        
        st.info("""
        **💡 Search Tips:**
        - Be specific with your niche
        - Use city names for better results
        - Try different variations of business types
        """)
        
        st.markdown("---")
        
        st.header("🔗 Useful Links")
        st.markdown("""
        - [SerpAPI Dashboard](https://serpapi.com/dashboard)
        - [Google Sheets](https://sheets.google.com)
        - [Google Cloud Console](https://console.cloud.google.com)
        """)

if __name__ == "__main__":
    main() 