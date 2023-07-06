#!/usr/bin/env python

import rospy
from process.NativeTrajectoryClient import TrajectoryClient
from math import pi, radians
from std_msgs.msg import Bool
from std_srvs.srv import Trigger
import socket

from std_srvs.srv import Trigger

class NativeMoveTest():

    def __init__(self):
        rospy.init_node("socket_gateway")
        print("Launch node ?")

        rospy.wait_for_service('point_front')

        HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
        PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((HOST, PORT))
        self.sock.listen()
        self.conn, self.addr = self.sock.accept()

        with self.conn:
            print(f"Connected by {addr}")
            while True:
                data = self.conn.recv(1024)
                if not data:
                    break
                self.conn.sendall(data)

        
    def call_point_front(self):

        try:
            point_front = rospy.ServiceProxy('point_front', Trigger)
            resp1 = point_front()
            return resp1.success
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)                