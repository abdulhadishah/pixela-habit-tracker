import requests
from datetime import datetime
import os

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_USERNAME = os.environ.get("PIXELA_USERNAME")
GRAPH_ID = "graph1"

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

"""
# CHECK 
# response = requests.post(PIXELA_ENDPOINT, json=user_params)
# print(response.text)
"""

graph_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"

# WHAT TO TRACK
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hr",
    "type": "float",
    "color": "ajisai",
}

headers ={
    "X-USER-TOKEN": PIXELA_TOKEN,
}

"""
# CHECK
# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
"""

# YOUR ENDPOINT
pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today?\n>>> "),
}

response = requests.post(pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)


"""
# TO UPDATE PIXELA DATA
# yesterday = datetime(2025, 9, 24)
#
# pixel_update_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime("%Y%m%d")}"
#
# pixel_update_data ={
#     "quantity": "2"
# }

# update = requests.put(pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print(update.text)
"""

"""
# TO DELETE PIXELA DATA
# delete = requests.delete(pixel_update_endpoint, headers=headers)
# print(delete.text)
"""
