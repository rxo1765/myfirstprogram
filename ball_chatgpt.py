# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 19:01:05 2023

@author: be
"""

import math
def calculate_max_height(v):
    theta = 90  # angle of projection (straight up)
    g = 32.2  # acceleration due to gravity in feet per second squared

    # Convert theta to radians
    theta_rad = math.radians(theta)

    # Calculate the maximum height
    h = (v**2 * math.sin(theta_rad)**2) / (2 * g)

    return h

# Initial velocity of 50 feet per second
initial_velocity = 50
max_height = calculate_max_height(initial_velocity)

print(f"The maximum height reached by the ball is {max_height} feet.")
