#a program to find the hypotenus of a triangle using a pythagoras thorem
import  math as m
#formula for pythagoras theorem is a^2=b^2+c^2
dimensions={
    "adjacent":25,
    "opposite":30
}

def pythagoras_theorem(opposite, adjacent):
    square_of_the_opposite_side = opposite ** 2
    square_of_the_adjacent_side = adjacent ** 2
    hypotenus_squared = square_of_the_adjacent_side + square_of_the_opposite_side
    hypotenus = m.sqrt(hypotenus_squared)
    print("the hypotenus of the triangle is:", round(hypotenus,2)) if hypotenus > 0 else print(0)
pythagoras_theorem(dimensions["opposite"],dimensions["adjacent"] )
