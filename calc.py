# Vehicle: Tesla Model 3 Long Range
# Conditions: Ordinary passenger car tires on smooth, dry asphalt on a flat surface
import math

mass_kg = 1847  # Curb weight (~1847 kg)
gravity = 9.81  # m/s^2
c_rr = 0.011  # Typical rolling resistance coefficient for standard radial tires on smooth asphalt
A = 2
rho = 1.2
v = 35
cD = 0.25
Rw = 0.3

# Normal force on a flat road: N = m * g
normal_force = mass_kg * gravity

# Variable "a" gives back the rolling resistance force in Newtons (N)
a = c_rr * normal_force

#Calculating drag force

F_d = 0.5 * v^2 * rho * A * cD

# wheel RPM calculation

n_wheel = v/Rw * 60 / (2 * math.pi)