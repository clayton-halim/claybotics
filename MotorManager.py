import Motor

class MotorManager():
	def __init__(self, motorLeft, motorRight):
		self.mLeft = motorLeft
		self.mRight = motorRight

	def forward(self):
		self.mLeft.forward()
		self.mRight.forward()

	def backward(self):
		self.mLeft.backward()
		self.mRight.backward()

	def stop(self):
		self.mLeft.stop()
		self.mRight.stop()

	def right(self):
		self.mLeft.forward()
		self.mRight.backward()

	def left(self):
		self.mLeft.backward()
		self.mRight.forward()


