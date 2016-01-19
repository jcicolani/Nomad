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

def get_diag_info(input_string):
	command = input_string.input
	print command
	
	commandList = command.split(",")
	print len(commandList)

	returnmessage = "diagnostics info:"

	for command in commandList:
		print command

		if(command == "firmware" or command == "all"): 
			print "firmware"
			#status = roboclaw.ReadVersion()
			status = [True, "firmware"]

			if status[0]==False:
				print "Command Failed"
			else:
				print repr(status[1])

			returnmessage += status[1] + ";"

		if(command == "mainbat" or command == "all"): 
			print "mainbat"
			#status = roboclaw.ReadMainBattery()
			status = [True, "mainbat"]

			if status[0]==False:
				print "Command Failed"
			else:
				print repr(status[1])

			returnmessage += status[1] + ";"

		if(command == "logicbat" or command == "all"): 
			print "logicbat"
			#status = roboclaw.ReadLogicBattery()
			status = [True, "logicbat"]

			if status[0]==False:
				print "Command Failed"
			else:
				print repr(status[1])

			returnmessage += status[1] + ";"

		if(command == "temp" or command == "all"): 
			print "temp"
			#status = roboclaw.ReadTemperature()
			status = [True, "temp"]

			if status[0]==False:
				print "Command Failed"
			else:
				print repr(status[1])

			returnmessage += status[1] + ";"

		if(command == "status" or command == "all"): 
			print "status"
			#status = roboclaw.ReadStatus()
			status = [True, "status"]

			if status[0]==False:
				print "Command Failed"
			else:
				print repr(status[1])

			returnmessage += status[1] + ";"

		if(command == "config" or command == "all"): 
			print "config"
			#status = roboclaw.ReadConfig()
			status = [True, "config"]

			if status[0]==False:
				print "Command Failed"
			else:
				print repr(status[1])

			returnmessage += status[1] + ";"

		if(command == "error" or command == "all"): 
			print "error"
			#status = roboclaw.ReadError(0x80)
			status = [True, "error"]

			if status[0]==False:
				print "Command Failed"
			else:
				print repr(status[1])

			returnmessage += status[1] + ";"

	return returnmessage


rospy.init_node('barb_drive')
sub = rospy.Subscriber('cmd_vel', Twist, drive_wheels)
service = rospy.Service('RoboclawDiagnostics', RoboclawDiagnostics, get_diag_info)

rospy.spin()
