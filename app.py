from flask import Flask
from flask_restful import reqparse, Api
from api.classes.AllArticles import AllArticles
from api.classes.Article import Article

from crawler.steps.raw_urls import raw_urls
from crawler.steps.find_trash_list import find_trash_list
from crawler.steps.remove_items import remove_items
from crawler.steps.crawl_all_pages import crawl_all_pages
from crawler.steps.upload_to_BigQuery import upload_to_BigQuery



app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

## Setup the Api resource routing
api.add_resource(AllArticles, '/AllArticles')
api.add_resource(Article, '/Article/<keyword>')


if __name__ == '__main__':
    
    # Getting raw URLs from main page
    raw_urls = raw_urls()
    
    # Filtering only URL that contain `/news/`
    trash_list = find_trash_list(raw_urls)
    urls = remove_items(raw_urls, trash_list)

    # Crawling all pages
    data = crawl_all_pages(urls)

    # Upload to BigQuery
    upload_to_BigQuery(data)

    app.run(debug=True)