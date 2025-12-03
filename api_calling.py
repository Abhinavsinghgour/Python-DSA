# print pthon url format output in json format
# here in dictionary we are searching results keyword then in result dictionary tracName keyword which will print the assigned value
# request package is to call the api
# sys : because we are using command line argument

import requests
import json
import sys


response=requests.get(f"https://itunes.apple.com/search?entity=song&limit={sys.argv[2]}&term={sys.argv[1]}")
o=response.json()
for result in o["results"]:
    print(result["trackName"])
