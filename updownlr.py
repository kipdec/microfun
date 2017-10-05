from microbit import *

x = 2
y = 2
while True:
	display.set_pixel(x,y,9)
	sleep(100)
	display.set_pixel(x,y,0)
	if(button_a.is_pressed() and x > 0):
		x -= 1
	if(button_b.is_pressed() and x < 4):
		x += 1
	if(pin0.is_touched() and y > 0):
		y -= 1
	if(pin1.is_touched() and y < 4):
		y += 1

	