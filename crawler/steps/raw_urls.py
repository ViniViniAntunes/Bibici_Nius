from crawler.functions.get_html_from_page import get_html_from_page

def raw_urls():
    '''
    Returns a list with all URLs crawled from main page https://www.bbc.com.
    
    :param url: string
    
    :return: list
    '''
    site_url = 'https://www.bbc.com'

    # Getting the HTML from main page
    soup = get_html_from_page(site_url)

    raw_urls = []

    # Fetch the tag where the links are
    bs_news = soup.findAll('h3', {'class': 'media__title'})

    for item in bs_news:
        if item.a.get('href')[0] == '/':
            raw_urls.append(site_url + item.a.get('href'))
        else:
            raw_urls.append(item.a.get('href'))
    
    return raw_urls
