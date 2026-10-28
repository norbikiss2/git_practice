# Vehicle: Tesla Model 3 Long Range
# Conditions: Ordinary passenger car tires on smooth, dry asphalt on a flat surface

mass_kg = 1847  # Curb weight (~1847 kg)
gravity = 9.81  # m/s^2
c_rr = 0.011  # Typical rolling resistance coefficient for standard radial tires on smooth asphalt

# Normal force on a flat road: N = m * g
normal_force = mass_kg * gravity

# Variable "a" gives back the rolling resistance force in Newtons (N)
a = c_rr * normal_force



