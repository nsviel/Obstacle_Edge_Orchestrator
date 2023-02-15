#---------------------------------------------
from src.param import param_hu

import socket


def send_packet_add(ip, port, packet):
    if(packet != None and param_hu.sock_client_ok):
        param_hu.sock_client.sendto(packet, (ip, port))

def network_info(dest, lidar):
    if(dest == "co"):
        ip = param_hu.state_hu["controlium"]["ip"]
        if(lidar == "l1"):
            port = param_hu.state_hu["controlium"]["sock_server_l1_port"]
        if(lidar == "l2"):
            port = param_hu.state_hu["controlium"]["sock_server_l2_port"]
    elif(dest == "ve"):
        ip = param_hu.state_hu["velodium"]["ip"]
        port = param_hu.state_hu["velodium"]["sock_server_port"]

    return [ip, port]