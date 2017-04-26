import Motor
from MotorState import MotorState

class MotorManager():
	def __init__(self, motorLeft, motorRight):
		self.mLeft = motorLeft
		self.mRight = motorRight
		self.state = MotorState.CENTER

	def setDirection(self, horizontal, depth):
		if horizontal == "left":
			if depth == "forward":
				self.state = MotorState.FORWARD_LEFT
			elif depth == "backward":
				self.state = MotorState.BACKWARD_LEFT
			else:
				self.state = MotorState.LEFT
		elif horizontal == "right":
			if depth == "forward":
				self.state = MotorState.FORWARD_RIGHT
			elif depth == "backward":
				self.state = MotorState.BACKWARD_RIGHT
			else:
				self.state = MotorState.RIGHT
		else:
			if depth == "forward":
				self.state = MotorState.FORWARD
			elif depth == "backward":
				self.state = MotorState.BACKWARD
			else:
				self.state = MotorState.CENTER

	def setMovement(self):
		if self.state == MotorState.CENTER:
			self.stop()
		elif self.state == MotorState.FORwARD:
			self.forward()
		elif self.state == MotorState.BACKWARD:
			self.backward()
		elif self.state == MotorState.RIGHT:
			self.right()
		elif self.state == MotorState.LEFT:
			self.left()
		elif self.state == MotorState.FORWARD_RIGHT:
			self.forwardRight()
		elif self.state == MotorState.FORWARD_LEFT:
			self.forwardLeft()
		elif self.state == BACKWARD_RIGHT:
			self.backwardRight()
		elif self.state == BACKWARD_LEFT:
			self.backwardLeft()

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

	def forwardRight(self):
		self.mLeft.forward()
		self.mRight.stop()

	def forwardLeft(self):
		self.mLeft.stop()
		self.mRight.forward()

	def backwardRight(self):
		self.mLeft.backward()
		self.mRight.stop()

	def backwardLeft(self):
		self.mLeft.stop()
		self.mRight.backward()

