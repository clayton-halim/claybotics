from enum import Enum

class MotorState(Enum):
	CENTER = 0
	FORWARD_LEFT = 1
	FORWARD = 2
	FORWARD_RIGHT = 3
	RIGHT = 4
	BACKWARD_RIGHT = 5
	BACKWARD = 6
	BACKWARD_LEFT = 7
	LEFT = 8