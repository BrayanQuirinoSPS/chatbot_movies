from elasticsearch import Elasticsearch
import json
import requests
from . import queries

class Connection:
    def __init__(self):
        self.CHATBOT_MOVIES='chatbot_movies'
        self.elastic_client = Elasticsearch()
    def get_movie_by_title(self,movie):
        search_param=queries.GET_MOVIE_BY_TITLE
        search_param['query']['match']['original_title']=movie
        #print(search_param)
        return self.elastic_client.search(index=self.CHATBOT_MOVIES, body=search_param)['hits']['hits']
    def get_movie_by_overview(self,overview):
        search_param=queries.GET_MOVIE_BY_OVERVIEW
        search_param['query']['match']['overview']=overview
        #print(search_param)
        return self.elastic_client.search(index=self.CHATBOT_MOVIES, body=search_param)['hits']['hits']

    def get_movie_by_score(self,score):
        search_param=queries.GET_MOVIE_BY_SCORE
        search_param['query']['range']['vote_average']['lte']=score
        return self.elastic_client.search(index=self.CHATBOT_MOVIES, body=search_param)['hits']['hits']

    def get_movie_by_runtime(self,runtime):
        search_param=queries.GET_MOVIE_BY_RUNTIME
        search_param['query']['range']['runtime']['lte']=runtime
        return self.elastic_client.search(index=self.CHATBOT_MOVIES, body=search_param)['hits']['hits']

    def get_recommendation(self):
        search_param=queries.GET_RECOMMENDATION
        return self.elastic_client.search(index=self.CHATBOT_MOVIES, body=search_param)['hits']['hits']

    def close_connection(self):
        self.elastic_client.close()
