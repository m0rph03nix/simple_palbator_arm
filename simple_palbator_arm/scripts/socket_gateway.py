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
        PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((HOST, PORT))
        self.sock.listen()
        self.conn, self.addr = self.sock.accept()

        with self.conn:
            print(f"Connected by {self.addr}")
            while True:
                data = self.conn.recv(1024)
                if data == 1:
                    self.call_point_front()
                elif data == 2:
                    self.call_raw_grasp()
                elif data == 3:
                    self.call_human_grasp()
                self.conn.sendall(data)

        
    def call_point_front(self):

        try:
            point_front = rospy.ServiceProxy('point_front', Trigger)
            resp1 = point_front()
            return resp1.success
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)      

    def call_raw_grasp(self):

        try:
            raw_grasp = rospy.ServiceProxy('raw_grasp', Trigger)
            resp1 = raw_grasp()
            return resp1.success
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)      

    def call_human_grasp(self):

        try:
            human_grasp = rospy.ServiceProxy('human_grasp', Trigger)
            resp1 = human_grasp()
            return resp1.success
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)                


if __name__ == "__main__":
    NativeMoveTest()