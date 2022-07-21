#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from SOCK import sock_client_fct


def connection():
    sock_client_fct.create_socket()

def send_packet(packet):
    ip = param_hu.state_hu["controlium"]["ip"]
    port = param_hu.state_hu["controlium"]["sock_server_port"]
    sock_client_fct.send_packet_add(ip, port, packet)

def test_velo_connection():
    sock_client_fct.test_velo_connection()