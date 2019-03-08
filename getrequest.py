import requests


url = "http://localhost:8080/rest/api/2/project"

payload = ""
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic ZW1zYWxjZW5naXo6RWMxMjM0",
    'cache-control': "no-cache",
    'Postman-Token': "82bced95-994d-4d93-b9da-ac86050cfcb8"
}

response = requests.request("GET", url, data=payload, headers=headers)
data = response.json()
jira_names = []
for object in data:
    jira_names.append(object['name'])

print(jira_names)
print(response.status_code)
