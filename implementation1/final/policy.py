#!/usr/bin/env python

import math
from random import *
from rewards import *

def policyA(agent0, agent1): # both random always
	action0 = randint(1,3) # random policy for agent0
	action1 = randint(1,3) # random policy for agent1

	print("action0 = " + repr(action0) + " action1 = " + repr(action1))	
	return action0, action1

def policyB(agent0, agent1): # if agent0 has no input from environment it listens/agent1 is random
	if agent0 == 0.5:
		action0 = 3
	else:
		if agent0 > 0.5:
			action0 = 2
		elif agent0 < 0.5:
			action0 = 1
		else:
			print("Something went wrong! agent0 action0")
	action1 = randint(1,3)

	print("action0 = " + repr(action0) + " action1 = " + repr(action1))	
	return action0, action1

def policyC(agent0, agent1): # if agent0 has no input from environment it listens/if agent1 has no input from environment it listens
	if agent0 == 0.5:
		action0 = 3
	else:
		if agent0 > 0.5:
			action0 = 2
		elif agent0 < 0.5:
			action0 = 1
		else:
			print("Something went wrong! agent0 action0")
	if agent1 == 0.5:
		action1 = 3
	else:
		if agent1 > 0.5:
			action1 = 2
		elif agent1 < 0.5:
			action1 = 1
		else:
			print("Something went wrong! agent1 action1")
	
	print("action0 = " + repr(action0) + " action1 = " + repr(action1))	
	return action0, action1