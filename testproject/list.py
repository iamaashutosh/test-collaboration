import requests

endpoint = "http://localhost:8000/test_api/"

get_response = requests.get(endpoint)#,json={"name":"Student1","email":"aa@aa.com"})

print(get_response.json())