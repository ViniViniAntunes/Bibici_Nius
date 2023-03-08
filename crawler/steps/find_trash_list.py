def find_trash_list(raw_urls):
    '''
    Filter `raw_urls` and returns a list of URL in string format that will be descarted.
    Only pages with `/news/` will pass.
    
    :param raw_urls: list
    
    :return: list
    '''
    trash_list = []

    for item in raw_urls:
        if item.find('/news/') == -1:
            trash_list.append(item)

    return trash_list
