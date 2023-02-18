import requests
from datetime import datetime
import os


USERNAME=os.environ.get("PIXELA_USERNAME")
TOKEN=os.environ.get("PIXELA_TOKEN")
pixela_endpoint=os.environ.get("PIXELA_ENDPOINT")

headers = {
    "X-USER-TOKEN": TOKEN
}

graphs = {}
graphs_list = []


def create_user(token,username,agreement,is_minor,endpoint):
    user_params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": agreement,
        "notMinor": is_minor,
    }
    user_endpoint = f"{endpoint}/users"
    response = requests.post(url=user_endpoint,json=user_params)
    print(response.text)


def create_graph(id,name,unit,type,color,username,header):
    graph_config = {
        "id": id,
        "name": name,
        "unit": unit,
        "type": type,
        "color": color
    }
    graph_endpoint = f"{pixela_endpoint}/users/{username}/graphs"
    graph_res = requests.post(url=graph_endpoint,json=graph_config, headers=header)
    graphs[graph_config['id']] = graph_config
    graphs_list.append(graphs)
    print(graph_res)
    return graphs


def add_pixel(graph_id,date,quantity,header):
    add_data_graph_endpoint = f"{pixela_endpoint}/users/{USERNAME}/graphs/{graph_id}"
    data = {
        "date": date,
        "quantity": quantity
    }
    graph_res = requests.post(url=add_data_graph_endpoint, json=data, headers=header)
    print(graph_res)


def update_pixel(graph_id,date,header):
    update_data_graph_endpoint = f"{pixela_endpoint}/users/{USERNAME}/graphs/{graph_id}/{date}"
    data = {
        "date": date,
    }
    graph_res = requests.put(url=update_data_graph_endpoint, json=data, headers=header)
    print(graph_res)


def delete_pixel(graph_id,date,header):
    update_data_graph_endpoint = f"{pixela_endpoint}/users/{USERNAME}/graphs/{graph_id}/{date}"
    graph_res = requests.put(url=update_data_graph_endpoint, headers=header)
    print(graph_res)


# running_graph = create_graph("running","Running","Km","float","momiji",USERNAME,headers)
now = datetime.today()
current_date = now.strftime("%Y%m%d")

add_pixel("running",current_date,"5",headers)



