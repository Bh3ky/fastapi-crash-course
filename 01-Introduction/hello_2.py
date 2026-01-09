from fastapi import FastAPI

app = FastAPI()

# `{who}` tells FastAPI to expect a variable named `who`
# at that position in the URL. it then assigns it to the
# `who` argument in the following `greet()` function
# shows coordination between the path decorator and
# path function.
@app.get("/hi/{who}")
def greet(who):
    return f"Hello? {who}?"