import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json = body, headers = data.headers)

def post_new_kits(body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, json = body, headers = data.kit_headers)

response = post_new_kits(data.kit_body)
print(response.json())