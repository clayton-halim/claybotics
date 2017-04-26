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
				state = MotorState.FORWARD_LEFT
			elif depth == "backward":
				state = MotorState.BACKWARD_LEFT
			else:
				state = MotorState.LEFT
		elif horizontal == "right":
			if depth == "forward":
				state = MotorState.FORWARD_RIGHT
			elif depth == "backward":
				state = MotorState.BACKWARD_RIGHT
			else:
				state = MotorState.RIGHT
		else:
			if depth == "forward":
				state = MotorState.FORWARD
			elif depth == "backward":
				state = MotorState.BACKWARD
			else:
				state = MotorState.CENTER

	def setMovement(self):
		if state == MotorState.CENTER:
			self.stop()
		elif state == MotorState.FORwARD:
			self.forward()
		elif state == MotorState.BACKWARD:
			self.backward()
		elif state == MotorState.RIGHT:
			self.right()
		elif state == MotorState.LEFT:
			self.left()
		elif state == MotorState.FORWARD_RIGHT:
			self.forwardRight()
		elif state == MotorState.FORWARD_LEFT:
			self.forwardLeft()
		elif state == BACKWARD_RIGHT:
			self.backwardRight()
		elif state == BACKWARD_LEFT:
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

