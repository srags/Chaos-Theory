from turtle import *
from random import randint
space = Screen()
sir = Turtle()
sir.speed(0)

def rotation(point1, vertex):
	return [(3*vertex[0]/2 - point1[0]/2), (3*vertex[1]/2 - point1[1]/2)]


	
def iteration(vertex, point):
	sir.penup()
	pointNew = rotation(point, vertex)
	sir.goto(pointNew)
	sir.pendown()
	sir.dot(5)
	return pointNew
		

	
def main():
	pointStart = [0, 0]
	vertex1 = [0, 100]
	vertex2 = [-100, -100]
	vertex3 = [100, -100]
	counter = 0
	total = input("How many points? Please enter a positive number: ")
	pointNew = iteration(vertex1, pointStart)	
	while total > 1:
		diceRoll = randint(1, 3)
        if diceRoll ==1:
            sir.color("cyan")
            pointNew = iteration(vertex1, pointNew)
        if diceRoll ==2:
            sir.color("cyan")
            pointNew = iteration(vertex2, pointNew)
        if diceRoll ==3:
            sir.color("cyan")
            pointNew = iteration(vertex3, pointNew)
        total -= 1
        counter += 1
        if counter % 200 ==0:
            print counter
    print counter + 1
            
	
main()