#!/usr/bin/env python3
#Author: Ched Duloy
#Author ID: 185662210
#Date Created: 2024/05/23

import sys

if len(sys.argv) == 2:
	timer = int(sys.argv[1])
else:

	timer = 3

while timer > 0:
	print(timer)
	timer -= 1

print("blast off!")

