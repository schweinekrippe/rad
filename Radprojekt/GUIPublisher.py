#! /usr/bin/env python2
from __future__ import print_function

import rospy
from communication.msg import controller


import numpy as np
import cv2
from time import clock

#pub = rospy.Publisher('GUIData', String, queue_size=10)
pub = rospy.Publisher('GUIData', controller, queue_size=10)

def talker(vel_ang_values):
    global pub
    print('publishing msg')
    rate = rospy.Rate(10)
    
    msg = controller()
    msg.velocity_angle = vel_ang_values
    
    
    #msg= str(vel_ang_values)
    #print(vel_ang_values)
    #print("Sending values: " + msg)
    
    rospy.loginfo(msg)
    pub.publish(msg)


class Sender:
    
    velocity_angle = []

    
    def __init__(self):
        try:

            #rospy.init_node('GUIPublisher', anonymous=True)
        
            print("Publisher started")

        except rospy.ROSInterruptException:
            print("fuck this")
            

    def setTargets(self, TargetAngle):
        
        velocity_angle = TargetAngle
        
        talker(velocity_angle)
    
    def stop(self):
		pass


#def main():
#    try:
#
#        rospy.init_node('GUIPublisher', anonymous=True)
#        
#        print("Publisher started")

#    except rospy.ROSInterruptException:
#        pass

#if __name__ == '__main__':
#    main()
