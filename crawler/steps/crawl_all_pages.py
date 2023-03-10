from crawler.functions.get_html_from_page import get_html_from_page
import time
from datetime import datetime
import pandas as pd

def crawl_all_pages(urls):
    '''
    Returns a pandas DataFrame with the informations of the articles crawled from bbc.com'.
    
    :param urls: list
    
    :return: pandas DataFrame
    '''

    redirected_urls = []
    headlines = []
    authors = []
    publications_date_time = []
    article_texts = []

    print('Wait few seconds. Crawling pages...')

    for url in urls:
        
        # Getting the HTML from each page
        soup_page = get_html_from_page(url)
        time.sleep(1)

    ###############################################################################
        # URLs redirected
        redirected = soup_page.find('head').find('meta', {'property': 'og:url'}).get('content')
        redirected_urls.append(redirected)


    ###############################################################################
        # Headlines
        title = soup_page.find('article').h1.get_text()
        headlines.append(title)


    ###############################################################################
        # Authors
        authors_names = []
        final_name = 'Author not identified'

        try:
            by_line_block = soup_page.find('article').find('div', {'data-component': 'byline-block'})
            tag_div_author = by_line_block.find('div', {'class': 'ssrcss-68pt20-Text-TextContributorName e8mq1e96'})
            complete_by_line = tag_div_author.get_text().split('By ')[1].split('&')
            
            # Sometimes there are more than one author
            for n, author in enumerate(complete_by_line):
                final_name = author.split(' and ')[0].split(' in ')[0].strip().split('BBC')[0]
                authors_names.append(final_name)
        
        
        # Some pages have no author on the front-end (pages with videos or photos only)
        except:
            # print(f'Redirected url without author\n{redirected}', end='\n\n') # Only developer check
            authors_names.append(final_name)
        
        authors.append(authors_names)


    ###############################################################################
        # Publication dates and times
        try:
            str_format = soup_page.findAll('time')[0].get('datetime')
            
            # Transforming the format
            for char in ['.', '+']:
                if str_format.find(char) != -1:
                    dt_format = datetime.strptime(str_format.split(char)[0], '%Y-%m-%dT%H:%M:%S')
            publications_date_time.append(dt_format)

        except:
            print('Error in datetime')


    ###############################################################################
        # Article texts
        try:
            paragraph = []
            text_block = soup_page.findAll('div', {'data-component': 'text-block'})

            # For pages with only videos, I get the video descriptions
            if text_block == []:

                tag_article = soup_page.find('article').find('div', {'data-testid': 'reveal-text-wrapper'})
                paragraphs_list = tag_article.findAll('p')

                video_description = []

                # The video descriptions are separated in more than one tag `p`
                for p in paragraphs_list:
                    
                    video_description.append(p.get_text().strip())
                
                # Merging all the texts in each tag and separating them with `\n`
                article_texts.append('\n'.join(video_description))
            
            # For pages with text
            else:

                # The article text are separated in more than one tag `div`
                for block in text_block:
                    paragraph.append(block.get_text().strip())
                    
                    try:
                        # Some article texts have subheadings in the middle and without them the text could be meaningless
                        if block.next_sibling['data-component'] == 'subheadline-block':
                            paragraph.append(block.next_sibling.get_text())
                    except:
                        pass
                
                # Merging all the texts in each tag and separating them with `\n`
                article_texts.append('\n'.join(paragraph))
        except:
            print('Error in text')
    
    data_dict = {
        'Headline': headlines,
        'Authors': authors,
        'Publication_datetime': publications_date_time,
        'Article': article_texts,
        "URL": urls,
        'Redirected_URL': redirected_urls
    }

    data = pd.DataFrame(data_dict)

    print(f'Crawling finished!')
    print(f'{data.shape[0]} articles were founded')
    
    for col in data.columns:
        if col != 'Publication_datetime':
            data[col] = data[col].astype(str)
    
    return data
