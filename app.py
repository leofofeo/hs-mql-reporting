import requests, json, urllib, time
from contact import Contact
from build_params import build_parameters
from sheets_business_layer import write_contact_to_sheets, get_contacts_from_sheets

# hubspot api request config
max_results = 10000
base_url = "https://api.hubspot.com"
endpoint = "/contacts/v1/lists/all/contacts/all?"

headers = {}
vid_offset=0
contact_list = []
mql_list = []

has_more = True
print('starting while loop')
while has_more:
    parameters = build_parameters(vid_offset)
    get_url = base_url + endpoint + parameters
    r = requests.get(url=get_url, headers=headers)
    response_dict = json.loads(r.text)
    has_more = response_dict['has-more']
    contact_list.extend(response_dict['contacts'])
    vid_offset = str(response_dict['vid-offset'])
    if len(contact_list) >= max_results:
        print('maximum number of results exceeded')
        break

print('loop finished')
list_length = len(contact_list)
print(f"You've successfully parsed through {list_length} contact records and added them to a list")
for contact in contact_list:
    if contact['properties']['lifecyclestage']['value'] == 'marketingqualifiedlead':
        mql_list.append(contact)

for idx, contact in enumerate(mql_list):
    email = ''
    first_name = ''
    last_name = ''
    if 'email' in contact['properties']:
        email = contact['properties']['email']['value']
    if 'firstname' in contact['properties']:
        first_name = contact['properties']['firstname']['value']
    if 'lastname' in contact['properties']:
        last_name = contact['properties']['lastname']['value']
    became_mql_date_unformatted = contact['properties']['hs_lifecyclestage_marketingqualifiedlead_date']['value']
    formatted_mql_datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(became_mql_date_unformatted) / 1000.0))
    became_mql_date = formatted_mql_datetime.split(' ')[0]
    new_contact = Contact(first_name, last_name, email, became_mql_date)
    write_contact_to_sheets(new_contact)
    # if idx > 10:
    #     break

contacts = get_contacts_from_sheets()
