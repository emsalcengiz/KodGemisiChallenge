import requests
import sched, time


def get_jira_projects():
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
    jira_project_names = []
    for obj in data:
        jira_project_names.append(obj['name'])
    return jira_project_names


def get_bitbucket_projects():
    url = "http://localhost:7990/rest/api/1.0/projects"

    payload = ""
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Basic RW1zYWw6RWMxMjM0",
        'cache-control': "no-cache",
        'Postman-Token': "2b681617-f336-4b04-ac5a-41e5a8fa8766"
    }

    response = requests.request("GET", url, data=payload, headers=headers)
    data = response.json()
    bitbucket_project_names = []
    for obj in data['values']:
        bitbucket_project_names.append(obj['name'])
    return bitbucket_project_names


def post_bitbucket_projects(project_name):
    url = "http://localhost:7990/rest/api/1.0/projects"

    payload = "{\r\n\t\"key\":\"" + project_name + "\",\r\n    \"name\": \"" + project_name + "\"\r\n}"
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Basic RW1zYWw6RWMxMjM0",
        'cache-control': "no-cache",
        'Postman-Token': "f571df5e-55bf-4e1a-b653-907fac2f9816"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response


def control(scheduler):
    for jira_project in get_jira_projects():
        is_found = False
        for bitbucket_project in get_bitbucket_projects():
            if jira_project == bitbucket_project:
                is_found = True
        if is_found == False:
            post_bitbucket_projects(jira_project)
            print(jira_project," created")
    s.enter(20, 1, control, (scheduler,))


s = sched.scheduler(time.time, time.sleep)
s.enter(20, 1, control, (s,))
s.run()
