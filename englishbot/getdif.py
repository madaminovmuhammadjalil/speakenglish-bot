import json
import requests
app_id  = "35a22e68"
app_key  = "65184e5e2a8155995321712891e07853"
language = "en-gb"
# word_id = "apricot"

def getdifinitions(word_id):
    respons = {}
    definitions = []
    try:
        url = "https://od-api-sandbox.oxforddictionaries.com:443/api/v2/words/" + language + "?q=" + word_id.lower()
        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
        response = r.json()
        senses = response["results"][0]["lexicalEntries"][0]["entries"][0]["senses"]
        for sense in senses:
            definitions.append(f"👉 {sense["definitions"][0]} ")
            respons["definitions"] = "\n".join(definitions)
        if response["results"][0]["lexicalEntries"][0]["entries"][0]["pronunciations"][0].get("audioFile"):
            respons["audioFile"] = response["results"][0]["lexicalEntries"][0]["entries"][0]["pronunciations"][0]["audioFile"]
        return respons
    except:
        respons["definitions"] = "bunday soz mavjud emas"
        return respons
