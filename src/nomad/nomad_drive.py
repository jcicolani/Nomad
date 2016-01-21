#!/usr/bin/env python

import roboclaw
import rospy
from geometry_msgs.msg import Twist
from nomad.srv import RoboclawDiagnostics, RoboclawDiagnosticsResponse


roboclaw.Open("/dev/ttyACM0",115200)

def drive_wheels(msg):
	t = msg
	x = t.linear.x
	z = t.angular.z

	r = (x-z)/2
	l = (x+z)/2

	m2 = (l * 64) + 64
	m1 = (r * 64) + 64

	print str(m1) + " " + str(m2)
	roboclaw.ForwardM1(0x80, int(m1))
	roboclaw.ForwardM2(0x80, int(m2))

def get_diag_info(input_string):
	command = input_string.input
	print command
	
	commandList = command.split(",")
	print len(commandList)

	returnmessage = "diagnostics info:\n"

	for command in commandList:
		print command

		if(command == "firmware" or command == "all"): 
			print "firmware"
			status = roboclaw.ReadVersion(0x80)

			if status[0]==False:
				print "Command Failed"
			else:
				print repr(status[1])

			returnmessage += "Firmware:" + repr(status[1]) + "\n"

		if(command == "mainbat" or command == "all"): 
			print "mainbat"
			status = roboclaw.ReadMainBatteryVoltage(0x80)

			if status[0]==False:
				print "Command Failed"
			else:
				print repr(status[1])

			returnmessage += "Main Batt:" + repr(status[1]) + "\n"

		if(command == "mainbatsettings" or command == "all"): 
			print "mainbatsettings"
			status = roboclaw.ReadMinMaxMainVoltages(0x80)

			if status[0]==False:
				print "Command Failed"
			else:
				print repr(status[1])

			returnmessage += "Main Batt Min:" + repr(status[1]) + "  Max:" + repr(status[2]) + "\n"

		if(command == "logicbat" or command == "all"): 
			print "logicbat"
			status = roboclaw.ReadLogicBatteryVoltage(0x80)

			if status[0]==False:
				print "Command Failed"
			else:
				print repr(status[1])

			returnmessage += "Logic Batt:" + repr(status[1]) + "\n"

		if(command == "temp" or command == "all"): 
			print "temp"
			status = roboclaw.ReadTemp(0x80)

			if status[0]==False:
				print "Command Failed"
			else:
				print repr(status[1])

			returnmessage += "Temp:" + repr(status[1]) + "\n"

		if(command == "config" or command == "all"): 
			print "config"
			status = roboclaw.GetConfig(0x80)

			if status[0]==False:
				print "Command Failed"
			else:
				print repr(status[1])

			returnmessage += "Config:" + repr(status[1]) + "\n"

		if(command == "error" or command == "all"): 
			print "error"
			status = roboclaw.ReadError(0x80)

			if status[0]==False:
				print "Command Failed"
			else:
				print repr(status[1])

			returnmessage += "Error Code:" + repr(status[1]) + "\n"

	return returnmessage


rospy.init_node('barb_drive')
sub = rospy.Subscriber('cmd_vel', Twist, drive_wheels)
service = rospy.Service('RoboclawDiagnostics', RoboclawDiagnostics, get_diag_info)

rospy.spin()
