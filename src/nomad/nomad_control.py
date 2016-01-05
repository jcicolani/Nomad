#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

def joyCommand(data):
	t = Twist()
	t.linear.x = data.axes[1]
	t.angular.z = data.axes[0]

	pub.publish(t)

def start():
	global pub
	pub = rospy.Publisher('cmd_vel', Twist,queue_size=10)
	rospy.Subscriber("joy", Joy, joyCommand)

	rospy.init_node('nomad_control')
	rospy.spin()

if __name__ == '__main__':
	start()
