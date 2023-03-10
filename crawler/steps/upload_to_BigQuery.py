from creds.credentials import credentials
from crawler.functions.get_GBQ_infos import get_GBQ_infos

def upload_to_BigQuery(data):
    '''
    Upload data from a pandas DataFrame. An error is thrown if there is a connection problem.
    
    :param data: pandas DataFrame
    
    :return: no return.
    '''
    
    infos_BQ = get_GBQ_infos('crawler\infos\BigQuery_infos.json')
    
    project_id = infos_BQ['project_id']
    dataset_id = infos_BQ['dataset_id']
    table_id = infos_BQ['table_id']
    if_exists = infos_BQ['if_exists']
    table_schema = infos_BQ['table_schema']

    destination_table = f'{dataset_id}.{table_id}'

    try:
        data.to_gbq(
            credentials=credentials(),
            destination_table=destination_table,
            if_exists=if_exists,
            project_id=project_id,
            table_schema=table_schema
        )
        print(f'Successfully uploaded to "{project_id}.{destination_table}" !!!')
    except:
        ConnectionError(f'Error when trying to upload data to BigQuery')
