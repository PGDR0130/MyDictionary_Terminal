import requests
import json


# word = input("Your word: ")
word = "find"

# FreeDictionary
response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

r_json = response.json()

# print(json.dumps(r_json, indent= 4))


synonym = r_json[0]["meanings"][0]["definitions"][0]["synonyms"]
for i in synonym :
    print(i)