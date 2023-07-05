#!/usr/bin/env python

import rospy
from process.NativeTrajectoryClient import TrajectoryClient
from math import pi, radians
from std_msgs.msg import Bool
from std_srvs.srv import Trigger

class NativeMoveTest():

    def __init__(self):
        print("Launch node ?")
        rospy.init_node("NativeMoveTest")
        s = rospy.Service('point_front', Trigger, self.point_front)
        print("Node Init")
        self.TC = TrajectoryClient()
        print("TC Init")
        self.TC.joint_trajectory_controller = self.TC.JOINT_TRAJECTORY_CONTROLLERS[0]
        print("Controller selected")
        rospy.spin()

    def point_front(self, req):

        position_list = [[radians(87), radians(-97), radians(159), radians(-51), radians(-180), radians(45) ]]
        #position_list = [[radians(86), radians(-97), radians(140), radians(-45), radians(-258), radians(-0.4) ]]
        #position_list = [[radians(63), radians(-97), radians(139), radians(-45), radians(-298), radians(-0.2) ]]
        duration_list = [1]      
        
        self.TC.send_joint_trajectory(position_list, duration_list)
       
        position_list = [[radians(63), radians(-97), radians(139), radians(-45), radians(-298), radians(-0.2) ]]
        position_list = [[radians(52.1), radians(-99.6), radians(151), radians(-47.5), radians(-309.6), radians(-4) ]]
        duration_list = [4]   

        rospy.sleep(3)   
        
        self.TC.send_joint_trajectory(position_list, duration_list)
        position_list = [[radians(87), radians(-97), radians(159), radians(-51), radians(-180), radians(45) ]]
        duration_list = [2]      
        
        self.TC.send_joint_trajectory(position_list, duration_list)
                     
        print("Traj done")
        

    def test(self):
        print("fin")


if __name__ == "__main__":
    NMT = NativeMoveTest()
    NMT.test()


