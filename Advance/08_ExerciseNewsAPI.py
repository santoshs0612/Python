# #Use NewsAPI and the requests module to fetch the default topics.
# Go to https://newsapi.org/ and explore the various options to build your applications 


# #Use NewsAPI and the requests module to fetch the default topics.
# Go to https://newsapi.org/ and explore the various options to build your applications 

import requests


def newsAPI():
  print("Welcome to World news here are some us news !")
  while True:
    print("Choose your sections")
    print(" 1. Business 2. Entertainment 3. General\n 4. Health 5. Science 6. Sports 7. Technology 8. Exit")
    val = input()
    if(val== "8"): break
    dictNews = {"1":"business", "2": "entertainment","3":"general", "4":"health", "5":"science","6":"sports","7":"technology"}
                

    # url = 'https://newsapi.org/v2/everything?'

    url= 'https://newsapi.org/v2/top-headlines?'
    secret = "025dbf54d9b54402be68c137a27a282a"
    category = dictNews[val]


    # Specify the query and number of returns
    parameters = {
        "sortBy": "top",
        "category": category,
        'country':'us',
        'pageSize': 10,  # maximum is 100
        'apiKey': secret # your own API key
    }

    # a ="https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=025dbf54d9b54402be68c137a27a282a"
    response = requests.get(url, params=parameters)
    # response = requests.get(a)

    # Convert the response to JSON format and pretty print it

    response_json = response.json()
    # print(response_json)
    article = response_json["articles"]

    results = []
      
    for ar in article:
        results.append(ar["title"])
          
    for i in range(len(results)):
          
        # printing all trending news
        print(i + 1, results[i])


        

newsAPI()