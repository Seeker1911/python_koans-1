#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    tri_side =  sorted([a,b,c])
    ### Why does 2 need to be the iterable compared? 0 > 1 + 2 does not work.
    if tri_side[2] > tri_side[1] + tri_side[0] : raise TriangleError('The sum of the side lengths of any 2 sides of a triangle must exceed the length of the third side')

    if tri_side[0] <= 0 : raise TriangleError('Sides cannot be 0 or less')

    #if tri_side[0] < tri_side

    if a == b == c:
        print('equilateral')
        return 'equilateral'
    elif a == b or a == c or b == c:
        print('isosceles') 
        return 'isosceles'
    else: 
        print('scalene')
        return 'scalene'
            
triangle(1,1,1)

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
