#!/usr/bin/python
# coding: utf-8

import curses
import curses.panel
import locale
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()
import time
import random


LOGO = """
 88          88 88          88                         
 88          "" 88          88                         
 88             88          88                         
 88,dPPYba,  88 88,dPPYba,  88 ,adPPYYba, 8b,dPPYba,   
 88P'    "8a 88 88P'    "8a 88 ""     `Y8 88P'   `"8a  
 88       88 88 88       d8 88 ,adPPPPP88 88       88  
 88       88 88 88b,   ,a8" 88 88,    ,88 88       88  
 88       88 88 8Y"Ybbd8"'  88 `"8bbdP"Y8 88       88 
"""

def make_panel(h,l, y,x, str): 
	win = curses.newwin(h,l, y,x) 
	win.erase() 
	#win.box() 
	win.addstr(2, 2, str) 
	panel = curses.panel.new_panel(win) 
	return win, panel 

def seatmap(win):
	
	win.addstr(0,0, str(win.getmaxyx()))
	win.border(0)
	win.refresh()

	(MY, MX) = win.getmaxyx()

	(logowin, logopan) = make_panel(20, 100, MY/2-20/2, MX/2-100/2, LOGO)
	
	curses.panel.update_panels()
	logopan.top()
	logowin.refresh()	




	while 1:
		time.sleep(1) 
		(PY,PX) = logowin.getmaxyx()
		(MY, MX) = win.getmaxyx()

		Y,X = random.randrange(0, MY+1-PY), random.randrange(0, MX+1-PX) 
 		logopan.move(Y,X)
		curses.panel.update_panels()
		logowin.refresh()
		win.refresh()
		#CMD = win.getch()
		
	#raise Exception


curses.wrapper(seatmap)


#print curses.__file__