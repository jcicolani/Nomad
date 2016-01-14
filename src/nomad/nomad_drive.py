#!/usr/bin/env python

import roboclaw
import rospy
from geometry_msgs.msg import Twist
from nomad.srv import RoboclawDiagnostics, RoboclawDiagnosticsResponse


#roboclaw.Open("/dev/ttyACM0",115200)

def drive_wheels(msg):
	t = msg
	x = t.linear.x
	z = t.angular.z

	r = (x-z)/2
	l = (x+z)/2

	m2 = (l * 64) + 64
	m1 = (r * 64) + 64

	print str(m1) + " " + str(m2)
	roboclaw.DriveM1(int(m1))
	roboclaw.DriveM2(int(m2))

def get_diag_info():
	status = roboclaw.ReadError(0x80)
	if status[0]==False:
		print "GETSTATUS Failed"
		return "GETSTATUS Failed"
	else:
		print repr(status[1])
		return repr(status[1])

	
rospy.init_node('barb_drive')
sub = rospy.Subscriber('cmd_vel', Twist, drive_wheels)
service = rospy.Service('RoboclawDiagnostics', RoboclawDiagnostics, get_diag_info)

rospy.spin()
