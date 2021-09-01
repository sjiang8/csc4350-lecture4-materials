# ASSIGNMENT: The below is a common design pattern that can be cleaned up.
# We have a lengthy mathematical operation that uses a few pieces of
# information several times in order to mutate a value. This code organization
# isn't inherently wrong, but it does result in some pretty messy callsites,
# especially once we introduce nested function calls in compound_op_it().
# 
# The goal of this assignment is to refactor the below into a class: 
# 1) Shared arguments between functions should become instance variables of the class
# in order to minimize clutter (because now they won't have to be arguments
# to each function). 
# 2) The class should have a function self.complicated_math_operation()
# that accomplishes everything complicated_math_operation() currently does.
# 3) There's a design decision lurking in here! Should we make the starting_value
# an instance variable of the class that each function call mutates, or should we
# keep the current structure where complicated_math_operation() accepts a starting value
# and repeatedly mutates it? Leave a comment explaining which one you chose
# and under what circumstances that might make sense. There's no right answer! 

import math

def complicated_math_operation(starting_value, min_value, max_value, coefficient):
    res = starting_value
    res = multiply_it(res, min_value, max_value, coefficient)
    res = add_it(res, min_value, max_value, coefficient)
    res = sqrt_it(res, min_value, max_value, coefficient)
    res = compound_op_it(res, min_value, max_value, coefficient)
    return res

def multiply_it(starting_value, min_value, max_value, coefficient):
    return max(min_value, min(max_value, starting_value * coefficient))

def add_it(starting_value, min_value, max_value, coefficient):
    return max(min_value, min(max_value, starting_value + coefficient))
 
def sqrt_it(starting_value, min_value, max_value, coefficient):
    return max(min_value, min(max_value, math.pow(starting_value, -coefficient)))

def compound_op_it(starting_value, min_value, max_value, coefficient):
    return add_it(
        multiply_it(starting_value, min_value, max_value, coefficient),
        min_value,
        max_value,
        coefficient
    )


    