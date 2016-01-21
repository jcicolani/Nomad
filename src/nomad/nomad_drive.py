#!/usr/bin/env python

import roboclaw
import rospy
from geometry_msgs.msg import Twist
from nomad.srv import RoboclawDiagnostics, RoboclawDiagnosticsResponse


roboclaw.Open("/dev/ttyACM0",115200)

def drive_wheels(msg):
	x = msg.linear.x
	z = msg.angular.z

	#127 is max speed
	m1 = int((x-z)*127)
	m2 = int((x+z)*127)

	print str(m1) + " " + str(m2)		
	
	if m1 > 0:
		roboclaw.ForwardM1(0x80, m1)
	else: 
		roboclaw.BackwardM1(0x80, m1)

	if m2 > 0:
		roboclaw.ForwardM2(0x80, m2)
	else: 
		roboclaw.BackwardM2(0x80, m2)


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


status = roboclaw.SetMainVoltages(0x80, 0x64, 0xa0)
if status==False:
	print "SetMainVoltages Failed"
else:
	print "SetMainVoltages Success"


rospy.init_node('barb_drive')
sub = rospy.Subscriber('cmd_vel', Twist, drive_wheels)
service = rospy.Service('RoboclawDiagnostics', RoboclawDiagnostics, get_diag_info)

rospy.spin()
