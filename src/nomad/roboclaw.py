import serial
import struct
import time

#Command Enums

class Cmd():
	M1FORWARD = 0
	M1BACKWARD = 1
	SETMINMB = 2
	SETMAXMB = 3
	M2FORWARD = 4
	M2BACKWARD = 5
	M17BIT = 6
	M27BIT = 7
	MIXEDFORWARD = 8
	MIXEDBACKWARD = 9
	MIXEDRIGHT = 10
	MIXEDLEFT = 11
	MIXEDFB = 12
	MIXEDLR = 13
	GETM1ENC = 16
	GETM2ENC = 17
	GETM1SPEED = 18
	GETM2SPEED = 19
	RESETENC = 20
	GETVERSION = 21
	SETM1ENCCOUNT = 22
	SETM2ENCCOUNT = 23
	GETMBATT = 24
	GETLBATT = 25
	SETMINLB = 26
	SETMAXLB = 27
	SETM1PID = 28
	SETM2PID = 29
	GETM1ISPEED = 30
	GETM2ISPEED = 31
	M1DUTY = 32
	M2DUTY = 33
	MIXEDDUTY = 34
	M1SPEED = 35
	M2SPEED = 36
	MIXEDSPEED = 37
	M1SPEEDACCEL = 38
	M2SPEEDACCEL = 39
	MIXEDSPEEDACCEL = 40
	M1SPEEDDIST = 41
	M2SPEEDDIST = 42
	MIXEDSPEEDDIST = 43
	M1SPEEDACCELDIST = 44
	M2SPEEDACCELDIST = 45
	MIXEDSPEEDACCELDIST = 46
	GETBUFFERS = 47
	GETPWMS = 48
	GETCURRENTS = 49
	MIXEDSPEED2ACCEL = 50
	MIXEDSPEED2ACCELDIST = 51
	M1DUTYACCEL = 52
	M2DUTYACCEL = 53
	MIXEDDUTYACCEL = 54
	READM1PID = 55
	READM2PID = 56
	SETMAINVOLTAGES = 57
	SETLOGICVOLTAGES = 58
	GETMINMAXMAINVOLTAGES = 59
	GETMINMAXLOGICVOLTAGES = 60
	SETM1POSPID = 61
	SETM2POSPID = 62
	READM1POSPID = 63
	READM2POSPID = 64
	M1SPEEDACCELDECCELPOS = 65
	M2SPEEDACCELDECCELPOS = 66
	MIXEDSPEEDACCELDECCELPOS = 67
	SETM1DEFAULTACCEL = 68
	SETM2DEFAULTACCEL = 69
	SETPINFUNCTIONS = 74
	GETPINFUNCTIONS = 75
	RESTOREDEFAULTS = 80
	GETTEMP = 82
	GETTEMP2 = 83
	GETERROR = 90
	GETENCODERMODE = 91
	SETM1ENCODERMODE = 92
	SETM2ENCODERMODE = 93
	WRITENVM = 94
	READNVM = 95
	SETCONFIG = 98
	GETCONFIG = 99
	SETM1MAXCURRENT = 133
	SETM2MAXCURRENT = 134
	GETM1MAXCURRENT = 135
	GETM2MAXCURRENT = 136
	SETPWMMODE = 148
	GETPWMMODE = 149
	FLAGBOOTLOADER = 255
			
#Private Functions

def _sendcommand(address,command):
	global _checksum
	_checksum = address
	port.write(chr(address))
	_checksum += command
	port.write(chr(command))
	return

def _readchecksumbyte():
	data = port.read(1)
	if len(data):
		val = ord(data);
		return (1,val)	
	return (0,0)
	
def _readbyte():
	global _checksum
	data = port.read(1)
	if len(data):
		val = ord(data)
		_checksum += val
		return (1,val)	
	return (0,0)
	
def _readword():
	val1 = _readbyte()
	if val1[0]:
		val2 = _readbyte()
		if val2[0]:
			return (1,val1[1]<<8|val2[1])
	return (0,0)

def _readlong():
	val1 = _readbyte()
	if val1[0]:
		val2 = _readbyte()
		if val2[0]:
			val3 = _readbyte()
			if val3[0]:
				val4 = _readbyte()
				if val4[0]:
					return (1,val1[1]<<24|val2[1]<<16|val3[1]<<8|val4[1])
	return (0,0)	

def _readslong():
	val = _readlong()
	if val[0]:
		if val[1]&0x80000000:
			val[1] = val[1]-0x100000000
	return val	

def _writebyte(val):
	global _checksum
	_checksum += val
	return port.write(struct.pack('>B',val))
def _writesbyte(val):
	global _checksum
	_checksum += val
	return port.write(struct.pack('>b',val))
def _writeword(val):
	global _checksum
	_checksum += val
	_checksum += (val>>8)&0xFF
	return port.write(struct.pack('>H',val))
def _writesword(val):
	global _checksum
	_checksum += val
	_checksum += (val>>8)&0xFF
	return port.write(struct.pack('>h',val))
def _writelong(val):
	global _checksum
	_checksum += val
	_checksum += (val>>8)&0xFF
	_checksum += (val>>16)&0xFF
	_checksum += (val>>24)&0xFF
	return port.write(struct.pack('>L',val))
def _writeslong(val):
	global _checksum
	_checksum += val
	_checksum += (val>>8)&0xFF
	_checksum += (val>>16)&0xFF
	_checksum += (val>>24)&0xFF
	return port.write(struct.pack('>l',val))

def _read1(cmd):
	global _checksum
	trys = 2
	while 1:
		_sendcommand(128,cmd)
		val1 = _readbyte()
		if val1[0]:
			crc = _readchecksumbyte()
			if crc[0]:
				if _checksum&0x7F!=crc[1]&0x7F:
					return (0,0)
				return (1,val1[1])
		trys-=1
		if trys==0:
			break
	return (0,0)

def _read2(cmd):
	global _checksum
	trys = 2
	while 1:
		_sendcommand(128,cmd)
		val1 = _readword()
		if val1[0]:
			crc = _readchecksumbyte()
			if crc[0]:
				if _checksum&0x7F!=crc[1]&0x7F:
					return (0,0)
				return (1,val1[1])
		trys-=1
		if trys==0:
			break
	return (0,0)

def _read4(cmd):
	global _checksum
	trys = 2
	while 1:
		_sendcommand(128,cmd)
		val1 = _readlong()
		if val1[0]:
			crc = _readchecksumbyte()
			if crc[0]:
				if _checksum&0x7F!=crc[1]&0x7F:
					return (0,0)
				return (1,val1[1])
		trys-=1
		if trys==0:
			break
	return (0,0)

def _read4_1(cmd):
	global _checksum
	trys = 2
	while 1:
		_sendcommand(128,cmd)
		val1 = _readslong()
		if val1[0]:
			val2 = _readbyte()
			if val2[0]:
				crc = _readchecksumbyte()
				if crc[0]:
					if _checksum&0x7F!=crc[1]&0x7F:
						return (0,0)
					return (1,val1[1],val2[1])
		trys-=1
		if trys==0:
			break
	return (0,0)

def _read_n(cmd,args):
	global _checksum
	trys = 3
	while 1:
		trys-=1
		if trys==0:
			break
		failed=False
		_sendcommand(128,cmd)
		data = [1,]
		for i in range(0,args):
			val = _readlong()
			if val[0]==0:
				failed=True
				break
			data.append(val[1])
		if failed:
			continue
		crc = _readchecksumbyte()
		if crc[0]:
			if crc[1]&0x7F==_checksum&0x7F:
				return (data);
	return (0,0,0,0,0)

def _writechecksum():
	global _checksum
	_writebyte(_checksum&0x7F | 0x80)
	val = _readbyte()
	if val[0]:
		return True
	return False

#User accessible functions

def M1Forward(val):
	_sendcommand(128,Cmd.M1FORWARD)
	_writebyte(val)
	return _writechecksum()

def M1Backward(val):
	_sendcommand(128,Cmd.M1BACKWARD)
	_writebyte(val)
	return _writechecksum()

def SetMinMainBattery(val):
	_sendcommand(128,Cmd.SETMINMB)
	_writebyte(val)
	return _writechecksum()

def SetMaxMainBattery(val):
	_sendcommand(128,Cmd.SETMAXMB)
	_writebyte(val)
	return _writechecksum()

def M2Forward(val):
	_sendcommand(128,Cmd.M2FORWARD)
	_writebyte(val)
	return _writechecksum()

def M2Backward(val):
	_sendcommand(128,Cmd.M2BACKWARD)
	_writebyte(val)
	return _writechecksum()

def DriveM1(val):
	_sendcommand(128,Cmd.M17BIT)
	_writebyte(val)
	return _writechecksum()

def DriveM2(val):
	_sendcommand(128,Cmd.M27BIT)
	_writebyte(val)
	return _writechecksum()

def ForwardMixed(val):
	_sendcommand(128,Cmd.MIXEDFORWARD)
	_writebyte(val)
	return _writechecksum()

def BackwardMixed(val):
	_sendcommand(128,Cmd.MIXEDBACKWARD)
	_writebyte(val)
	return _writechecksum()

def RightMixed(val):
	_sendcommand(128,Cmd.MIXEDRIGHT)
	_writebyte(val)
	return _writechecksum()

def LeftMixed(val):
	_sendcommand(128,Cmd.MIXEDLEFT)
	_writebyte(val)
	return _writechecksum()

def DriveMixed(val):
	_sendcommand(128,Cmd.MIXEDFB)
	_writebyte(val)
	return _writechecksum()

def TurnMixed(val):
	_sendcommand(128,Cmd.MIXEDLR)
	_writebyte(val)
	return _writechecksum()

def ReadM1Encoder():
	return _read4_1(Cmd.GETM1ENC)

def ReadM2Encoder():
	return _read4_1(Cmd.GETM2ENC)

def ReadM1Speed():
	return _read4_1(Cmd.GETM1SPEED)

def ReadM2Speed():
	return _read4_1(Cmd.GETM2SPEED)

def ResetEncoders():
	_sendcommand(128,Cmd.RESETENC)
	return _writechecksum()

def ReadVersion():
	global _checksum
	trys=2
	while 1:
		_sendcommand(128,Cmd.GETVERSION)
		str = ""
		passed = True
		for i in range(0,48):
			data = port.read(1)
			if len(data):
				val = ord(data)
				if(val==0):
					break
				_checksum+=val
				str+=data[0]
			else:
				passed = False
				break
		if passed:
			crc = _readchecksumbyte()
			if crc[0]:
				if(crc[1]&0x7F==_checksum&0x7F):
					return (1,str)
				else:
					break
		trys-=1
		if trys==0:
			break
	return (0,0)

def SetM1EncoderCnt(cnt):
	_sendcommand(128,Cmd.SETM1ENCCOUNT)
	_writelong(cnt)
	return _writechecksum()

def SetM2EncoderCnt(cnt):
	_sendcommand(128,Cmd.SETM2ENCCOUNT)
	_writelong(cnt)
	return _writechecksum()

def ReadMainBattery():
	return _read2(Cmd.GETMBATT)

def ReadLogicBattery():
	return _read2(Cmd.GETLBATT)

def SetM1VelocityConstants(p,i,d,qpps):
	_sendcommand(128,Cmd.SETM1PID)
	_writelong(d*65536)
	_writelong(p*65536)
	_writelong(i*65536)
	_writelong(qpps)
	return _writechecksum()

def SetM2VelocityConstants(p,i,d,qpps):
	_sendcommand(128,Cmd.SETM2PID)
	_writelong(d*65536)
	_writelong(p*65536)
	_writelong(i*65536)
	_writelong(qpps)
	return _writechecksum()

def ReadM1ISpeed():
	return _read4_1(Cmd.GETM1ISPEED)

def ReadM2ISpeed():
	return _read4_1(Cmd.GETM2ISPEED)

def SetM1Duty(val):
	_sendcommand(128,Cmd.M1DUTY)
	_writesword(val)
	return _writechecksum()

def SetM2Duty(val):
	_sendcommand(128,Cmd.M2DUTY)
	_writesword(val)
	return _writechecksum()

def SetMixedDuty(m1,m2):
	_sendcommand(128,Cmd.MIXEDDUTY)
	_writesword(m1)
	_writesword(m2)
	return _writechecksum()

def SetM1Speed(val):
	_sendcommand(128,Cmd.M1SPEED)
	_writeslong(val)
	return _writechecksum()

def SetM2Speed(val):
	_sendcommand(128,Cmd.M2SPEED)
	_writeslong(val)
	return _writechecksum()

def SetMixedSpeed(m1,m2):
	_sendcommand(128,Cmd.MIXEDSPEED)
	_writeslong(m1)
	_writeslong(m2)
	return _writechecksum();

def SetM1SpeedAccel(accel,speed):
	_sendcommand(128,Cmd.M1SPEEDACCEL)
	_writelong(accel)
	_writeslong(speed)
	return _writechecksum()

def SetM2SpeedAccel(accel,speed):
	_sendcommand(128,Cmd.M2SPEEDACCEL)
	_writelong(accel)
	_writeslong(speed)
	return _writechecksum()

def SetMixedSpeedAccel(accel,speed1,speed2):
	_sendcommand(128,Cmd.MIXEDSPEED2ACCEL)
	_writelong(accel)
	_writeslong(speed1)
	_writeslong(speed2)
	return _writechecksum();

def SetM1SpeedDistance(speed,distance,buffer):
	_sendcommand(128,Cmd.M1SPEEDDIST)
	_writeslong(speed)
	_writelong(distance)
	_writebyte(buffer)
	return _writechecksum()

def SetM2SpeedDistance(speed,distance,buffer):
	_sendcommand(128,Cmd.M2SPEEDDIST)
	_writeslong(speed)
	_writelong(distance)
	_writebyte(buffer)
	return _writechecksum()

def SetMixedSpeedDistance(speed1,distance1,speed2,distance2,buffer):
	_sendcommand(128,Cmd.MIXEDSPEEDDIST)
	_writeslong(speed1)
	_writelong(distance1)
	_writeslong(speed2)
	_writelong(distance2)
	_writebyte(buffer)
	return _writechecksum()

def SetM1SpeedAccelDistance(accel,speed,distance,buffer):
	_sendcommand(128,Cmd.M1SPEEDACCELDIST)
	_writelong(accel)
	_writeslong(speed)
	_writelong(distance)
	_writebyte(buffer)
	return _writechecksum()

def SetM2SpeedAccelDistance(accel,speed,distance,buffer):
	_sendcommand(128,Cmd.M2SPEEDACCELDIST)
	_writelong(accel)
	_writeslong(speed)
	_writelong(distance)
	_writebyte(buffer)
	return _writechecksum()

def SetMixedSpeedAccelDistance(accel,speed1,distance1,speed2,distance2,buffer):
	_sendcommand(128,Cmd.MIXEDSPEED2ACCELDIST)
	_writelong(accel)
	_writeslong(speed1)
	_writelong(distance1)
	_writeslong(speed2)
	_writelong(distance2)
	_writebyte(buffer)
	return _writechecksum()

def ReadBuffers():
	val = _read2(Cmd.GETBUFFERS)
	if val[0]:
		return (1,val[1]>>8,val[1]&0xFF)
	return (0,0,0)

def ReadPWMs():
	val = _read4(Cmd.GETPWMS)
	if val[0]:
		cur1 = val[1]>>16
		cur2 = val[1]&0xFFFF
		if pwm1&0x8000:
			pwm1-=0x10000
		if pwm2&0x8000:
			pwm2-=0x10000
		return (1,pwm1,pwm2)
	return (0,0,0)

def ReadCurrents():
	val = _read4(Cmd.GETCURRENTS)
	if val[0]:
		cur1 = val[1]>>16
		cur2 = val[1]&0xFFFF
		if cur1&0x8000:
			cur1-=0x10000
		if cur2&0x8000:
			cur2-=0x10000
		return (1,cur1,cur2)
	return (0,0,0)

def SetMixedSpeed2Accel(accel1,speed1,accel2,speed2):
	_sendcommand(128,Cmd.MIXEDSPEED2ACCEL)
	_writelong(accel1)
	_writeslong(speed1)
	_writelong(accel2)
	_writeslong(speed2)
	return _writechecksum()

def SetMixedSpeed2AccelDistance(accel1,speed1,distance1,accel2,speed2,distance2,buffer):
	_sendcommand(128,Cmd.MIXEDSPEED2ACCELDIST)
	_writelong(accel1)
	_writeslong(speed1)
	_writelong(distance1)
	_writelong(accel2)
	_writeslong(speed2)
	_writelong(distance2)
	_writebyte(buffer)
	return _writechecksum()

def SetM1DutyAccel(accel,duty):
	_sendcommand(128,Cmd.M1DUTYACCEL)
	_writesword(duty)
	_writelong(accel)
	return _writechecksum()

def SetM2DutyAccel(accel,duty):
	_sendcommand(128,Cmd.M2DUTYACCEL)
	_writesword(duty)
	_writelong(accel)
	return _writechecksum()

def SetMixedDutyAccel(accel1,duty1,accel2,duty2):
	_sendcommand(128,Cmd.MIXEDDUTYACCEL)
	_writesword(duty1)
	_writeword(accel1)
	_writesword(duty2)
	_writeword(accel2)
	return _writechecksum()
	
def ReadM1VelocityConstants():
	data = _read_n(Cmd.READM1PID,4)
	if data[0]:
		data[1]/=65536.0
		data[2]/=65536.0
		data[3]/=65536.0
		return data
	return (0,0,0,0,0)

def ReadM2VelocityConstants():
	data = _read_n(Cmd.READM2PID,4)
	if data[0]:
		data[1]/=65536.0
		data[2]/=65536.0
		data[3]/=65536.0
		return data
	return (0,0,0,0,0)

def SetMainVoltages(min, max):
	_sendcommand(128,Cmd.SETMAINVOLTAGES)
	_writeword(min)
	_writeword(max)
	return _writechecksum();
	
def SetLogicVoltages(min, max):
	_sendcommand(128,Cmd.SETLOGICVOLTAGES)
	_writeword(min)
	_writeword(max)
	return _writechecksum();
	
def ReadMainBatterySettings():
	val = _read4(Cmd.GETMINMAXMAINVOLTAGES)
	if val[0]:
		min = val[1]>>16
		max = val[1]&0xFFFF
		return (1,min,max)
	return (0,0,0)

def ReadLogicBatterySettings():
	val = _read4(Cmd.GETMINMAXLOGICVOLTAGES)
	if val[0]:
		min = val[1]>>16
		max = val[1]&0xFFFF
		return (1,min,max)
	return (0,0,0)

def SetM1PositionConstants(kp,ki,kd,kimax,deadzone,min,max):
	_sendcommand(128,Cmd.SETM1POSPID)
	_writelong(kd*1024)
	_writelong(kp*1024)
	_writelong(ki*1024)
	_writelong(kimax*1024)
	_writelong(deadzone)
	_writelong(min)
	_writelong(max)
	return _writechecksum()

def SetM2PositionConstants(kp,ki,kd,kimax,deadzone,min,max):
	_sendcommand(128,Cmd.SETM2POSPID)
	_writelong(kd*1024)
	_writelong(kp*1024)
	_writelong(ki*1024)
	_writelong(kimax*1024)
	_writelong(deadzone)
	_writelong(min)
	_writelong(max)
	return _writechecksum()

def ReadM1PositionConstants():
	data = _read_n(Cmd.READM1POSPID,7)
	if data[0]:
		data[0]/=1024.0
		data[1]/=1024.0
		data[2]/=1024.0
		data[3]/=1024.0
		return data
	return (0,0,0,0,0,0,0,0)
	
def ReadM2PositionConstants():
	data = _read_n(Cmd.READM2POSPID,7)
	if data[0]:
		data[0]/=1024.0
		data[1]/=1024.0
		data[2]/=1024.0
		data[3]/=1024.0
		return data
	return (0,0,0,0,0,0,0,0)

def SetM1SpeedAccelDeccelPosition(accel,speed,deccel,position,buffer):
	_sendcommand(128,Cmd.M1SPEEDACCELDECCELPOS)
	_writelong(accel)
	_writelong(speed)
	_writelong(deccel)
	_writelong(position)
	_writebyte(buffer)
	return _writechecksum()

def SetM2SpeedAccelDeccelPosition(accel,speed,deccel,position,buffer):
	_sendcommand(128,Cmd.M2SPEEDACCELDECCELPOS)
	_writelong(accel)
	_writelong(speed)
	_writelong(deccel)
	_writelong(position)
	_writebyte(buffer)
	return _writechecksum()

def SetMixedSpeedAccelDeccelPosition(accel1,speed1,deccel1,position1,accel2,speed2,deccel2,position2,buffer):
	_sendcommand(128,Cmd.MIXEDSPEEDACCELDECCELPOS)
	_writelong(accel1)
	_writelong(speed1)
	_writelong(deccel1)
	_writelong(position1)
	_writelong(accel2)
	_writelong(speed2)
	_writelong(deccel2)
	_writelong(position2)
	_writebyte(buffer)
	return _writechecksum()

def SetM1DefaultAccel(accel):
	_sendcommand(128,Cmd.SETM1DEFAULTACCEL)
	_writelong(accel)
	return _writechecksum()

def SetM2DefaultAccel(accel):
	_sendcommand(128,Cmd.SETM2DEFAULTACCEL)
	_writelong(accel)
	return _writechecksum()

def SetPinFunctions(S3mode,S4mode,S5mode):
	_sendcommand(128,Cmd.SETPINFUNCTIONS)
	_writebyte(S3mode)
	_writebyte(S4mode)
	_writebyte(S5mode)
	return _writechecksum()

def ReadPinFunctions():
	global _checksum
	trys = 2
	while 1:
		_sendcommand(128,Cmd.GETPINFUNCTIONS)
		val1 = _readbyte()
		if val1[0]:
			val2 = _readbyte()
			if val1[0]:
				val3 = _readbyte()
				if val1[0]:
					crc = _readchecksumbyte()
					if crc[0]:
						if _checksum&0x7F!=crc[1]&0x7F:
							return (0,0)
						return (1,val1[1],val2[1],val3[1])
		trys-=1
		if trys==0:
			break
	return (0,0)

#Warning(TTL Serial): Baudrate will change if not already set to 38400.  Communications will be lost
def RestoreDefaults():
	_sendcommand(128,Cmd.RESTOREDEFAULTS)
	return _writechecksum()

def ReadTemperature():
	return _read2(Cmd.GETTEMP)

def ReadTemperature2():
	return _read2(Cmd.GETTEMP2)

def ReadStatus():
	return _read2(Cmd.GETERROR)

def ReadEncoderModes():
	val = _read2(Cmd.GETENCODERMODE)
	if val[0]:
		return (1,val[1]>>8,val[1]&0xFF)
	return (0,0,0)
	
def SetM1EncoderMode(mode):
	_sendcommand(128,Cmd.SETM1ENCODERMODE)
	_writebyte(mode)
	return _writechecksum()

def SetM2EncoderMode(mode):
	_sendcommand(128,Cmd.SETM2ENCODERMODE)
	_writebyte(mode)
	return _writechecksum()

#saves active settings to NVM
def WriteNVM():
	_sendcommand(128,Cmd.WRITENVM)
	_writelong(0xE22EAB7A)
	return _writechecksum()

#restores settings from NVM
#Warning(TTL Serial): If baudrate changes or the control mode changes communications will be lost
def ReadNVM():
	_sendcommand(128,Cmd.READNVM)
	return _writechecksum()

#Warning(TTL Serial): If control mode is changed from packet serial mode when setting config communications will be lost!
#Warning(TTL Serial): If baudrate of packet serial mode is changed communications will be lost!
def SetConfig(config):
	_sendcommand(128,Cmd.SETCONFIG)
	_writeword(config)
	return _writechecksum()

def ReadConfig():
	return _read2(Cmd.GETCONFIG)

def SetM1MaxCurrent(max):
	_sendcommand(128,Cmd.SETM1MAXCURRENT)
	_writelong(max)
	_writelong(0)
	return _writechecksum()

def SetM2MaxCurrent(max):
	_sendcommand(128,Cmd.SETM2MAXCURRENT)
	_writelong(max)
	_writelong(0)
	return _writechecksum()

def ReadM1MaxCurrent():
	data = _read_n(Cmd.GETM1MAXCURRENT,2)
	if data[0]:
		return (1,data[1])
	return (0,0)

def ReadM2MaxCurrent():
	data = _read_n(Cmd.GETM2MAXCURRENT,2)
	if data[0]:
		return (1,data[1])
	return (0,0)

def SetPWMMode(mode):
	_sendcommand(128,Cmd.SETPWMMODE)
	_writebyte(mode)
	return _writechecksum()

def ReadPWMMode():
	return _read1(Cmd.GETPWMMODE)

def Open(comport, rate):
	global port
	port = serial.Serial(comport, baudrate=rate, timeout=1, interCharTimeout=0.01)
	return

