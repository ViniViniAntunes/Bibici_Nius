import pandas as pd

from creds.credentials import credentials

def query(keyword, all_articles=False):
    '''
    Returns a dict with the informations of the article whose headline contains `keyword`.
    
    :param keywords: string
    :param all_articles: bool
        Default False. If True, returns the informations of all articles in the BigQuery table (around 30 articles).
    
    :return: dict
    '''

    project_id = 'vini-project-379618'
    all = ''
    
    if all_articles:
        all = '--'

    query_str=f'''
        SELECT
            *
        FROM
            `{project_id}.coding_test_lima_consulting.bbc_news`
        {all}WHERE CONTAINS_SUBSTR(Headline, "{keyword}")
    '''

    output = pd.read_gbq(
        query=query_str,
        credentials=credentials(),
        project_id=project_id
    )

    output['Publication_datetime'] = output['Publication_datetime'].astype(str)

    return output
