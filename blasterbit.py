from microbit import *

x = 2
y = 4


def bullet():
	global x
	global y
	bullet_x = x
	bullet_y = y
	count = 0
	display.set_pixel(bullet_x,bullet_y,4)
	while bullet_y > 0:
		if bullet_y != y:
			display.set_pixel(bullet_x,bullet_y,0)
		else:
			display.set_pixel(bullet_x,bullet_y,9)
		bullet_y -= 1
		display.set_pixel(bullet_x,bullet_y,4)
		sleep(100)
	display.set_pixel(bullet_x,bullet_y,0)

def main():
	global x
	global y
	display.set_pixel(x,y,9)
	sleep(100)
	if(button_a.is_pressed() and x >= 0):
		display.set_pixel(x,y,0)
		x -= 1
		
	if(button_a.is_pressed() and x == -1):
		x = 4

	if(button_b.is_pressed()):
		bullet()
	sleep(50)

while True:
	main()
	