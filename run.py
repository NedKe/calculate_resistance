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
    
    vi_data = data_str.split(",")
    validate_data(vi_data)
    

def validate_data(values):
    """
    In the try, converts string values into numbers, integers or floats,
    if strings can not be convereted or there are more than two input, it raises error.
    """
    try: 
        [float(value) for value in values]
        if len(values) != 2:
            raise ValueError(
              f"Exactly two values required, you entered {len(values)}"
        )
    except ValueError as e:
        print(f"Invalid data:{e}, please try again.\n")

get_vi_data()


