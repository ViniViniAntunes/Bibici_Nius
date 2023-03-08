from google.oauth2 import service_account

def credentials():
    '''
    Return a google.auth.service_account.Credentials object with the constructed credentials.
    
    No params.
    
    :return: google.auth.service_account.Credentials object
    '''
    key_path = 'creds\GBQ.json' # Insert here the path of your json credential file

    scopes = [
        'https://www.googleapis.com/auth/bigquery',
        'https://www.googleapis.com/auth/cloud-platform'
    ]

    credentials = service_account.Credentials.from_service_account_file(
        key_path,
        scopes=scopes
    )

    return credentials
