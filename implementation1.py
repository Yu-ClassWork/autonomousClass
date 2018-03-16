#!/usr/bin/env python
# classic triger problem
# PROBLEM DESCRIPTION
# two agents face two doors. one door has a hungry tiger and the other door has money. the position of these are unknown.
# 
import math
import importlib
from random import *
from rewards import *

def initializing():
	tigerDoor = randint(1,2) # ground truth of where the tiger is (1: tiger is behind 1 SL, 2: tiger is behind 2 SR)
	agent0 = 0.5 # belief that the tiger is behind door 1 for agent0
	agent1 = 0.5 # belief that the tiger is behind door 1 for agent1
	print("Door the tiger is behind = " + repr(tigerDoor))
	return tigerDoor, agent0, agent1

def choosingAction(agent0, agent1):
	if agent0 == 0.5:
		action0 = randint(1,3) # random policy for agent0
	else:
		if agent0 > 0.5:
			action0 = 2
		elif agent0 < 0.5:
			action0 = 1
		else:
			print("Something went wrong! agent0 action0")
	if agent1 == 0.5:
		action1 = randint(1,3) # random policy for agent1
	else:
		if agent1 > 0.5:
			action1 = 2
		elif agent1 < 0.5:
			action1 = 1
		else:
			print("Something went wrong! agent1 action1")
	print("action0 = " + repr(action0) + " action1 = " + repr(action1))	
	return action0, action1



def main():
	agent0 = []
	agent1 = []
	policy0 = [0]
	policy1 = [0]
	state = 0
	reward = 0
	totalReward = 0
	listened = 0
	while True:
		if listened == 0:
			tigerDoor, agent0, agent1 = initializing()

		action0, action1 = choosingAction(agent0, agent1)
		listened, reward = reward1(tigerDoor, action0, action1)

		totalReward = totalReward + reward
		print("totalReward: " + repr(totalReward))
		input("Press Enter to for next round!")

if __name__ == '__main__':
	main()