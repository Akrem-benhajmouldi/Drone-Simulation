#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
#import roslib; roslib.load_manifest('teleop_twist_keyboard')
import sys, select, termios, tty
import curses
empty=Empty()
screen=curses.initscr()
curses.noecho()
#curses.cbreak()
screen.keypad(True)

def publishMethod():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1) 
    pub1 = rospy.Publisher('/drone/takeoff', Empty,queue_size=1) 
    pub2 = rospy.Publisher('/drone/land', Empty,queue_size=1) 
    rospy.init_node('publish_node', anonymous=True) # defining the ros node - publish node 
    rate = rospy.Rate(10) # 10hz # fequency at which the publishing occurs
    twist = Twist()
    k=0.8
    while not rospy.is_shutdown():
        char=screen.getch()
        if (char==ord("t")):
            pub1.publish(empty)
            rospy.loginfo("the drone is flying ")
            rate.sleep()
        elif (char==ord("l")):
            pub2.publish(empty)
            rospy.loginfo("the drone is landed ")
            rate.sleep()
        elif (char==curses.KEY_UP):
            twist.linear.z=k
            pub.publish(twist)
            rate.sleep()
        elif (char==curses.KEY_DOWN):
            twist.linear.z=-k
            pub.publish(twist)
            rate.sleep()
        elif (char==ord(' ')):
            twist.linear.x = 1e-16; twist.linear.y = 1e-16; twist.linear.z = -0.048
            twist.angular.x = 1e-16; twist.angular.y = 1e-16; twist.angular.z = 1e-16
            pub.publish(twist)
            rate.sleep() 
        elif (char==curses.KEY_LEFT):
            twist.angular.z=0.2
            pub.publish(twist)
            rate.sleep()
        elif (char==curses.KEY_RIGHT):
            twist.angular.z=-0.2
            pub.publish(twist)
            rate.sleep()
        elif (char==ord('q')):
            twist.linear.x=-k
            pub.publish(twist)
            rate.sleep()
        elif (char==ord('d')):
            twist.linear.x=k
            pub.publish(twist)
            rate.sleep()
        elif (char==ord('z')):
            twist.linear.y=k
            pub.publish(twist)
            rate.sleep()
        elif (char==ord('s')):
            twist.linear.y=-k
            pub.publish(twist)
            rate.sleep()   
    #curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    curses.endwin()
if __name__ == '__main__':
    try:
        publishMethod()
    except rospy.ROSInterruptException: 
        pass
