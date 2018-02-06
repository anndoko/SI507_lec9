from requests_oauthlib import OAuth1Session
import secrets2
import json

client_key = secrets2.client_key
client_secret = secrets2.client_secret

resource_owner_key = secrets2.access_token
resource_owner_secret = secrets2.access_token_secret

protected_url = "https://api.twitter.com/1.1/account/settings.json"

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = "https://api.twitter.com/1.1/search/tweets.json"
params = {"q" : "food"}
r = oauth.get(protected_url, params = params)
r_dic = json.loads(r.text)

for r in r_dic["statuses"]:
    print(r["user"]["name"])
    print(r["text"])
    print("----------")
