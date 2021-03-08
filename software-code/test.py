from lx16a import *
from math import sin, cos
import time

buffer = 1000
unit_convert = 1000
LX16A.initialize("COM5")

# motor class, parameter: joint name, motor ID, motor initial pos
class motor():
	def __init__(self, name, ID, pos):
		self.m_name = name
		self.engine = LX16A(ID)
		self.initial = pos

#robot class iniital each joint
class Robot():
	def __init__(self):
		self.left_mid = motor("left_keen", 1, 125)
		self.left_shoulder = motor("left_shoulder",3, 150)
		self.left_foot = motor("left_foot", 2, 125)
		self.motors = [self.left_mid, self.left_shoulder, self.left_foot]
	
	# moving algorithm
	def move(self):
		t = 0
		#boot check
		if self.boot():
			time.sleep(3)
			while True:
				self.left_foot.engine.moveTimeWrite(-sin(0.5*t) * 10 + self.left_foot.initial)
				self.left_shoulder.engine.moveTimeWrite(sin(0.2*t) * 30 + self.left_shoulder.initial)
				t += 0.01
		else:
			print("motor issue")
	
	#dance algorithm
	def dance(self):
		return
	
	#home and boot check
	def boot(self):
		for i in range(len(self.motors)):
			cur_motor, cur_motor_name , init_pos = self.motors[i].engine, self.motors[i].m_name, self.motors[i].initial
			voltage = cur_motor.vInRead() / unit_convert
			if not voltage or voltage < 4.5:
				print(cur_motor_name + "voltage issue")
				return False
			print(cur_motor_name + 's voltge is ', voltage)
			cur_motor.moveTimeWrite(init_pos, buffer)

		return True

#main function
if __name__ == "__main__":
	robot = Robot()
	robot.boot()




