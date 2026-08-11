# PARABOLIC SIMUALTOR BUILT WITH PYTHON

import math # New library for mathematical functions

v0 = float(input("\nEnter the initial velocity (m/s): ")) # Initial velocity input
angle = float(input("\nEnter the launch angle (degrees): ")) # Launch angle input
print("")

angle_rad = math.radians(angle) # Angle in rad

vx = v0 * math.cos(angle_rad) # Horitzontal speed
vy = v0 * math.sin(angle_rad) # Vertical speed

print(f"Horitzontal speed: {vx:.2f} m/s | Vertical speed: {vy:.2f} m/s\n") # We print them to see if it works