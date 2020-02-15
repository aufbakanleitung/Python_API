# https://docs.thecatapi.com/
import requests
import json

api_url = "https://api.thecatapi.com/v1/images/search?breed_id=beng"

headers = {"Accept": "application/json"}
response = requests.get(api_url)

print("code:\n" + str(response.status_code))
print("\n==================\n")
print("headers:\n" + str(response.headers))
print("\n==================\n")
print("content:\n" + str(response.text))
print("\n==================\n")

print("pretty content:\n" + json.dumps(json.loads(response.text), indent=2))


# Assignment:
# Please print only the name, description, and temperament of the Bengal cat
print("Characteristics of the Bengal cat:\n")
cat_dict = json.loads(response.text)


print("Name: \t\t\t" + cat_dict[0]["breeds"][0]["name"])
print("Description: \t" + cat_dict[0]["breeds"][0]["description"])
print("Temperament: \t" + cat_dict[0]["breeds"][0]["temperament"])


# Extra credit:
# Please print the names of all the cats in the database
print("\n===============\nList of cat breeds:\n")
api_url_breeds = "https://api.thecatapi.com/v1/breeds"

response_breeds = requests.get(api_url_breeds)
breeds_dict = json.loads(response_breeds.text)

print()
for breeds in breeds_dict:
    print(breeds.get("name"))









#
# for breed in breeds_dict:
#     print(breed.get("name"))
