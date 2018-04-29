#!/usr/bin/env python

import math
import matplotlib.pyplot as plt
import numpy as np
from random import *

global m, n
m = 13
n = 18

def createGrid(value):
	global m, n
	# Creates a list containing n lists, each of m items, all set to 0
	matrix = [[value for x in range(m)] for y in range(n)]
	return matrix

def up(stateX, stateY):
	global m
	newStateX = stateX
	newStateY = stateY +1
	if newStateY >m-1:
		newStateY = stateY
	return newStateX, newStateY

def right(stateX, stateY):
	global n
	newStateX = stateX +1
	newStateY = stateY
	if newStateX >n-1:
		newStateX = stateX
	return newStateX, newStateY

def down(stateX, stateY):
	newStateX = stateX
	newStateY = stateY -1
	if newStateY <0:
		newStateY = stateY
	return newStateX, newStateY

def left(stateX, stateY):
	newStateX = stateX -1
	newStateY = stateY
	if newStateX <0:
		newStateX = stateX
	return newStateX, newStateY

def collect(agent, rewards, prevAction):
	global m,n
	lock = 0
	if (agent[0]+1) < n and lock == 0 and prevAction != 2:
		if rewards[agent[0]+1][agent[1]] == 1:
			action = 2
			lock = 1
	if (agent[1]+1) < m and lock == 0 and prevAction != 1:
		if rewards[agent[0]][agent[1]+1] == 1:
			action = 1
			lock = 1
	if (agent[0]-1) > -1 and lock == 0 and prevAction != 4:
		if rewards[agent[0]-1][agent[1]] == 1:
			action = 4
			lock = 1
	if (agent[1]-1) > -1 and lock == 0 and prevAction != 3:
		if rewards[agent[0]][agent[1]-1] == 1:
			action = 3
			lock = 1
	if lock == 0:
		action = randint(1,4)
	return action

def collectRowCol(agent, rewards, prevAction):
	global m,n
	lock = 0
	col = np.sum(rewards, axis=0)
	row = np.sum(rewards, axis=1)
	rowSumDown = 0
	rowSumUp = 0
	colSumRight = 0
	colSumLeft = 0
	for i in range(agent[0]+1, n):
		rowSumDown = rowSumDown + row[i]
	for i in range(0, agent[0]):
		rowSumUp = rowSumUp + row[i]
	for i in range(agent[1]+1, m):
		colSumRight = colSumRight + col[i]
	for i in range(0, agent[1]):
		colSumLeft = colSumLeft + col[i]
	sectorRewards = [rowSumDown, rowSumUp, colSumRight, colSumLeft]
	temp = max(sectorRewards)
	locationMax = [i for i, j in enumerate(sectorRewards) if j == temp]
	if locationMax[0] == 0 and prevAction != 2:
		action = 2
	elif locationMax[0] == 1 and prevAction != 4:
		action = 4
	elif locationMax[0] == 2 and prevAction != 1:
		action = 1
	elif locationMax[0] == 3 and prevAction != 3:
		action = 3
	else:
		action = randint(1,4)
	return action


def move(direction, stateX, stateY):
	if direction == 1:		# right
		newStateX, newStateY = up(stateX, stateY)
	elif direction == 2:	# down
		newStateX, newStateY = right(stateX, stateY)
	elif direction == 3:	# left
		newStateX, newStateY = down(stateX, stateY)
	elif direction == 4:	# up
		newStateX, newStateY = left(stateX, stateY)
	else:
		newStateX = stateX
		newStateY = stateY

	return newStateX, newStateY

def agentMovement(agent, locations, rewards, prevAction, type):
	# type == 0: random policy
	# type == 1: run then left, down, right, up
	# type == 2: run then go on row/column with most rewards
	global m,n
	lock = 0
	if type == 0:
		action = randint(1,4)
	else:
		if (agent[0]+1) < n and (agent[1]+1) < m:
			if locations[agent[0]+1][agent[1]] == 8 or locations[agent[0]+1][agent[1]+1]:
				action = 4
				lock = 1
		if (agent[1]+1) < m and (agent[0]-1) > -1:
			if locations[agent[0]][agent[1]+1] == 8 or locations[agent[0]-1][agent[1]+1]:
				action = 3
				lock = 1
		if (agent[0]-1) > -1 and (agent[1]-1) > -1:
			if locations[agent[0]-1][agent[1]] == 8 or locations[agent[0]-1][agent[1]-1]:
				action = 2
				lock = 1
		if (agent[1]-1) > -1 and (agent[0]+1) < n:
			if locations[agent[0]][agent[1]-1] == 8 or locations[agent[0]+1][agent[1]-1]:
				action = 1
				lock = 1
		if lock == 0:
			if type == 1:
				action = collect(agent, rewards, prevAction)
			elif type == 2:
				action = collectRowCol(agent, rewards, prevAction)
			else:
				print("Not a policy. Reassign in code")

	agent[0], agent[1] = move(action, agent[0], agent[1])
	return agent, action

def updateWorld(locationWorld, rewardWorld, numAgents, agents):
	locationWorld = createGrid(0)
	locationWorld[agents[0][0]][agents[0][1]] = 8
	for i in range(1,len(agents)):
		locationWorld[agents[i][0]][agents[i][1]] = 6
	rewardWorld[agent1[0]][agent1[1]] = 0
	rewardWorld[agent2[0]][agent2[1]] = 0
	return locationWorld, rewardWorld


if __name__ == '__main__':
	# behaviors: try to kick, run away
	# agents: 1 protector, 2 kickers
	# state: grid world
	# action: up down left right staystill
	totalRewards = []
	record = []
	steps = []
	total = 300
	for i in range(0,total):
		world = createGrid(1)
		world[0][0] = 0
		# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in world]))
		locationWorld = createGrid(0)
		stateX = 0
		stateY = 0
		newStateX = 0
		newStateY = 0
		agent0 = [n-1,m-1]
		agent1 = [0,0]
		agent2 = [0,0]
		jointReward = 0
		numAgents = 3
		action = 0
		counter = 0
		while 1:
			# print(repr(stateX) + repr(stateY))
			stateX = newStateX
			stateY = newStateY
			# raw_input()
			agent0, action0 = agentMovement(agent0, locationWorld, world, action, 0)
			agent1, action1 = agentMovement(agent1, locationWorld, world, action, 1)
			agent2, action2 = agentMovement(agent2, locationWorld, world, action1, 1)
			tempAgent0 = world[agent0[0]][agent0[1]]
			if world[agent1[0]][agent1[1]] == 1:
				jointReward = jointReward + 1
			if world[agent2[0]][agent2[1]] == 1:
				jointReward = jointReward + 1
			agents = [agent0, agent1, agent2]
			locationWorld, world = updateWorld(locationWorld, world, numAgents, agents)
			
			# print('\n')
			# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in locationWorld]))
			# print('\n')
			# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in world]))
			counter = counter + 1

			if np.sum(world) == 0:
				# print("max = " + repr(np.sum(world)))
				# print("Game is over. Agent0 was not able to catch other agents before they collected all rewards! :)")
				steps.append(counter)
				totalRewards.append(jointReward)
				record.append(1)
				break
			elif agent0 == agent1 or agent0 == agent2:
				# locationWorld[agent0[0]][agent0[1]] = 9
				# print("Game is over. Agent0 has caught an agent! >:)")
				steps.append(counter)
				totalRewards.append(jointReward)
				record.append(0)
				break

	plt.plot(range(0,total), steps)
	plt.show()
	plt.plot(range(0,total), totalRewards)
	plt.show()
	plt.plot(range(0,total), record)
	plt.show()
	print(np.mean(steps))
	print(np.mean(totalRewards))
	print(np.mean(record)*100)


	# print('\n LOCATIONS')
	# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in locationWorld]))
	# print('\n REWRADS')
	# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in world]))


	# KTC()