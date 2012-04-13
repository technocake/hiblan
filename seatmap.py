#!/usr/bin/python
# coding: utf-8

import curses
import curses.panel
import locale
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()
import time


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
	win.box() 
	win.addstr(2, 2, str) 
	panel = curses.panel.new_panel(win) 
	return win, panel 

def seatmap(win):
	
	win.addstr(0,0, str(win.getmaxyx()))
	win.border(0)
	win.refresh()

	(logowin, logopan) = make_panel(20, 150, 30, 20, LOGO)
	
	curses.panel.update_panels()
	logopan.top()
	logowin.refresh()	


	while 1:
		time.sleep(10)
		#CMD = win.getch()
		
	#raise Exception


curses.wrapper(seatmap)


#print curses.__file__