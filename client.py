#!/usr/bin/env python3
import socket
from time import sleep
from Board import Board  # our test object
import pickle
import struct
import sys

HOST = "127.0.0.1"
PORT = 20001


def send_msg(sock, msg):
    # Prefix each message with a 4-byte length (network byte order)
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)


def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return recvall(sock, msglen)


def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data


board = Board()  # our 100x100 matrix test data
board.make_board()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # after it connects, send data to server, print size in bytes
    # and print what it received also, size in bytes
    count = 1
    while True:
        packet = pickle.dumps(board)
        print("bytes sent:", sys.getsizeof(packet))
        send_msg(s, packet)
        data = recv_msg(s)
        print("bytes received", sys.getsizeof(data))
        print(pickle.loads(data))  # or print actual matrix
        print("count:", count)
        count += 1
        sleep(5)
