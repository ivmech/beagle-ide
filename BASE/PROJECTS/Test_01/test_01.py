#!/usr/bin/env python

from beagle import *
from time import sleep

def fnc1():
	while True:
		digitalWrite(LED1, HIGH)
		sleep(0.5)
		digitalWrite(LED1, LOW)
		sleep(0.5)

def fnc2():
	while True:
		print digitalRead(TP15).strip()
		sleep(0.1)

if __name__ == "__main__":
	fnc1()
