#!/usr/bin/env python

import rospy
from process.NativeTrajectoryClient import TrajectoryClient
from process.Gripper import Gripper
from math import pi, radians
from std_msgs.msg import Bool
from std_srvs.srv import Trigger
from geometry_msgs.msg import Vector3, Pose, Quaternion
from tf.transformations import euler_from_quaternion, quaternion_from_euler

class NativeMoveTest():

    def __init__(self):
        print("Launch node ?")
        rospy.init_node("NativeMoveTest")
        s1 = rospy.Service('point_front', Trigger, self.point_front)
        s2 = rospy.Service('raw_grasp', Trigger, self.raw_grasp)
        s3 = rospy.Service('cart_grasp', Trigger, self.cart_grasp)
        print("Node Init")

        self.Grip = Gripper() 

        self.TC = TrajectoryClient()
        print("TC Init")
        self.TC.joint_trajectory_controller = self.TC.JOINT_TRAJECTORY_CONTROLLERS[0]
        self.TC.cartesian_trajectory_controller = self.TC.CARTESIAN_TRAJECTORY_CONTROLLERS[0]
        print("Controller selected")
        rospy.spin()

    def point_front(self, req):

        position_list = [[radians(87), radians(-97), radians(159), radians(-51), radians(-180), radians(45) ]]
        duration_list = [2]      
        self.TC.send_joint_trajectory(position_list, duration_list)
       
        position_list = [[radians(52.1), radians(-99.6), radians(151), radians(-47.5), radians(-309.6), radians(-4) ]]
        duration_list = [4]   
        self.TC.send_joint_trajectory(position_list, duration_list)

        position_list = [[radians(52.1), radians(-99.6), radians(151), radians(-47.5), radians(-309.6), radians(-4) ]]
        duration_list = [1]           
        self.TC.send_joint_trajectory(position_list, duration_list)

        position_list = [[radians(87), radians(-97), radians(159), radians(-51), radians(-180), radians(45) ]]
        duration_list = [2]      
        self.TC.send_joint_trajectory(position_list, duration_list)
                     
        print("Traj done")


    def raw_grasp(self, req):

        position_list = [[radians(87), radians(-97), radians(159), radians(-51), radians(-180), radians(45) ]]
        duration_list = [2]      
        self.TC.send_joint_trajectory(position_list, duration_list)
       
        # Pregrasp 
        position_list = [[radians(73.46), radians(-69), radians(101.68), radians(-121.68), radians(-90), radians(-15.52) ]]
        duration_list = [4]   
        self.TC.send_joint_trajectory(position_list, duration_list)
        self.Grip.open()

        # Grasp 
        position_list = [[radians(75), radians(-38.3), radians(101.58), radians(-155.14), radians(-87), radians(71) ]]
        duration_list = [4]   
        self.TC.send_joint_trajectory(position_list, duration_list)      
        self.Grip.close()  

        # Travel with bag
        #position_list = [[-0.22848111787904912, -2.039434095422262, 1.6872642675982874, -1.00609643877063, 4.5479583740234375, 0.9501953125]]
        #duration_list = [5]      
        #self.TC.send_joint_trajectory(position_list, duration_list)
                     
        print("Traj done")       

    def cart_grasp(self, req):
            
        pose_list = [
            Pose(
                Vector3(0.079, -0.566, -0.074), Quaternion(*quaternion_from_euler(2.327, 2.113, -0.051) )
            ),
        ]
        duration_list = [10]  

        self.TC.send_cartesian_trajectory(pose_list, duration_list)    
        

    def test(self):
        print("fin")


if __name__ == "__main__":
    NMT = NativeMoveTest()
    NMT.test()


