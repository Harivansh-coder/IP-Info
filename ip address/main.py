"""
This python script gives information about the ip address provided
it uses a free api for this
"""
import requests
from pprint import pprint

def requestData(url):
    r = requests.get(url = URL)
    data = r.json()

    return data

def apiResponse(data):
    if data['status'] == "success":
        return True
    else:
        return False

def jsonToText(data):
    for i in data:
        print(f"{i} = {data[i]}")

if __name__ == "__main__":

    URL = "http://ip-api.com/json/" # api endpoint

    ipInput = input("Enter an ip address (press enter to use your ip address): ")

    URL += ipInput # final query for the api

    data = requestData(URL) #getting the data
    responseRecived = apiResponse(data) #getting response

    #pprint(data)

    if responseRecived:
        jsonToText(data)
    else:
        raise("IP incorrect")
        




    
