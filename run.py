import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('calculate_resistance')

def get_vi_data():
    """
    Get the voltage and current data from the user
    """
    print("Please put in the voltage and current data from your experiment")
    print("Data should be two numbers separated with commas.") 
    print("e.g. 2, 0.8")    

    data_str = input("Enter your data here:")
    print(f"The data entered is {data_str}")
    
get_vi_data()