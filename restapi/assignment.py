import requests
import json
# http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow
url="http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow"
simple={"name":"miss" , "title":"hello" ,"complete":True}

response=requests.get(url)
print(response.json())

print()
response=requests.post(url , json=simple)
print(response)
print()
print(response.json())