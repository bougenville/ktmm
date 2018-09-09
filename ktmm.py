#
# "Keep That Mouse Moving"
# Stops a computer from going into IDLE mode
#
# Created by Andrew Odendaal (ao.gl)
#
from pynput.mouse import Button, Controller
import time

if __name__ == '__main__':
	mouse = Controller()
	while True:
		mouse.move(0.1, 0.1)
		time.sleep(1)
		mouse.move(0.1, 0.1)
		time.sleep(1)
