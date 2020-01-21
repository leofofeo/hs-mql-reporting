import google_sheets as gs

def write_contact_to_sheets(contact):
    gs.write_contact_to_sheets(contact)

def get_contacts_from_sheets():
    return gs.get_sheet_records()