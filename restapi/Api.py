import requests
import json
# http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow
url="http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow"
response=requests.get(url)
for data in response.json()["items"]:
    if data["answer_count"]==0:

      print(data["title"])
      print(data["link"])
      print()
    else:
       print("skipped ")
    print()


