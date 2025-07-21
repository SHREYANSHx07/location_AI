import requests
import re
import json
from typing import List, Dict, Optional
from urllib.parse import urlparse
import time

class LeadFinder:
    def __init__(self, api_key: str):
        """
        Initialize the LeadFinder with SerpAPI key
        
        Args:
            api_key (str): SerpAPI key for searching
        """
        self.api_key = api_key
        self.base_url = "https://serpapi.com/search"
    
    def search_leads(self, niche: str, location: str, num_results: int = 20) -> List[Dict]:
        """
        Search for business leads based on niche and location
        
        Args:
            niche (str): Business niche/category
            location (str): Location to search in
            num_results (int): Number of results to fetch
            
        Returns:
            List[Dict]: List of lead dictionaries with business info
        """
        leads = []
        
        # Create search query
        search_query = f"{niche} in {location}"
        
        try:
            # Perform Google search using SerpAPI
            search_results = self._perform_search(search_query, num_results)
            
            # Extract leads from search results
            leads = self._extract_leads_from_results(search_results, niche, location)
            
            return leads
            
        except Exception as e:
            print(f"Error during lead search: {str(e)}")
            return []
    
    def _perform_search(self, query: str, num_results: int) -> Dict:
        """
        Perform Google search using SerpAPI
        
        Args:
            query (str): Search query
            num_results (int): Number of results to fetch
            
        Returns:
            Dict: Search results from SerpAPI
        """
        params = {
            'q': query,
            'api_key': self.api_key,
            'engine': 'google',
            'num': min(num_results, 100),  # SerpAPI limit
            'gl': 'us',  # Country code
            'hl': 'en'   # Language
        }
        
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        
        return response.json()
    
    def _extract_leads_from_results(self, search_results: Dict, niche: str, location: str) -> List[Dict]:
        """
        Extract structured lead data from search results
        
        Args:
            search_results (Dict): Raw search results from SerpAPI
            niche (str): Original niche for context
            location (str): Original location for context
            
        Returns:
            List[Dict]: List of structured lead data
        """
        leads = []
        
        # Extract organic results
        organic_results = search_results.get('organic_results', [])
        
        for result in organic_results:
            try:
                lead = self._extract_lead_from_result(result, niche, location)
                if lead:
                    leads.append(lead)
            except Exception as e:
                print(f"Error extracting lead from result: {str(e)}")
                continue
        
        # Extract local results if available
        local_results = search_results.get('local_results', [])
        for result in local_results:
            try:
                # Check if result is a dictionary
                if isinstance(result, dict):
                    lead = self._extract_local_lead_from_result(result, niche, location)
                    if lead:
                        leads.append(lead)
                else:
                    print(f"Skipping non-dict local result: {type(result)}")
            except Exception as e:
                print(f"Error extracting local lead from result: {str(e)}")
                continue
        
        return leads
    
    def _extract_lead_from_result(self, result: Dict, niche: str, location: str) -> Optional[Dict]:
        """
        Extract lead information from a single search result
        
        Args:
            result (Dict): Single search result
            niche (str): Original niche
            location (str): Original location
            
        Returns:
            Optional[Dict]: Structured lead data or None
        """
        title = result.get('title', '')
        link = result.get('link', '')
        snippet = result.get('snippet', '')
        
        # Skip if no meaningful data
        if not title or not link:
            return None
        
        # Extract business name from title
        business_name = self._extract_business_name(title)
        
        # Extract website from link
        website = self._extract_website(link)
        
        # Extract contact information from snippet
        contact_info = self._extract_contact_info(snippet)
        
        # Create lead dictionary
        lead = {
            'business_name': business_name,
            'website': website,
            'title': title,
            'description': snippet,
            'contact_info': contact_info,
            'niche': niche,
            'location': location,
            'source_url': link,
            'search_date': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return lead
    
    def _extract_local_lead_from_result(self, result: Dict, niche: str, location: str) -> Optional[Dict]:
        """
        Extract lead information from a local search result
        
        Args:
            result (Dict): Local search result
            niche (str): Original niche
            location (str): Original location
            
        Returns:
            Optional[Dict]: Structured lead data or None
        """
        title = result.get('title', '')
        address = result.get('address', '')
        phone = result.get('phone', '')
        website = result.get('website', '')
        
        # Skip if no meaningful data
        if not title:
            return None
        
        # Extract business name
        business_name = self._extract_business_name(title)
        
        # Extract website if not provided
        if not website:
            website = self._extract_website_from_snippet(result.get('snippet', ''))
        
        # Create lead dictionary
        lead = {
            'business_name': business_name,
            'website': website,
            'address': address,
            'phone': phone,
            'title': title,
            'description': result.get('snippet', ''),
            'contact_info': f"Phone: {phone}, Address: {address}" if phone or address else '',
            'niche': niche,
            'location': location,
            'source_url': result.get('link', ''),
            'search_date': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return lead
    
    def _extract_business_name(self, title: str) -> str:
        """
        Extract business name from search result title
        
        Args:
            title (str): Search result title
            
        Returns:
            str: Extracted business name
        """
        # Remove common suffixes and prefixes
        suffixes = [' - Home', ' - Official Website', ' | ', ' - ', ' – ', ' — ']
        name = title
        
        for suffix in suffixes:
            if suffix in name:
                name = name.split(suffix)[0]
        
        # Remove website extensions
        name = re.sub(r'\.(com|org|net|co|in|uk)$', '', name, flags=re.IGNORECASE)
        
        return name.strip()
    
    def _extract_website(self, link: str) -> str:
        """
        Extract website URL from search result link
        
        Args:
            link (str): Search result link
            
        Returns:
            str: Website URL
        """
        try:
            parsed = urlparse(link)
            if parsed.netloc:
                return f"{parsed.scheme}://{parsed.netloc}"
        except:
            pass
        
        return link
    
    def _extract_website_from_snippet(self, snippet: str) -> str:
        """
        Extract website from snippet text
        
        Args:
            snippet (str): Search result snippet
            
        Returns:
            str: Extracted website or empty string
        """
        # Look for website patterns in snippet
        website_pattern = r'https?://[^\s]+'
        matches = re.findall(website_pattern, snippet)
        
        if matches:
            return matches[0]
        
        return ""
    
    def _extract_contact_info(self, snippet: str) -> str:
        """
        Extract contact information from snippet
        
        Args:
            snippet (str): Search result snippet
            
        Returns:
            str: Extracted contact information
        """
        contact_info = []
        
        # Extract phone numbers
        phone_pattern = r'(\+?[\d\s\-\(\)]{10,})'
        phones = re.findall(phone_pattern, snippet)
        if phones:
            contact_info.append(f"Phone: {phones[0]}")
        
        # Extract email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, snippet)
        if emails:
            contact_info.append(f"Email: {emails[0]}")
        
        return ', '.join(contact_info)
    
    def clean_and_validate_leads(self, leads: List[Dict]) -> List[Dict]:
        """
        Clean and validate extracted leads
        
        Args:
            leads (List[Dict]): Raw leads data
            
        Returns:
            List[Dict]: Cleaned and validated leads
        """
        cleaned_leads = []
        
        for lead in leads:
            # Remove duplicates based on business name and website
            if not any(
                existing['business_name'] == lead['business_name'] and 
                existing['website'] == lead['website'] 
                for existing in cleaned_leads
            ):
                # Clean business name
                lead['business_name'] = lead['business_name'].strip()
                
                # Ensure website has proper format
                if lead['website'] and not lead['website'].startswith(('http://', 'https://')):
                    lead['website'] = f"https://{lead['website']}"
                
                cleaned_leads.append(lead)
        
        return cleaned_leads 