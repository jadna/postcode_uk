 
from fastapi import FastAPI
import uvicorn
import postcode
import requests


# http://127.0.0.1:8000/docs

description = """
Postcode UK . 🚀

Write a library that supports validating and formatting post codes for UK.
The details of which post codes are valid and which are the parts they consist of can be found at
https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting.

"""

app = FastAPI(
    title="Postcode UK",
    description=description,
    version="0.0.1",
    contact={
        "name": "Jadna Almeida",
        "github": "http://ubiq.hp.com/contact/",
        "email": "jadna.ac@gmail.com",
    })


responses = {
    200: {
        "description": "This request was successful."
    },
    500: {
        "description": "500 Internal Server Error."
    },
    400:{
        "description": "Bad request."
    },
    404:{
        "description": "Not found."
    }
}

# http://127.0.0.1:8000/formatted/details/B33 208TH
@app.get("/postcode/formatted/{code}", responses=responses)
async def postcode_formatted(code: str):
    result = postcode.format_code(code)
    return {"Postcode formatted": result}

# http://127.0.0.1:8000/valid/details/B33 208TH
@app.get("/postcode/valid/{code}", responses=responses)
async def postcode_valid(code: str):
    result = postcode.is_postcode_valid(code)
    print(result)
    if result:
        return {"The postcode ": code + " is valid!"}
    else: 
        return {"The postcode ": code + " is not valid!"}

# http://127.0.0.1:8000/postcode/details/B33 208TH
@app.get("/postcode/details/{code}", responses=responses)
async def show_details(code: str):

    response = requests.get(f"https://api.postcodes.io/postcodes/{code}")
    return response.json()



if __name__ == "__main__":

    uvicorn.run("postcode_api:app", host='127.0.0.1', port=8000, debug=True, reload=True)
