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
	if world[stateX][stateY] == 2:
		world[stateX][stateY] = 6
	if world[stateX][stateY] == 1:
		world[stateX][stateY] = 6
	return newStateX, newStateY, world

def up(stateX, stateY, world):		# right 1
	global m
	newStateX = stateX
	newStateY = stateY + 1
	if newStateY > m-1:
		newStateY = stateY
		print("Couldn't move.")
	if world[stateX][stateY] == 2:
		world[stateX][stateY] = 6
	if world[stateX][stateY] == 1:
		world[stateX][stateY] = 6
	return newStateX, newStateY, world

def right(stateX, stateY, world):	# down 2
	global n
	newStateX = stateX +1
	newStateY = stateY
	if newStateX >n-1:
		newStateX = stateX
		print("Couldn't move.")
	if world[stateX][stateY] == 2:
		world[stateX][stateY] = 6
	if world[stateX][stateY] == 1:
		world[stateX][stateY] = 6
	return newStateX, newStateY, world

def down(stateX, stateY, world):	# left 3
	newStateX = stateX
	newStateY = stateY -1
	if newStateY <0:
		newStateY = stateY
		print("Couldn't move.")
	if world[stateX][stateY] == 2:
		world[stateX][stateY] = 6
	if world[stateX][stateY] == 1:
		world[stateX][stateY] = 6
	return newStateX, newStateY, world

def left(stateX, stateY, world):	# up 4
	newStateX = stateX -1
	newStateY = stateY
	if newStateX <0:
		newStateX = stateX
		print("Couldn't move.")
	if world[stateX][stateY] == 2:
		world[stateX][stateY] = 6
	if world[stateX][stateY] == 1:
		world[stateX][stateY] = 6
	return newStateX, newStateY, world

def clearDanger(stateX, stateY, world):
	temp = world[stateX][stateY]
	if temp == 5: # danger & victim
		world[stateX][stateY] = 4 # victim is left
	else: # just danger
		world[stateX][stateY] = 6 # cleared danger
	return stateX, stateY, world

def extractVictim(stateX, stateY, world):
	temp = world[stateX][stateY]
	if temp == 5: # danger & victim
		world[stateX][stateY] = 3 # danger is left
	else: # just danger
		world[stateX][stateY] = 6 # cleared victim
	return stateX, stateY, world

def doAction(direction, stateX, stateY, world):
	if direction == 1:		# right
		newStateX, newStateY, newWorld = up(stateX, stateY, world)
	elif direction == 2:	# down
		newStateX, newStateY, newWorld = right(stateX, stateY, world)
	elif direction == 3:	# left
		newStateX, newStateY, newWorld = down(stateX, stateY, world)
	elif direction == 4:	# up
		newStateX, newStateY, newWorld = left(stateX, stateY, world)
	elif direction == 0:	# stop
		newStateX, newStateY, newWorld = still(stateX, stateY, world)
	elif direction == 5:	# clear danger if robot
		newStateX, newStateY, newWorld = clearDanger(stateX, stateY, world)
	elif direction == 6:	# extract victim if human
		newStateX, newStateY, newWorld = extractVictim(stateX,stateY, world)
	else:
		newStateX = stateX
		newStateY = stateY
		newWorld = world
		print("Not an action. Stayed still!")

	return newStateX, newStateY, newWorld

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

def calcRewards(state, action, statePrime, agentType):
	rewards = 0
	# agent is a human
	if state == 1 and statePrime == 1 and agentType == 0:
		rewards = -1
	if state == 1 and statePrime == 2 and agentType == 0:
		rewards = -1
	if state == 1 and statePrime == 3 and agentType == 0:
		rewards = -50
	if state == 1 and statePrime == 4 and agentType == 0:
		rewards = -1
	if state == 1 and statePrime == 5 and agentType == 0:
		rewards = -50
	if state == 2 and statePrime == 1 and agentType == 0:
		rewards = -1
	if state == 2 and statePrime == 2 and agentType == 0:
		rewards = -1
	if state == 2 and statePrime == 3 and agentType == 0:
		rewards = -50
	if state == 2 and statePrime == 4 and agentType == 0:
		rewards = -1
	if state == 2 and statePrime == 5 and agentType == 0:
		rewards = -50
	if state == 3 and statePrime == 1 and agentType == 0:
		rewards = -1
	if state == 3 and statePrime == 2 and agentType == 0:
		rewards = -1
	if state == 3 and statePrime == 3 and agentType == 0:
		rewards = -50
	if state == 3 and statePrime == 4 and agentType == 0:
		rewards = -1
	if state == 3 and statePrime == 5 and agentType == 0:
		rewards = -50
	if state == 4 and statePrime == 1 and agentType == 0:
		rewards = -1
	if state == 4 and statePrime == 2 and agentType == 0:
		rewards = 100
	if state == 4 and statePrime == 3 and agentType == 0:
		rewards = -50
	if state == 4 and statePrime == 4 and agentType == 0:
		rewards = -1
	if state == 4 and statePrime == 5 and agentType == 0:
		rewards = -50
	if state == 5 and statePrime == 1 and agentType == 0:
		rewards = -1
	if state == 5 and statePrime == 2 and agentType == 0:
		rewards = 100
	if state == 5 and statePrime == 3 and agentType == 0:
		rewards = -50
	if state == 5 and statePrime == 4 and agentType == 0:
		rewards = -1
	if state == 5 and statePrime == 5 and agentType == 0:
		rewards = -50
	# agent is a robot
	if state == 1 and statePrime == 1 and agentType == 1:
		rewards = -1
	if state == 1 and statePrime == 2 and agentType == 1:
		rewards = -1
	if state == 1 and statePrime == 3 and agentType == 1:
		rewards = -1
	if state == 1 and statePrime == 4 and agentType == 1:
		rewards = -1
	if state == 1 and statePrime == 5 and agentType == 1:
		rewards = -1
	if state == 2 and statePrime == 1 and agentType == 1:
		rewards = -1
	if state == 2 and statePrime == 2 and agentType == 1:
		rewards = -1
	if state == 2 and statePrime == 3 and agentType == 1:
		rewards = -1
	if state == 2 and statePrime == 4 and agentType == 1:
		rewards = -1
	if state == 2 and statePrime == 5 and agentType == 1:
		rewards = -1
	if state == 3 and statePrime == 1 and agentType == 1:
		rewards = -1
	if state == 3 and statePrime == 2 and agentType == 1:
		rewards = 50
	if state == 3 and statePrime == 3 and agentType == 1:
		rewards = -1
	if state == 3 and statePrime == 4 and agentType == 1:
		rewards = -1
	if state == 3 and statePrime == 5 and agentType == 1:
		rewards = -1
	if state == 4 and statePrime == 1 and agentType == 1:
		rewards = -1
	if state == 4 and statePrime == 2 and agentType == 0:
		rewards = -1
	if state == 4 and statePrime == 3 and agentType == 1:
		rewards = -1
	if state == 4 and statePrime == 4 and agentType == 1:
		rewards = -1
	if state == 4 and statePrime == 5 and agentType == 1:
		rewards = -1
	if state == 5 and statePrime == 1 and agentType == 1:
		rewards = -1
	if state == 5 and statePrime == 2 and agentType == 1:
		rewards = 50
	if state == 5 and statePrime == 3 and agentType == 1:
		rewards = -1
	if state == 5 and statePrime == 4 and agentType == 1:
		rewards = 50
	if state == 5 and statePrime == 5 and agentType == 1:
		rewards = -1
	return rewards

def finished(world):
	finsh = []
	finish.append((1 in world))
	finish.append((2 in world))
	finish.append((3 in world))
	finish.append((4 in world))
	finish.append((5 in world))
	if finish[:] == False:
		done = 1
	else:
		done = 0
	return done


if __name__ == '__main__':
	# state: grid world
	# actionR: up:4, down:2, left:3, right:1, stayStill:0, clearDanger:5
	# actionH: up:4, down:2, left:3, right:1, stayStill:0, extractVictim:6
	# WORLD description: 0:can't move, 1:can move, 2:node, 3:danger, 4:victim, 5:danger & victim, 6: visited and cleared (also a node)
	# agent = [x,y,agentType] agentType 0 = human; agentType 1 = robot

	# Initialize Worlds and Agents
	world1 = createGrid(1)	# create worlds
	world1 = createFig2(world1)
	world2 = copy.deepcopy(world1)
	world3 = copy.deepcopy(world1)
	# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in world1]))
	# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in world2]))
	# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in world3]))
	agent1 = [3,3,0]	# initial location of agents (x,y,type)
	agent2 = [1,0,1]
	agent3 = [1,0,1]
	SAS1 = [0,0,0]	# keep track of state action state' for rewards
	SAS2 = [0,0,0]
	SAS3 = [0,0,0]
	totRewards = 0
	user_input = "N"
	while True:
		if user_input == "y":
			break
		else:
			# check possible movements
			possibleMovement1 = findPossibleMovement(agent1[0], agent1[1], world1) # returns list [still, right, down, left, up]
			# check possible movements

			SAS1[1] = possibleMovement1[0] # current state
			observation = possibleMovement1[0] # Collect Observation

			print(repr(SAS1[1]))
			# get action
			temp = 0
			if observation == 4: # victim is present
				if agent1[2] == 0: # agent is a human
					SAS1[1] = 6
				else: # agent is a robot
					if 6 in possibleMovement1:
						temp = np.where(possibleMovement1 == 6)[0] # already visited node
						randTemp = random.randint(0,len(temp))
						SAS1[1] = randTemp
					if 1 in possibleMovement1:
						temp = possibleMovement1.index(1) # movement node
						SAS1[1] = temp
					if 2 in possibleMovement1:
						temp = possibleMovement1.index(2) # node that hasn't been visited
						SAS1[1] = temp
					if 3 in possibleMovement1:
						temp = possibleMovement1.index(3) # if there is a danger node next to me
						SAS1[1] = temp
					if 5 in possibleMovement1:
						temp = possibleMovement1.index(5) # if there is a danger & victim node next to me
						SAS1[1] = temp

			elif observation == 3: # danger is present
				if agent1[2] == 1: # agent is a robot
					SAS1[1] = 5
				else: # agent is a human
					if 6 in possibleMovement1:
						temp = np.where(possibleMovement1 == 6)[0] # already visited node
						randTemp = random.randint(0,len(temp))
						SAS1[1] = randTemp
					if 1 in possibleMovement1:
						temp = possibleMovement1.index(1) # movement node
						SAS1[1] = temp
					if 2 in possibleMovement1:
						temp = possibleMovement1.index(2) # node that hasn't been visited
						SAS1[1] = temp
					if 4 in possibleMovement1:
						temp = possibleMovement1.index(4) # if there is a victim only node next to me
						SAS1[1] = temp

			elif observation == 5: # danger & victim are present
				if agent1[2] == 0: # agent is a human
					SAS1[1] = 6 # extract victim
				else: # agent is a robot
					SAS1[1] = 5 # clear danger
			
			else:
				if agent1[2] == 1: # agent is a robot
					if 6 in possibleMovement1:
						temp = np.where(possibleMovement1 == 6)[0] # already visited node
						randTemp = random.randint(0,len(temp))
						SAS1[1] = randTemp
					if 1 in possibleMovement1:
						temp = possibleMovement1.index(1) # movement node
						SAS1[1] = temp
					if 2 in possibleMovement1:
						temp = possibleMovement1.index(2) # node that hasn't been visited
						SAS1[1] = temp
					if 3 in possibleMovement1:
						temp = possibleMovement1.index(3) # if there is a danger node next to me
						SAS1[1] = temp
					if 5 in possibleMovement1:
						temp = possibleMovement1.index(5) # if there is a danger node next to me
						SAS1[1] = temp
				else: # agent is a human
					if 6 in possibleMovement1:
						print("1")
						temp = np.where(possibleMovement1 == 6)[0] # already visited node
						randTemp = random.randint(0,len(temp))
						SAS1[1] = randTemp
					if 1 in possibleMovement1:
						print("2")
						temp = possibleMovement1.index(1) # movement node
						SAS1[1] = temp
					if 2 in possibleMovement1:
						print("3")
						temp = possibleMovement1.index(2) # node that hasn't been visited
						SAS1[1] = temp
					if 4 in possibleMovement1:
						print("4")
						temp = possibleMovement1.index(4) # if there is a victim only node next to me
						SAS1[1] = temp
			# get action
			# TODO: figure out how to not get stuck in a state because of 6
			# TODO: add multiple agents
			# TODO: make robots do the opposite action of humans if possible

			# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in world1]))
			print("(x, y, action): " + repr(agent1[0]) + " " + repr(agent1[1]) + " " + repr(SAS1[1]))
			agent1[0], agent1[1], world1[:] = doAction(SAS1[1], agent1[0], agent1[1], world1) # doing action
			# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in world1]))

			tempMovements = findPossibleMovement(agent1[0], agent1[1], world1) # getting next state
			SAS1[2] = tempMovements[0] # saving next state
			rewards = calcRewards(SAS1[0], SAS1[1], SAS1[2], agent1[2]) # getting instantaneous rewards
			totRewards = totRewards + rewards # calculating total rewards
			
			print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in world1]))

			user_input = raw_input("exit? [y/N]")

			doneFlag = finished(world1)
			if doneFlag == 1:
				user_input == "y"


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