#!/usr/bin/env python

import math
import matplotlib.pyplot as plt
import mdptoolbox.example


def main():
	P, R = mdptoolbox.example.forest()
	vi = mdptoolbox.mdp.ValueIteration(P, R, 0.9)
	vi.run()
	vi.policy # result is (0, 0, 0)


if __name__ == '__main__':
	main()