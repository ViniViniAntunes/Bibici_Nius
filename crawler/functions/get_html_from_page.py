from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_html_from_page(url):
    '''
    Returns a BeutifulSoup object given an URL in string format.
    
    :param url: string
    
    :return: BeautifulSoup object
    '''
    response = urlopen(url)
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    return soup
