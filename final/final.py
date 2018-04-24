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

def still(stateX, stateY, world):
	newStateX = stateX
	newStateY = stateY
	return newStateX, newStateY

def up(stateX, stateY, world):		# right 1
	global m
	newStateX = stateX
	newStateY = stateY +1
	if newStateY >m-1:
		newStateY = stateY
		print("Couldn't move.")
	return newStateX, newStateY

def right(stateX, stateY, world):	# down 2
	global n
	newStateX = stateX +1
	newStateY = stateY
	if newStateX >n-1:
		newStateX = stateX
		print("Couldn't move.")
	return newStateX, newStateY

def down(stateX, stateY, world):	# left 3
	newStateX = stateX
	newStateY = stateY -1
	if newStateY <0:
		newStateY = stateY
		print("Couldn't move.")
	return newStateX, newStateY

def left(stateX, stateY, world):	# up 4
	newStateX = stateX -1
	newStateY = stateY
	if newStateX <0:
		newStateX = stateX
		print("Couldn't move.")
	return newStateX, newStateY

# def clearDanger(stateX, stateY, world):

# def extractVictim(stateX, stateY, world):

def doAction(direction, stateX, stateY, world):
	if direction == 1:		# right
		newStateX, newStateY = up(stateX, stateY, world)
	elif direction == 2:	# down
		newStateX, newStateY = right(stateX, stateY, world)
	elif direction == 3:	# left
		newStateX, newStateY = down(stateX, stateY, world)
	elif direction == 4:	# up
		newStateX, newStateY = left(stateX, stateY, world)
	elif direction == 0:
		newStateX, newStateY = still(stateX, stateY, world)
	elif direction == 5:
		newStateX, newStateY = clearDanger(stateX, stateY, world)
	elif direction == 6:
		newStateX, newStateY = extractVictim(stateX,stateY, world)
	else:
		newStateX = stateX
		newStateY = stateY
		print("Not an action. Stayed still!")

	return newStateX, newStateY

def findPossibleMovement(stateX, stateY, world):
	global m, n
	actions = []
	index1 = stateY+1
	index2 = stateX+1
	index3 = stateY-1
	index4 = stateX-1
	
	actions.append(world[stateX][stateY]) # check current location
	if (0 <= index1) and (index1 < m):
		actions.append(world[stateX][stateY+1])	# check right
	else:
		actions.append(-1)
	if (0 <= index2) and (index2 < n):
		actions.append(world[stateX+1][stateY]) # check down
	else:
		actions.append(-1)
	if (0 <= index3) and (index3 < m):
		actions.append(world[stateX][stateY-1]) # check left
	else:
		actions.append(-1)
	if (0 <= index4) and (index4 < n):
		actions.append(world[stateX-1][stateY]) # check up
	else:
		actions.append(-1)
	return actions


if __name__ == '__main__':
	# state: grid world
	# actionR: up:4, down:2, left:3, right:1, stayStill:0, clearDanger:5
	# actionH: up:4, down:2, left:3, right:1, stayStill:0, extractVictim:6
	# WORLD description: 0:can't move, 1:can move, 2:node, 3:danger, 4:victim, 5:danger & victim

	# Initialize Worlds and Agents
	world1 = createGrid(1)	# create worlds
	world1 = createFig2(world1)
	world2 = copy.deepcopy(world1)
	world3 = copy.deepcopy(world1)
	# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in world1]))
	# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in world2]))
	# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in world3]))
	agent1 = [3,3]	# initial location of agents
	agent2 = [1,0]
	agent3 = [1,0]
	SAS1 = [0,0,0]	# keep track of state action state' for rewards
	SAS2 = [0,0,0]
	SAS3 = [0,0,0]

	# Check Possible Movements
	possibleMovement1 = findPossibleMovement(agent1[0], agent1[1], world1) # returns list [still, right, down, left, up]

	SAS1[0] = possibleMovement1[0]

	# Collect Observation
	observationTemp = findPossibleMovement(agent1[0], agent1[1], world1)
	observation = observationTemp[0]

	# TODO: take an action
	if observation == 4:
		action = 6
	elif observation == 3:
		action = 5
	elif observation == 5:
		action = 5 & 6 # TODO: fix this for both depending on agent
	else:

	SAS1[1] = # TODO: place action in here


	raw_input()

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