#!/usr/bin/python
# coding: utf-8

import curses, curses.panel, time, random

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
	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

	win = curses.newwin(h,l, y,x) 
	win.erase() 
	panel = curses.panel.new_panel(win) 
	return win, panel 

def seatmap(win):

	(MY, MX) = win.getmaxyx() #putting screen size in a corner
	win.border(0)
	win.addstr(0,0, str(win.getmaxyx()))
	win.addstr(MY-1, MX/2-4, "Colormode: %s" % curses.has_colors() ) #Tells if we can use colors or not :)

	win.refresh()

	logolen = len(LOGO.split('\n')[1])+1 #Width of the logo

	(logowin, logopan) = make_panel(20, logolen, MY/2-20/2, MX/2-100/2, LOGO)
	
	curses.panel.update_panels()
	logopan.top()
	logowin.refresh()	

	


	while 1:
		time.sleep(1) 
		(PY,PX) = logowin.getmaxyx()
		(MY, MX) = win.getmaxyx()
		win.addstr(0, MX/2, str(logowin.getmaxyx()) )
		Y,X = random.randrange(0, MY-PY), random.randrange(0, MX+1-PX) 
 		logopan.move(Y,X)
 		curses.init_pair(1,random.randrange(0, 8), 0 )
 		logowin.addstr(2, 2, LOGO, curses.color_pair(1))

		curses.panel.update_panels()
		logowin.refresh()
		win.refresh()

curses.wrapper(seatmap)
