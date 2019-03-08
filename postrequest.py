import requests

url = "http://localhost:7990/rest/api/1.0/projects"

payload = "{\r\n    \"key\": \"jh789789\",\r\n    \"name\": \"fgh789\",\r\n    \"description\": \"The description for my cool project.\"\r\n   \r\n}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic RW1zYWw6RWMxMjM0",
    'cache-control': "no-cache",
    'Postman-Token': "f571df5e-55bf-4e1a-b653-907fac2f9816"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)