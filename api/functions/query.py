import pandas as pd

from crawler.functions.get_GBQ_infos import get_GBQ_infos
from creds.credentials import credentials

def query(keyword, all_articles=False):
    '''
    Returns a dict with the informations of the article whose headline contains `keyword`.
    
    :param keywords: string
    :param all_articles: bool
        Default False. If True, returns the informations of all articles in the BigQuery table (around 30 articles).
    
    :return: dict
    '''
    infos_BQ = get_GBQ_infos('crawler\infos\BigQuery_infos.json')
    
    project_id = infos_BQ['project_id']
    dataset_id = infos_BQ['dataset_id']
    table_id = infos_BQ['table_id']

    all = ''
    
    if all_articles:
        all = '--'

    query_str=f'''
        SELECT
            *
        FROM
            `{project_id}.{dataset_id}.{table_id}`
        {all}WHERE CONTAINS_SUBSTR(Headline, "{keyword}")
    '''

    output = pd.read_gbq(
        query=query_str,
        credentials=credentials(),
        project_id=project_id
    )

    output['Publication_datetime'] = output['Publication_datetime'].astype(str)

    return output
