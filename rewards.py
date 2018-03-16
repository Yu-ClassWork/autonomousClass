#!/usr/bin/env python

import math
from random import *

def reward1(tigerDoor, action0, action1):
	if tigerDoor == 1:
		if action0 == 2 and action1 == 2:
			listened = 0
			reward = 20
			print("reward = " + repr(reward))
		elif action0 == 1 and action1 == 1:
			listened = 0
			reward = -50
			print("reward = " + repr(reward))
		elif action0 == 2 and action1 == 1:	
			listened = 0
			reward = -100
			print("reward = " + repr(reward))
		elif action0 == 1 and action1 == 2:
			listened = 0
			reward = -100
			print("reward = " + repr(reward))
		elif action0 == 3 and action1 == 3:
			agent0 = 0.85
			agent1 = 0.85
			listened = 1
			reward = -2
			print("reward = " + repr(reward))
		elif action0 == 3 and action1 == 2:
			listened = 0
			reward = 9
			print("reward = " + repr(reward))
		elif action0 == 2 and action1 == 3:
			listened = 0
			reward = 9
			print("reward = " + repr(reward))
		elif action0 == 3 and action1 == 1:
			listened = 0
			reward = -101
			print("reward = " + repr(reward))
		elif action0 == 1 and action1 == 3:
			listened = 0
			reward = -101
			print("reward = " + repr(reward))
	elif tigerDoor == 2:
		if action0 == 2 and action1 == 2:
			listened = 0
			reward = -50
			print("reward = " + repr(reward))
		elif action0 == 1 and action1 == 1:
			listened = 0
			reward = 20
			print("reward = " + repr(reward))
		elif action0 == 2 and action1 == 1:	
			listened = 0
			reward = -100
			print("reward = " + repr(reward))
		elif action0 == 1 and action1 == 2:
			listened = 0
			reward = -100
			print("reward = " + repr(reward))
		elif action0 == 3 and action1 == 3:
			agent0 = 0.15
			agent1 = 0.15
			listened = 1
			reward = -2
			print("reward = " + repr(reward))
		elif action0 == 3 and action1 == 2:
			listened = 0
			reward = -101
			print("reward = " + repr(reward))
		elif action0 == 2 and action1 == 3:
			listened = 0
			reward = -101
			print("reward = " + repr(reward))
		elif action0 == 3 and action1 == 1:
			listened = 0
			reward = 9
			print("reward = " + repr(reward))
		elif action0 == 1 and action1 == 3:
			listened = 0
			reward = 9
			print("reward = " + repr(reward))
	else:
		print("Something went wrong with creating the tigerDoor")
	return listened, reward