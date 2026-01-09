from fastapi import FastAPI

app = FastAPI() # app is an FastAPI object which represents the whole web application.

@app.get("/hi") # path decorator which tells FastAPI the following:
# request for the URL "/hi" on this server should be directed to 
# the function below 
# the decorator applies only to the HTTP `GET` verb.
def greet(): # path function (main point of contact with HTTP requests and responses)
    return "Hello? World?"