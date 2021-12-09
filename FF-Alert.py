import curses
from curses import wrapper
import pyautogui
import sys
import time
from playsound import playsound
import keyboard

status = ["Initializing...","Running","Running.","Running..","Running...","Stopped","How did it get this status??"]
newstat = status[0]
queue = "Locating..."
messy = 1

def dings(): 
	playsound("C:\Windows\Media\chord.wav")
	playsound("C:\Windows\Media\chord.wav")
	playsound("C:\Windows\Media\chord.wav")


def main(stdscr):
	global newstat
	global queue
	global messy
	while True:
		stdscr.clear()
		stdscr.addstr(10,30,"- Final Fantasy Queue Checker -",curses.A_UNDERLINE)
		stdscr.addstr(12,30,"Programc Status :" + str(newstat))
		stdscr.addstr(13,30,"Queue Location  :" + str(queue))
		stdscr.addstr(15,30,"Hold Q to exit")
		stdscr.refresh()
		time.sleep(1)
		if queue != None:
				newstat = status[messy]
				messy += 1 
				queue = pyautogui.locateOnScreen("lookfor.png")
				stdscr.refresh()
				if messy == 5:
					messy = 1
		if keyboard.is_pressed('q'):
			stdscr.addstr(14,30,"Closing.....")
			newstat = status[5]
			stdscr.refresh()
			break
		if queue == None:
			time.sleep(3)
			queue = pyautogui.locateOnScreen("lookfor.png")
			if queue == None:
				newstat == status[5]
				stdscr.addstr(16,30,"Better requeue before you QQ")
				stdscr.refresh()
				dings()
				
wrapper(main)
