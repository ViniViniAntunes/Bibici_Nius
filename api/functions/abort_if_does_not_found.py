from flask_restful import abort

def abort_if_does_not_found(keyword):
    '''
    Launch a 404 error message if `keyword` doesn't found.
    
    :param keyword: string
    
    :return: None
    '''
    abort(404, message=f"Sorry! No article was found with the keyword '{keyword}' in the headline.")
