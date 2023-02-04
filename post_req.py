import http.client
import json

def call_registration(email):
    conn = http.client.HTTPSConnection("reqres.in")
    payload = json.dumps({
    "email": email,
    "password": "pistol"
    })
    headers = {
    'Content-Type': 'application/json'
    }
    conn.request("POST", "/api/register", payload, headers)
    res = conn.getresponse()
    data = res.read()
    result = data.decode("utf-8")
    p = json.loads(result)
    return p["token"]

email_file = open("emails.txt", "r")
data = email_file.readlines()
email_file.close()

print(data)

token_details = ["email,registration_token"]
response = ""

for x in data:
    print(call_registration(x.strip()))
    response = x.strip() + "," + str(call_registration(x.strip()))
    token_details.append(str(response))

csv_content = ""
for x in token_details:
    csv_content = csv_content + x + "\n"

csv_sheet = open("email_token_details.csv", "w")
csv_sheet.write(csv_content)
csv_sheet.close()