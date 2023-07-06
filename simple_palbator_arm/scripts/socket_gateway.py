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
        rospy.loginfo("Launch node ?")

        rospy.wait_for_service('point_front')

        HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
        PORT = 10155        # Port to listen on (non-privileged ports are > 1023)

        self.nok_response = "nok".encode()
        self.ok_response = "ok".encode()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((HOST, PORT))
        self.sock.listen()

        self.conn, self.addr = self.sock.accept()

        with self.conn:
            print(f"Connected by {self.addr}")
            while not rospy.is_shutdown():
                data = self.conn.recv(1024)
                if not data: break
                if int(data) == 1:
                    self.call_point_front()
                elif int(data) == 2:
                    self.call_raw_grasp()
                elif int(data) == 3:
                    self.call_human_grasp()
        self.sock.close()


    def call_point_front(self):

        try:
            point_front = rospy.ServiceProxy('point_front', Trigger)
            resp1 = point_front()
            print("1")
            self.conn.sendall(self.ok_response)
            return resp1.success
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)      
            self.conn.sendall(self.nok_response)

    def call_raw_grasp(self):

        try:
            raw_grasp = rospy.ServiceProxy('raw_grasp', Trigger)
            resp1 = raw_grasp()
            print("2")
            self.conn.sendall(self.ok_response)
            return resp1.success
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)   
            self.conn.sendall(self.nok_response)   

    def call_human_grasp(self):

        try:
            human_grasp = rospy.ServiceProxy('human_grasp', Trigger)
            resp1 = human_grasp()
            print("3")
            self.conn.sendall(self.ok_response)
            return resp1.success
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)   

            self.conn.sendall(self.nok_response)             


if __name__ == "__main__":
    NativeMoveTest()