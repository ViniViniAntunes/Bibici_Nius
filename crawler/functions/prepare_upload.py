import json

# Prepare the upload
def prepare_upload(file_path):
    '''
    Returns a dict with a BigQuery infos from JSON file

    :param file_path: string - Path to JSON file

    :return: dict
    '''
    
    with open(file_path) as file:
        output = json.load(file)
    file.close()

    return output
