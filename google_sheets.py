import gspread, time
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
from contact import Contact
from creds import get_spreadsheet_name


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet_name = get_spreadsheet_name()
sheet = client.open(sheet_name).sheet1
starting_from_zero = True
next_available_row = 1

def get_sheet_records():
    list_of_hashes = sheet.get_all_records()
    # print(list_of_hashes)
    return list_of_hashes

def get_row_count(sheet):
    print(sheet.row_count)

def get_next_available_row(sheet):
    if starting_from_zero:
        return str(next_available_row)
    else:
        str_list = list(filter(None, sheet.col_values(1)))
    return str(len(str_list) + 1)

def write_contact_to_sheets(contact):
    row_number = get_next_available_row(sheet)
    columns = ['A', 'B', 'C', 'D', 'E', 'F']
    col_coords = [col + row_number for col in columns]

    time.sleep(0.5)
    # update first name (column A)
    sheet.update_acell(col_coords[0], contact.first_name)
    
    time.sleep(0.5)
    # update last name (column B)
    sheet.update_acell(col_coords[1], contact.last_name)

    time.sleep(0.5)
    # update email (column C)
    sheet.update_acell(col_coords[2], contact.email)

    time.sleep(0.5)
    # update MQL date (column D)
    sheet.update_acell(col_coords[3], str(contact.mql_date))

    time.sleep(0.5)
    # update today's date (column E)
    sheet.update_acell(col_coords[4], str(date.today()))

    time.sleep(0.5)
    # update formula column (column F)
    sheet.update_acell(col_coords[5], f"=DAYS(E{row_number}, D{row_number})")

    print(f'Contact {contact.email} recorded'
    next_available_row += 1
