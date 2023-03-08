def remove_items(raw_urls, trash_list):
    '''
    Removes from list `raw_urls` the elements of list `trash_list` and returns the clean list.
    
    :param raw_urls: list
    :param trash_list: list
    
    :return: list
    '''
    urls = raw_urls.copy()

    for trash in trash_list:
        urls.remove(trash)

    return urls
