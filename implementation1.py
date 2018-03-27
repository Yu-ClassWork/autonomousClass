#!/usr/bin/env python
# classic triger problem
# PROBLEM DESCRIPTION
# two agents face two doors. one door has a hungry tiger and the other door has money. the position of these are unknown.

import math
from random import *
from rewards import *
from policy import *
import matplotlib.pyplot as plt

def initializing():
	tigerDoor = randint(1,2) # ground truth of where the tiger is (1: tiger is behind 1 SL, 2: tiger is behind 2 SR)
	agent0 = 0.5 # belief that the tiger is behind door 1 for agent0
	agent1 = 0.5 # belief that the tiger is behind door 1 for agent1
	print("Door the tiger is behind = " + repr(tigerDoor))
	return tigerDoor, agent0, agent1

def main():
	agent0 = []
	agent1 = []
	policy0 = [0]
	policy1 = [0]
	state = 0
	reward = 0
	totalReward = [0]
	listened = 0
	i = 0
	policyType = input("What policy do you want to use?")
	policyType = int(policyType)
	# while True:
	for i in range(0,300):
		if 1 <= policyType <= 3:
			if listened == 0:
				tigerDoor, agent0, agent1 = initializing()
			if policyType == 1:
				action0, action1 = policyA(agent0, agent1)
			elif policyType == 2:
				action0, action1 = policyB(agent0, agent1)
			elif policyType == 3:
				action0, action1 = policyC(agent0, agent1)
			

			listened, reward, agent0, agent1 = rewardA(tigerDoor, action0, action1, agent0, agent1)
			print(agent0, agent1)
			i = i+1
			totalReward.append(totalReward[i-1] + reward)
			# print("totalReward: " + repr(totalReward[i]))
			# input("Press Enter to for next round!")
		else:
			policyType = input("Not a suitable policy. Pick a number 1, 2 or 3.")
			policyType = int(policyType)
		# except KeyboardInterrupt:
		# 	break
	plt.plot(range(0,i+1), totalReward)
	plt.show()


if __name__ == '__main__':
	main()