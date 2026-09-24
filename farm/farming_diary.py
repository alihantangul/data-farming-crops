"""
Module: farming_diary
This script simulates a farming diary where different crops (corn and rice) are grown, watered,
and checked for ripeness.
"""

from farm.corn import Corn
from farm.rice import Rice



print('\n\n Day One: Corn')

# 1.1 Instantiate a corn crop
corn = Corn()

# 1.2 Water the corn crop
corn.water()

# 1.3 Print "The corn crop produced ## grains"
print(f"The corn crop produced {corn.grains} grains")


# 1.4 Print "The corn crop is ripe" or "The corn crop is not ripe"
print(f"The corn crop is {'' if corn.ripe() else 'not '}ripe")


print('\n\n 📄 Day Two: Rice')
# 2. Water the corn crop

# 2.1 Instantiate a rice crop
rice = Rice()

# 2.2 Water the rice crop
rice.water()

# 2.3 Transplant the rice crop
rice.transplant()

# 2.4 Print "The rice crop produced ## grains"
print(f"The rice crop produced {rice.grains} grains")

# 2.5 Print "The rice crop is ripe" or "The rice crop is not ripe"
print(f"The rice crop is {'' if rice.ripe() else 'not '}ripe")



# 3. Print "The corn crop produced ## grains"


# 4. Print "The corn crop is ripe" or "The corn crop is not ripe"

print("\n\n📝 Day Two: Rice")

# 1. Instantiate a rice crop


# 2. Water the rice crop


# 3. Transplant the rice crop


# 4. Print "The rice crop produced ## grains"


# 5. Print "The rice crop is ripe" or "The rice crop is not ripe"
