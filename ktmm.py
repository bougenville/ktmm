"""
Name:		ktmm
Brief:		'Keep That Mouse Moving'
Description:	Stops a computer from going into IDLE mode
Created by:	Andrew Odendaal (https://github.com/ao/ktmm)
"""

from pynput.mouse import Controller
import time

def now():
	t = time.localtime()
	current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
	print(current_time, '\n-------------------')

if __name__ == '__main__':
	mouse = Controller()
	while True:
		now()		
		mouse.move(0.1, 0.1)
		time.sleep(10)
		mouse.move(-0.1, -0.1)
		time.sleep(10)

	# Oh damn, that was simple!
