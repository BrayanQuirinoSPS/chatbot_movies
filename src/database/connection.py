from elasticsearch import Elasticsearch
import json
import requests
import queries
class Connection:
    def __init__(self):
        self.CHATBOT_MOVIES='chatbot_movies'
        self.elastic_client = Elasticsearch()
    def get_movie_by_title(movie):
        search_param=queries.GET_MOVIE_BY_TITLE
        search_param['query']['match']['origin-title']=movie
        #print(search_param)
        return self.elastic_client.search(index=self.CHATBOT_MOVIES, body=search_param)['hits']['hits']
    def get_movie_by_overview(overview):
        search_param=queries.GET_MOVIE_BY_OVERVIEW
        search_param['query']['match']['overview']=overview
        #print(search_param)
        return self.elastic_client.search(index=self.CHATBOT_MOVIES, body=search_param)['hits']['hits']
    def close_connection():
        self.elastic_client.close()
