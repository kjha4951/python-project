import requests
import json

reurl="https://api.coindesk.com/v1/bpi/currentprice.json"

simple={"name":"api","id":7 , "complete": True}

response=requests.get(reurl)
print(response.json())

# https://catfact.ninja/fact

print()
ul="https://reqres.in/api/users"
push={"name":"komal","location":"kanpur"}
response=requests.post(ul, push)
print( response)
print( response.json())



ul="https://reqres.in/api/users/5"
put1={"name":"renu"}
response=requests.put(ul, put1)
print(response.json())


# 403- Forbidden = you don't have permission to access this server
# 503-  service unavailable
# 301-  move permanently


# Statelessness helps in scaling the APIs to millions of concurrent users by deploying it to multiple 
# servers. Any server can handle any request because there is no session related dependency.