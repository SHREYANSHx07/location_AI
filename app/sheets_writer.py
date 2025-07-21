import gspread
from google.oauth2.service_account import Credentials
from typing import List, Dict
import pandas as pd
from datetime import datetime

class GoogleSheetsWriter:
    def __init__(self, credentials_path: str):
        """
        Initialize Google Sheets writer with service account credentials
        
        Args:
            credentials_path (str): Path to Google service account JSON file
        """
        self.credentials_path = credentials_path
        self.scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        self.client = None
        self._authenticate()
    
    def _authenticate(self):
        """Authenticate with Google Sheets API"""
        try:
            credentials = Credentials.from_service_account_file(
                self.credentials_path, 
                scopes=self.scope
            )
            self.client = gspread.authorize(credentials)
        except Exception as e:
            raise Exception(f"Failed to authenticate with Google Sheets: {str(e)}")
    
    def save_leads(self, leads: List[Dict], spreadsheet_id: str, sheet_name: str = "Leads") -> bool:
        """
        Save leads data to Google Sheets
        
        Args:
            leads (List[Dict]): List of lead dictionaries
            spreadsheet_id (str): Google Sheets spreadsheet ID
            sheet_name (str): Name of the sheet to write to
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Open the spreadsheet
            spreadsheet = self.client.open_by_key(spreadsheet_id)
            
            # Try to get existing sheet, create if doesn't exist
            try:
                worksheet = spreadsheet.worksheet(sheet_name)
            except gspread.WorksheetNotFound:
                worksheet = spreadsheet.add_worksheet(title=sheet_name, rows=1000, cols=20)
            
            # Prepare data for writing
            headers = self._get_headers()
            data_rows = self._prepare_data_rows(leads, headers)
            
            # Clear existing data and write new data
            worksheet.clear()
            worksheet.update('A1', [headers])
            if data_rows:
                worksheet.update('A2', data_rows)
            
            # Format the sheet
            self._format_sheet(worksheet, len(headers), len(data_rows) + 1)
            
            return True
            
        except Exception as e:
            print(f"Error saving to Google Sheets: {str(e)}")
            return False
    
    def _get_headers(self) -> List[str]:
        """Get the headers for the leads data"""
        return [
            'Business Name',
            'Website',
            'Address',
            'Phone',
            'Contact Info',
            'Niche',
            'Location',
            'Description',
            'Source URL',
            'Search Date'
        ]
    
    def _prepare_data_rows(self, leads: List[Dict], headers: List[str]) -> List[List]:
        """
        Prepare data rows for Google Sheets
        
        Args:
            leads (List[Dict]): Lead data
            headers (List[str]): Column headers
            
        Returns:
            List[List]: Data rows ready for Google Sheets
        """
        data_rows = []
        
        for lead in leads:
            row = []
            for header in headers:
                # Map headers to lead data fields
                if header == 'Business Name':
                    row.append(lead.get('business_name', ''))
                elif header == 'Website':
                    row.append(lead.get('website', ''))
                elif header == 'Address':
                    row.append(lead.get('address', ''))
                elif header == 'Phone':
                    row.append(lead.get('phone', ''))
                elif header == 'Contact Info':
                    row.append(lead.get('contact_info', ''))
                elif header == 'Niche':
                    row.append(lead.get('niche', ''))
                elif header == 'Location':
                    row.append(lead.get('location', ''))
                elif header == 'Description':
                    row.append(lead.get('description', ''))
                elif header == 'Source URL':
                    row.append(lead.get('source_url', ''))
                elif header == 'Search Date':
                    row.append(lead.get('search_date', ''))
                else:
                    row.append('')
            
            data_rows.append(row)
        
        return data_rows
    
    def _format_sheet(self, worksheet, num_cols: int, num_rows: int):
        """
        Format the Google Sheet for better readability
        
        Args:
            worksheet: Google Sheets worksheet object
            num_cols (int): Number of columns
            num_rows (int): Number of rows
        """
        try:
            # Format header row
            worksheet.format('A1:J1', {
                'backgroundColor': {
                    'red': 0.2,
                    'green': 0.6,
                    'blue': 0.9
                },
                'textFormat': {
                    'bold': True,
                    'foregroundColor': {
                        'red': 1,
                        'green': 1,
                        'blue': 1
                    }
                },
                'horizontalAlignment': 'CENTER'
            })
            
            # Auto-resize columns
            for col in range(1, num_cols + 1):
                worksheet.set_column_width(col, 150)
            
            # Add borders
            worksheet.format(f'A1:J{num_rows}', {
                'borders': {
                    'top': {'style': 'SOLID'},
                    'bottom': {'style': 'SOLID'},
                    'left': {'style': 'SOLID'},
                    'right': {'style': 'SOLID'}
                }
            })
            
        except Exception as e:
            print(f"Warning: Could not format sheet: {str(e)}")
    
    def append_leads(self, leads: List[Dict], spreadsheet_id: str, sheet_name: str = "Leads") -> bool:
        """
        Append leads to existing Google Sheet (without clearing existing data)
        
        Args:
            leads (List[Dict]): List of lead dictionaries
            spreadsheet_id (str): Google Sheets spreadsheet ID
            sheet_name (str): Name of the sheet to write to
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Open the spreadsheet
            spreadsheet = self.client.open_by_key(spreadsheet_id)
            
            # Try to get existing sheet, create if doesn't exist
            try:
                worksheet = spreadsheet.worksheet(sheet_name)
            except gspread.WorksheetNotFound:
                worksheet = spreadsheet.add_worksheet(title=sheet_name, rows=1000, cols=20)
                # Add headers for new sheet
                headers = self._get_headers()
                worksheet.update('A1', [headers])
            
            # Prepare data for writing
            headers = self._get_headers()
            data_rows = self._prepare_data_rows(leads, headers)
            
            # Append data to existing sheet
            if data_rows:
                # Find the next empty row
                all_values = worksheet.get_all_values()
                next_row = len(all_values) + 1
                
                # Append data
                worksheet.update(f'A{next_row}', data_rows)
            
            return True
            
        except Exception as e:
            print(f"Error appending to Google Sheets: {str(e)}")
            return False
    
    def get_existing_leads(self, spreadsheet_id: str, sheet_name: str = "Leads") -> List[Dict]:
        """
        Get existing leads from Google Sheet
        
        Args:
            spreadsheet_id (str): Google Sheets spreadsheet ID
            sheet_name (str): Name of the sheet to read from
            
        Returns:
            List[Dict]: List of existing leads
        """
        try:
            # Open the spreadsheet
            spreadsheet = self.client.open_by_key(spreadsheet_id)
            
            # Get the worksheet
            worksheet = spreadsheet.worksheet(sheet_name)
            
            # Get all values
            all_values = worksheet.get_all_values()
            
            if len(all_values) < 2:  # No data or only headers
                return []
            
            # Convert to list of dictionaries
            headers = all_values[0]
            leads = []
            
            for row in all_values[1:]:
                lead = {}
                for i, header in enumerate(headers):
                    if i < len(row):
                        lead[header.lower().replace(' ', '_')] = row[i]
                    else:
                        lead[header.lower().replace(' ', '_')] = ''
                leads.append(lead)
            
            return leads
            
        except Exception as e:
            print(f"Error reading from Google Sheets: {str(e)}")
            return []
    
    def create_spreadsheet(self, title: str) -> str:
        """
        Create a new Google Spreadsheet
        
        Args:
            title (str): Title of the spreadsheet
            
        Returns:
            str: Spreadsheet ID
        """
        try:
            spreadsheet = self.client.create(title)
            return spreadsheet.id
        except Exception as e:
            raise Exception(f"Failed to create spreadsheet: {str(e)}")
    
    def share_spreadsheet(self, spreadsheet_id: str, email: str, role: str = "writer"):
        """
        Share a Google Spreadsheet with someone
        
        Args:
            spreadsheet_id (str): Google Sheets spreadsheet ID
            email (str): Email address to share with
            role (str): Role (reader, writer, owner)
        """
        try:
            spreadsheet = self.client.open_by_key(spreadsheet_id)
            spreadsheet.share(email, perm_type='user', role=role)
        except Exception as e:
            print(f"Error sharing spreadsheet: {str(e)}") 