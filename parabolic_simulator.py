# PARABOLIC SIMUALTOR BUILT WITH PYTHON


# We need gravity constant, and both sinus and cosinus
from scipy.constants import g # We'll only need g, so doing it with that it's faster
import math # New library for mathematical functions


# We need the initial velocity and its angle
while True:
    v0 = float(input("\nEnter the initial velocity (m/s): ")) # Initial velocity input

    if v0 < 0 or v0 > 3e8:
        print("The initial velocity must be between 0 and 300.000.000 m/s!\n")

    else:
        angle = float(input("\nEnter the launch angle (degrees): ")) # Launch angle input

        if angle < 0 or angle > 90:
            print("The angle must be between 0 and 90 degrees!\n")

        else:
            print("")
            angle_rad = math.radians(angle) # Angle in rad


            # This speed has two components
            vx = v0 * math.cos(angle_rad) # Horizontal speed
            vy = v0 * math.sin(angle_rad) # Vertical speed


            # Then we print the results
            print(f"--- PROJECTILE STATS ---\nHorizontal speed: {vx:.2f} m/s | Vertical speed: {vy:.2f} m/s\n") # We print them to see if it works


            # Now we calculate the total flight time
            f_time = 2 * vy / g # [s]
            print(f"Total flight time: {f_time:.2f} s\n")


            # We need both max height and horizontal range too
            max_height = (vy ** 2) / (2 * g)
            horizontal_range = vx * f_time


            # We print those results
            print(f"Max height: {max_height:.2f} m\n")
            print(f"Horizontal range: {horizontal_range:.2f} m\n")


            # We need to close the loop
            answer = input("Do you want to create another projectile (yes/no)? ").lower().strip()

            if answer == "yes":
                continue

            elif answer == "no":
                break

            else:
                print(answer)