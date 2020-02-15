# https://docs.thecatapi.com/
import requests
import json

api_url = "http://localhost:8080"
headers = {"Accept": "application/json"}
response = requests.get(api_url, headers=headers)

# -= Assignment =-
# Access your own http server and print status code, headers, pretty print text
print("code:\n")
print("\n==================\n")
print("headers:\n")
print("\n==================\n")
print("pretty content:\n")

post_response = requests.post(api_url, {"bootcamp": "rocks"})
print(post_response.text)
