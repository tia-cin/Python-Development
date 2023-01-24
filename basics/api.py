# cmd -> pip install requests
import requests
import json

# request to API
res = requests.get('https://api.tomitokko.repl.co/')

# print status code of request
print(res.status_code)

# pass json response
json.loads(res.text)

for data in res.text:
    print(data) # prints each character