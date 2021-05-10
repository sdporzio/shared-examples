import requests
import json

db_url = "http://130.92.128.162"
db_port = "8086"
db_name = "slowcontrol"

fullUrl = f"{db_url}:{db_port}/write?db={db_name}"
post = "timedelta value=0.6"

print(fullUrl,post)

r = requests.post(fullUrl, data=post)