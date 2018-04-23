#!/usr/bin/env python

import math
import matplotlib.pyplot as plt
import numpy as np
from random import *
import copy

global m, n
m = 5	# y
n = 6	# x

def createGrid(value):
	global m, n
	# Creates a list containing n lists, each of m items, all set to value
	matrix = [[value for x in range(m)] for y in range(n)]
	return matrix

def createFig2(world):
	world[0][0] = 0
	world[0][1] = 0
	world[2][0] = 0
	world[2][1] = 0
	world[4][1] = 0
	world[5][1] = 0
	world[1][3] = 0
	world[2][3] = 0
	world[4][3] = 0
	world[5][3] = 0
	world[1][0] = 2
	world[3][0] = 2
	world[5][0] = 2
	world[0][2] = 2
	world[1][2] = 2
	world[3][2] = 2
	world[5][2] = 2
	world[0][4] = 2
	world[3][4] = 2
	world[5][4] = 2
	return world

def still(stateX, stateY):
	newStateX = stateX
	newStateY = stateY
	return newStateX, newStateY

def up(stateX, stateY):		# right 1
	global m
	newStateX = stateX
	newStateY = stateY +1
	if newStateY >m-1:
		newStateY = stateY
		print("Couldn't move.")
	return newStateX, newStateY

def right(stateX, stateY):	# down 2
	global n
	newStateX = stateX +1
	newStateY = stateY
	if newStateX >n-1:
		newStateX = stateX
		print("Couldn't move.")
	return newStateX, newStateY

def down(stateX, stateY):	# left 3
	newStateX = stateX
	newStateY = stateY -1
	if newStateY <0:
		newStateY = stateY
		print("Couldn't move.")
	return newStateX, newStateY

def left(stateX, stateY):	# up 4
	newStateX = stateX -1
	newStateY = stateY
	if newStateX <0:
		newStateX = stateX
		print("Couldn't move.")
	return newStateX, newStateY

def move(direction, stateX, stateY):
	if direction == 1:		# right
		newStateX, newStateY = up(stateX, stateY)
	elif direction == 2:	# down
		newStateX, newStateY = right(stateX, stateY)
	elif direction == 3:	# left
		newStateX, newStateY = down(stateX, stateY)
	elif direction == 4:	# up
		newStateX, newStateY = left(stateX, stateY)
	elif direction == 0:
		newStateX, newStateY = still(stateX, stateY)
	else:
		newStateX = stateX
		newStateY = stateY
		print("Not an action. Stayed still!")

	return newStateX, newStateY

if __name__ == '__main__':
	# behaviors: try to kick, run away
	# agents: 1 protector, 2 kickers
	# state: grid world
	# actionR: up:4, down:2, left:3, right:1, stayStill:0, clearDanger:5
	# actionH: up:4, down:2, left:3, right:1, stayStill:0, extractVictim:5
	# WORLD description: 0:can't move, 1:can move, 2:node, 3:danger, 4:victim

	world1 = createGrid(1)
	world1 = createFig2(world1)
	world2 = copy.deepcopy(world1)
	world3 = copy.deepcopy(world1)
	# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in world1]))
	# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in world2]))
	# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in world3]))
	agent1 = [1,0]	# initial location of agent1
	agent2 = [1,0]	# initial location of agent2
	agent3 = [1,0]	# initial location of agent3
	


	raw_input()
	# print(repr(agent1[0]) + repr(agent1[1]))

	# for i in range(0,total):
	# locationWorld = createGrid(0)
	# agent0 = [n-1,m-1]
	# agent2 = [0,0]
	# jointReward = 0
	# numAgents = 3
	# action = 0
	# counter = 0
	# while 1:
	# 	agent0, action0 = agentMovement(agent0, locationWorld, world, action, 0)
	# 	agent1, action1 = agentMovement(agent1, locationWorld, world, action, 1)
	# 	agent2, action2 = agentMovement(agent2, locationWorld, world, action1, 1)
	# 	tempAgent0 = world[agent0[0]][agent0[1]]
	# 	if world[agent1[0]][agent1[1]] == 1:
	# 		jointReward = jointReward + 1
	# 	if world[agent2[0]][agent2[1]] == 1:
	# 		jointReward = jointReward + 1
	# 	agents = [agent0, agent1, agent2]
	# 	locationWorld, world = updateWorld(locationWorld, world, numAgents, agents)
		
	# 	# print('\n')
	# 	# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in locationWorld]))
	# 	# print('\n')
	# 	# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in world]))
	# 	counter = counter + 1

	# 	if np.sum(world) == 0:
	# 		# print("max = " + repr(np.sum(world)))
	# 		# print("Game is over. Agent0 was not able to catch other agents before they collected all rewards! :)")
	# 		steps.append(counter)
	# 		totalRewards.append(jointReward)
	# 		record.append(1)
	# 		break
	# 	elif agent0 == agent1 or agent0 == agent2:
	# 		# locationWorld[agent0[0]][agent0[1]] = 9
	# 		# print("Game is over. Agent0 has caught an agent! >:)")
	# 		steps.append(counter)
	# 		totalRewards.append(jointReward)
	# 		record.append(0)
	# 		break

	# plt.plot(range(0,total), steps)
	# plt.show()
	# plt.plot(range(0,total), totalRewards)
	# plt.show()
	# plt.plot(range(0,total), record)
	# plt.show()
	# print(np.mean(steps))
	# print(np.mean(totalRewards))
	# print(np.mean(record)*100)


	# print('\n LOCATIONS')
	# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in locationWorld]))
	# print('\n REWRADS')
	# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in world]))


	# KTC()