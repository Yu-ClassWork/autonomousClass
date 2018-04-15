#!/usr/bin/env python

import math
import matplotlib.pyplot as plt
import numpy as np
from random import *

global m, n
m = 5
n = 3

# def KTC(): # Kick the Can Game


def createGrid(value):
	global m, n
	# Creates a list containing n lists, each of m items, all set to 0
	matrix = [[value for x in range(m)] for y in range(n)]
	return matrix

def up(stateX, stateY):
	# print("up")
	global n
	newStateX = stateX
	newStateY = stateY +1
	if newStateY >m-1:
		newStateY = stateY
	return newStateX, newStateY

def right(stateX, stateY):
	# print("right")
	global m
	newStateX = stateX +1
	newStateY = stateY
	if newStateX >n-1:
		newStateX = stateX
	return newStateX, newStateY

def down(stateX, stateY):
	# print("down")
	newStateX = stateX
	newStateY = stateY -1
	if newStateY <0:
		newStateY = stateY
	return newStateX, newStateY

def left(stateX, stateY):
	# print("left")
	newStateX = stateX -1
	newStateY = stateY
	if newStateX <0:
		newStateX = stateX
	return newStateX, newStateY

def collect(agent, rewrads):
	if rewrads[agent0[0]+1][agent0[1]] == 1:
		action = 4
	elif rewrads[agent0[0]][agent0[1]+1] == 1:
		action = 3
	elif rewrads[agent0[0]-1][agent0[1]] == 1:
		action = 2
	elif rewrads[agent0[0]][agent0[1]-1] == 1:
		action = 1
	else:
		action = randint(1,4)
	return action


def move(direction, stateX, stateY):
	if direction == 1:
		newStateX, newStateY = up(stateX, stateY)
	elif direction == 2:
		newStateX, newStateY = right(stateX, stateY)
	elif direction == 3:
		newStateX, newStateY = down(stateX, stateY)
	elif direction == 4:
		newStateX, newStateY = left(stateX, stateY)
	else:
		newStateX = stateX
		newStateY = stateY
		print("STAYING STILL ")

	return newStateX, newStateY

def agentMovement(agent, locations, rewards, type):
	if type == 0:
		action = randint(1,4)
	else:
		if locations[agent0[0]+1][agent0[1]] == 8:
			action = 4
		elif locations[agent0[0]][agent0[1]+1] == 8:
			action = 3
		elif locations[agent0[0]-1][agent0[1]] == 8:
			action = 2
		elif locations[agent0[0]][agent0[1]-1] == 8:
			action = 1
		else:
			action = collect(agent, rewards)

	agent[0], agent[1] = move(action, agent[0], agent[1])
	return agent

def updateWorld(locationWorld, rewardWorld, numAgents, agents):
	locationWorld = createGrid(0)
	locationWorld[agent0[0]][agent0[1]] = 8
	locationWorld[agent1[0]][agent1[1]] = 6
	locationWorld[agent2[0]][agent2[1]] = 6
	rewardWorld[agent0[0]][agent0[1]] = 0
	rewardWorld[agent1[0]][agent1[1]] = 0
	rewardWorld[agent2[0]][agent2[1]] = 0
	return locationWorld, rewardWorld


if __name__ == '__main__':
	global m, n
	# behaviors: try to kick, run away
	# agents: 1 protector, 2 kickers
	# state: grid world
	# action: up down left right staystill
	world = createGrid(1)
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in world]))
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
	while 1:
		# print(repr(stateX) + repr(stateY))
		stateX = newStateX
		stateY = newStateY
		# raw_input()
		agent0 = agentMovement(agent0, locationWorld, world, 0)
		agent1 = agentMovement(agent1, locationWorld, world, 1)
		agent2 = agentMovement(agent2, locationWorld, world, 1)
		tempAgent0 = world[agent0[0]][agent0[1]]
		if world[agent1[0]][agent1[1]] == 1:
			jointReward = jointReward + 1
		if world[agent2[0]][agent2[1]] == 1:
			jointReward = jointReward + 1
		agents = [agent0, agent1, agent2]
		locationWorld, world = updateWorld(locationWorld, world, numAgents, agents)
		
		print('\n')
		print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in locationWorld]))
		print('\n')
		print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in world]))


		if np.sum(world) == 0:
			print("max = " + repr(np.sum(world)))
			print("Game is over. Agent0 was not able to catch other agents before they collected all rewards! :)")
			break
		elif agent0 == agent1 or agent0 == agent2:
			locationWorld[agent0[0]][agent0[1]] = 9
			print("Game is over. Agent0 has caught an agent! >:)")
			break



	print('\n LOCATIONS')
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in locationWorld]))
	print('\n REWRADS')
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in world]))


	# KTC()