from creds import get_hapi_key

def build_parameters(vid_offset):
    hapi_key = get_hapi_key()
    property_email = "email"
    property_became_mql = "hs_lifecyclestage_marketingqualifiedlead_date"
    property_lcs = 'lifecyclestage'
    property_first_name = 'firstname'
    property_last_name = 'lastname'
    form_submission_mode = 'none'
    
    parameters = ''
    parameters += 'property=' + property_first_name
    parameters += '&property=' + property_last_name
    parameters += '&property=' + property_email
    parameters += '&property=' + property_lcs
    parameters += '&property=' + property_became_mql
    parameters += '&formSubmissionMode=' + form_submission_mode
    parameters += '&vidOffset=' + str(vid_offset)
    parameters += '&hapikey=' + hapi_key
    return parameters