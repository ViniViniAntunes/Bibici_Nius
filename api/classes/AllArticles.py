from flask_restful import Resource

from api.functions.query import query

# AllArticles
# Shows all articles
class AllArticles(Resource):
    def get(self):
        output_get = query('', all_articles=True)
        return output_get.to_dict()
