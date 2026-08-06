import requests
import datetime as dt

USERNAME = "ajaykh7"
TOKEN = "sjhgdr43iuwfb84538n"
GRAPH_ID = "graph1"
# Step1 : creating pixela user
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# respones = requests.post(url=pixela_endpoint,json=user_params)
# print(respones.text)

# Step2 :creating graph for python
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Python Code Graph",
    "unit": "Has done",
    "type": "float",
    "color": "shibafu",
}
header = {"X-USER-TOKEN": TOKEN}
# respones = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(respones.text)


# Step3 : Adding pixel to the graph
today = dt.date.today().strftime("%Y%m%d")
pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_data = {
    "date": f"{today}",
    "quantity": f"{input("How many lectures you completed in toadys python class : ")}",
}

respones = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=header)
print(respones.text)


# Step4 : Updating pixel int the graph
update_pixel_endpoint = f"{pixel_creation_endpoint}/{today}"
new_pixel_data = {
    "quantity": f"{input("Did you completed the toadys python class : ")}"
}
# respones = requests.put(url=update_pixel_endpoint,json=new_pixel_data,headers=header)
# print(respones.text)


# Step5 : Deleting the pixel from the graph
delet_endpoint = f"{pixel_creation_endpoint}/{today}"
# respones = requests.delete(url=delet_endpoint,headers=header)
# print(respones.text)

# if you want to test it go through the step 3
#this below is to add 
# endpoint = f"https://pixe.la/@ajaykh7"
# params = {"displayName": f"{USERNAME}"}
# respones = requests.put(url=endpoint, json=params, headers=header)
# print(respones.text)


#pixela profile
# https://pixe.la/@ajaykh7