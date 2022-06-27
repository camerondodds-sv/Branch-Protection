import requests 
url = "https://api.github.com/repos/camerondodds-sv/Branch-Protection/branches"
token = "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"
print("token {}".format(token))
headers = {"Authorization" : "token {}".format(token)} 
response = requests.get(url, headers=headers)
 
print(response.json())