from flask_restful import Resource

from api.functions.query import query
from api.functions.abort_if_does_not_found import abort_if_does_not_found


# Article
# Shows all articles that contain a keyword
class Article(Resource):

    def get(self, keyword):

        output_get = query(keyword=keyword)

        if output_get.shape[0] == 0:
            return abort_if_does_not_found(keyword)
        
        return output_get.to_dict()
