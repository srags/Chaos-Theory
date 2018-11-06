from turtle import *
from random import randint
space = Screen()
sir = Turtle()
sir.speed(0)

def midpoint(point1, vertex):
	return [(point1[0]+vertex[0])/2, (point1[1]+vertex[1])/2]


	
def iteration(vertex, point):
	sir.penup()
	pointNew = midpoint(point, vertex)
	sir.goto(pointNew)
	sir.pendown()
	sir.dot(5)
	return pointNew
		

	
def main():
    pointStart = [0, 0]
    vertex1 = [0, 200]
    vertex2 = [-200, -200]
    vertex3 = [200, -200]
    
    total = input("Welcome to the CHAOS GAME How many points do you want to plot?: ")
    
    pointNew = iteration(vertex1, pointStart)
    while total>1:
        diceRoll = randint(1,3)
        if diceRoll == 1:
            pointNew = iteration(vertex1, pointNew)
        if diceRoll == 2:
            pointNew = iteration(vertex2, pointNew)
        if diceRoll == 3:
            pointNew = iteration(vertex3, pointNew)
        total -= 1
        
    exitonclick()


main()
