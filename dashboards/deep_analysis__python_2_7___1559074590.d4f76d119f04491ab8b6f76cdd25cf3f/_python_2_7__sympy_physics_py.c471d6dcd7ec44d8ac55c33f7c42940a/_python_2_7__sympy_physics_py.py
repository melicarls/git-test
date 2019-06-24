# taken from http://docs.sympy.org/latest/modules/physics/units/examples.html

from sympy import symbols
from sympy.physics.units import length, mass, acceleration, force
from sympy.physics.units import gravitational_constant as G
F = mass*acceleration
print(F.get_dimensional_dependencies())

# expect-output-to-have: 'length': 1
# expect-output-to-have: 'mass': 1
# expect-output-to-have: 'time': -2
