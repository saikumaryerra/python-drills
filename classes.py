"""
* Create a class called `Point` which has two instance variables,
`x` and `y` that represent the `x` and `y` co-ordinates respectively. 

* Initialize these instance variables in the `__init__` method

* Define a method, `distance` on `Point` which accepts another `Point` object as an argument and 
returns the distance between the two points.
"""

import math
class Point:
    def __init__(self,a,b):
    	self.x=a
    	self.y=b
    def distance(self,a_p):
    	return math.sqrt(((self.x-a_p.x)**2)+((self.y-a_p.y)**2))
