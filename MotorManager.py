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
				print("forward left")
				self.state = MotorState.FORWARD_LEFT
			elif depth == "backward":
				print("backward left")
				self.state = MotorState.BACKWARD_LEFT
			else:
				print("left")
				self.state = MotorState.LEFT
		elif horizontal == "right":
			if depth == "forward":
				print("forward right")
				self.state = MotorState.FORWARD_RIGHT
			elif depth == "backward":
				print("backward right")
				self.state = MotorState.BACKWARD_RIGHT
			else:
				print("right")
				self.state = MotorState.RIGHT
		elif horizontal == "center":
			if depth == "forward":
				print("forward")
				self.state = MotorState.FORWARD
			elif depth == "backward":
				print("backward")
				self.state = MotorState.BACKWARD
			else:
				print("stop")
				self.state = MotorState.CENTER

	def setMovement(self):
		if self.state == MotorState.CENTER:
			self.stop()
		elif self.state == MotorState.FORWARD:
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
		elif self.state == MotorState.BACKWARD_RIGHT:
			self.backwardRight()
		elif self.state == MotorState.BACKWARD_LEFT:
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

