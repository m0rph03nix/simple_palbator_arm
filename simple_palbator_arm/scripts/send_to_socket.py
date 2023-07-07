#!/usr/bin/env python

import rospy
from math import pi, radians
from std_msgs.msg import Bool
from std_srvs.srv import Trigger

import socket

class NativeMoveTest():

    def __init__(self):
        print("Launch node ?")
        rospy.init_node("NativeMoveTest")

        s1 = rospy.Service('point_front', Trigger, self.point_front)
        s2 = rospy.Service('raw_grasp', Trigger, self.raw_grasp)
        #s3 = rospy.Service('cart_grasp', Trigger, self.cart_grasp)
        s4 = rospy.Service('human_grasp', Trigger, self.human_grasp)
        s5 = rospy.Service('human_carry', Trigger, self.human_carry)
        s6 = rospy.Service('raw_drop', Trigger, self.raw_drop)        

        HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
        PORT = 10145        # Port to listen on (non-privileged ports are > 1023)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.connect((HOST,PORT))

        while not rospy.is_shutdown():
            rospy.sleep(1)
            print(self.sock.recv(1024))

        self.sock.close()
            

    def point_front(self, req):
        data = "1"
        self.sock.send(data.encode())
        print("1 done")


    def raw_grasp(self, req):
        data = "2"
        self.sock.send(data.encode())
        print("2 done")
                          
        
    def human_grasp(self, req):
        data = "3"
        self.sock.send(data.encode())
        print("3 done")

    def human_carry(self, req):
        data = "4"
        self.sock.send(data.encode())
        print("4 done")     

    def raw_drop(self, req):
        data = "5"
        self.sock.send(data.encode())
        print("5 done")           
                     


    def test(self):
        print("fin")


if __name__ == "__main__":
    NMT = NativeMoveTest()


