# -*- coding: utf-8 -*-
"""
The program should print two roots of the quadratic equation of the form

a x² + b x + c = 0

The roots must be stored in a tuple named 'solutions' and printed at the very end of the program.
"""

# This is sample input data

a = 1
b = 3
c = 2

# This is a tuple for results. You should override it with actual results

solutions = ()

# DO NOT CHANGE ANYTHING ABOVE THIS LINE!!!
if a == 0:
    xx =((-c)/b,)
else:
   delta = b**2 - 4*a*c
   if delta == 0:
       xx = (-b/(2*a),)
   elif delta > 0:
      x1 = (-b+delta**(1/2))/(2*a)
      x2 = (-b-delta**(1/2))/(2*a)
      xx = (x2,x1,)


# Put your here...




# At the end, the results are printed to the screen
print(*solutions)
