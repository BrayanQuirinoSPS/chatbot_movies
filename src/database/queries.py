#Archivo de las queries como DICS
GET_MOVIE_BY_TITLE= {
    "query": {
        "match": {
            "original_title": ""
        }
    },
    "sort": [
      {
        "runtime": {
          "order": "desc"
        }
      }
    ], 
    "size": 10000
}
GET_MOVIE_BY_OVERVIEW={
    "query": {
        "match": {
            "overview": ""
        }
    },
    "sort": [
      {
        "runtime": {
          "order": "desc"
        }
      }
    ], 
    "size": 10000
}
GET_MOVIE_BY_SCORE={
    "query": {
        "range": {
          "vote_average": {
            "lte": 0
            }
        }
    },
    "sort": [
      {
        "vote_average": {
          "order": "desc"
        }
      }
    ], 
    "size": 10000
}
GET_MOVIE_BY_RUNTIME={
    "query": {
        "range": {
          "runtime": {
            "lte": 0
            }
        }
    },
    "sort": [
      {
        "runtime": {
          "order": "desc"
        }
      }
    ], 
    "size": 10000
}
GET_RECOMMENDATION={
  "query": {
    "function_score": {
      "query": {
        "match_all": {}
      },
      "functions": [
        {
          "random_score": {}
        }
      ]
    }
  },
  "size": 1
}
