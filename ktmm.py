"""
Name:		ktmm
Brief:		'Keep That Mouse Moving'
Description:	Stops a computer from going into IDLE mode
Created by:	Andrew Odendaal (https://github.com/ao/ktmm)
"""

from pynput.mouse import Controller
import time

if __name__ == '__main__':
	mouse = Controller()
	while True:
		mouse.move(0.1, 0.1)
		time.sleep(10)
		print('Ho!')
		mouse.move(-0.1, -0.1)
		time.sleep(10)
		print('Ha!')


	# Oh damn, that was simple!
