

import http.client
import json

conn = http.client.HTTPSConnection("reqres.in")
payload = ''
headers = {}
conn.request("GET", "/api/users", payload, headers)
res = conn.getresponse()
data = res.read()
result = data.decode("utf-8")
result_dic = json.loads(result)

registered_emails = []

for x in result_dic["data"]:
    registered_emails.append(x["email"])

content = ""

for x in registered_emails:
    content = content + x.strip() + "\n"

email_file = open("emails.txt", "w")
email_file.write(content)
email_file.close()
