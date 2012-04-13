#!/usr/bin/python
# coding: utf-8

import curses
import curses.panel
import locale
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()


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


def seatmap(win):

	
	win.addstr(0,0, str(win.getmaxyx()))
	logoWin = curses.newwin(0,0)
	logoWin.addstr(20,20, LOGO)
	win.border(0)
	win.refresh()
	logoWin.refresh()	
	
	while 1:
		CMD = win.getch()
	#raise Exception


curses.wrapper(seatmap)


#print curses.__file__