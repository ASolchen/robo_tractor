#!/usr/bin/env python
# coding: utf-8

# Load the gamepad and time libraries
import Gamepad
import time

# Gamepad settings
gamepadType = Gamepad.PS4


# Wait for a connection
if not Gamepad.available():
    print('Please connect your gamepad...')
    while not Gamepad.available():
        time.sleep(1.0)
gamepad = gamepadType()
print('Gamepad connected')

# Set some initial state
speed = 0.0
steering = 0.0

btn_dict = {}

# Handle joystick updates one at a time
gamepad.startBackgroundUpdates()
while gamepad.isConnected():
    for axisname in gamepad.axisIndex:
        btn_dict[axisname] = gamepad.axis(axisname)
    for btn_name in gamepad.buttonIndex:
        btn_dict[btn_name] = gamepad.isPressed(btn_name)
    print(btn_dict)
    time.sleep(0.2)