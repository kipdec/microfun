from microbit import *
import random 

coins =["Heads","Tails"]

die1 = Image("09990:"
	         "99999:"
	         "90009:"
	         "90009:"
	         "09990:")

die2 = Image("09990:"
	         "90009:"
	         "99999:"
	         "90009:"
	         "09990:")
die3 = Image("09990:"
	         "90009:"
	         "90009:"
	         "99999:"
	         "09990:")
all_die = [die1,die2,die3,die1,die2,die3]

def coin():
	if accelerometer.was_gesture("shake"):
		random.seed(running_time())
		display.show(all_die, delay = 100)
		display.clear()
		sleep(200)
		display.scroll(str(random.choice(coins)), wait=False, loop = True)

def roller(n):
	global all_die
	if accelerometer.was_gesture("shake"):
		random.seed(running_time())
		display.show(all_die, delay = 100)
		display.clear()
		sleep(200)
		display.scroll(str(random.randrange(1, n)), wait=False, loop = True)
	

def rollPerc():
	global all_die
	if accelerometer.was_gesture("shake"):
		random.seed(running_time())
		display.show(all_die, delay = 100)
		display.clear()
		sleep(200)
		display.scroll(str(random.randrange(1, 11) * 10), wait=False, loop = True)
	

def main():
	n = 0
	while True:
		if(n==0):
			display.scroll("Coin", wait=False, loop=True)
			while not button_a.is_pressed() and not button_b.is_pressed():
				
				coin()
				if button_a.is_pressed():
					n -= 1
				if button_b.is_pressed():
					n += 1
		elif(n==1):
			display.scroll("D4", wait=False, loop=True)
			while not button_a.is_pressed() and not button_b.is_pressed():

				roller(5)
				if button_a.is_pressed():
					n -= 1
				if button_b.is_pressed():
					n += 1
		elif(n==2):
			display.scroll("D6", wait=False, loop=True)
			while not button_a.is_pressed() and not button_b.is_pressed():
				roller(7)
				if button_a.is_pressed():
					n -= 1
				if button_b.is_pressed():
					n += 1
		elif(n==3):
			display.scroll("D8", wait=False, loop=True)
			while not button_a.is_pressed() and not button_b.is_pressed():
				roller(9)
				if button_a.is_pressed():
					n -= 1
				if button_b.is_pressed():
					n += 1
		elif(n==4):
			display.scroll("D10", wait=False, loop=True)
			while not button_a.is_pressed() and not button_b.is_pressed():
				roller(11)
				if button_a.is_pressed():
					n -= 1
				if button_b.is_pressed():
					n += 1
		elif(n==5):
			display.scroll("D12", wait=False, loop=True)
			while not button_a.is_pressed() and not button_b.is_pressed():
				roller(13)
				if button_a.is_pressed():
					n -= 1
				if button_b.is_pressed():
					n += 1
		elif(n==6):
			display.scroll("D20", wait=False, loop=True)
			while not button_a.is_pressed() and not button_b.is_pressed():
				roller(21)
				if button_a.is_pressed():
					n -= 1
				if button_b.is_pressed():
					n += 1
		elif(n==7):
			display.scroll("D00", wait=False, loop=True)
			while not button_a.is_pressed() and not button_b.is_pressed():
				rollPerc()
				if button_a.is_pressed():
					n -= 1
				if button_b.is_pressed():
					n += 1
		elif(n > 7):
			n = 0
		elif(n < 0):
			n = 7
		else:
			n = 0

while True:
	main()
