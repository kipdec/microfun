from microbit import *
import radio
import random

x_bird = 0
x_wall = 0
y_bird = 0
y_wall = 0
score = -1

def wall_draw(x,y):
	while(y > 5):
		display.set_pixel(x,y,4)
		y += 1

def collision_check():
	global x_bird
	global y_bird
	global x_wall
	global y_wall
	if(x_bird == x_wall and y_bird == y_wall):
			y_bird = 5

def main():
	global x_bird
	global y_bird
	global x_wall
	global y_wall
	display.clear()
	x_bird = 0
	y_bird = 2
	x_wall = 4
	y_wall = 2
	global score
	

	scoreTime = running_time()
	speed = 1000
	score_base = 5
	while(y_bird < 5):
		
		display.set_pixel(x_bird,y_bird,9)
		display.set_pixel(x_wall,y_wall,4)
		last = running_time()
		while(running_time() - last  < speed):
			if(button_a.is_pressed() and y_bird > 0):
				display.set_pixel(x_bird,y_bird,0)
			 	y_bird -= 1
				display.set_pixel(x_bird,y_bird,9)
			sleep(100)
			collision_check()
			
		if(y_bird < 5):
			display.set_pixel(x_bird,y_bird,0)
		if(y_bird < 5):
			y_bird += 1
		display.set_pixel(x_wall,y_wall,0)
		if(x_wall > 0):
			x_wall -= 1
		else:
			x_wall = 4
			y_wall = random.randrange(5)

		

		if(running_time() - scoreTime > 1000):
			score += 1
			scoreTime = running_time()

		if(score > score_base and speed > 100):
			score_base += 10
			speed -= 100


		collision_check()

display.scroll("Press A to flap!", delay = 100)
while True:
	
	display.scroll("3 2 1 GO!", delay = 100)
	sleep(1000)
	display.clear()

	main()

	display.show(Image.SAD, delay = 100)
	sleep(2000)
	
	
	while not button_a.is_pressed():
		sleep(100)
		display.scroll("Score: ", delay = 100)
		display.scroll(str(score), delay = 100)
		display.scroll("Hold A to try again!", delay = 100)

	sleep(1000)

	score = -1
	display.clear()
