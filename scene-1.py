#!/usr/bin/python
# coding: utf-8

import curses, curses.panel, time, random



PADDING = 1

NYANCAT = ["""
+      o     +              o   
    +             o     +       +
o          +
    o  +           +        +
+        o     o       +        o
_-_-_-_-_-_-_-,------,      o 
_-_-_-_-_-_-_-|   /\_/\  
-_-_-_-_-_-_-~|__( ^ .^)  +     +  
_-_-_-_-_-_-_-""  ""      
+      o         o   +       o
    +         +
o        o         o      o     +
    o           +
+      +     o        o      +    
""",

"""
+      o     +              o   
    ()            o     +       +
o          +
    o  +          ()        +
+        o     o       +        o
-_-_-_-_-_-_-_             o 
_-_-_-_-_-_-_-,------,   
-_-_-_-_-_-_-~|   /\_/\   +     +  
_-_-_-_-_-_-_-|__( ^ .^)  
+      o      ""  ""         o
    +         +
o        o         o      o     +
    o           +
+      ()     o        o      +    
""",

"""
-_-_-_-_-_-_-_
_-_-_-_-_-_-_-
-_-_-_-_-_-_-
_-_-_-_-_-_-_-""",

"""
_-_-_-_-_-_-_-
-_-_-_-_-_-_-
_-_-_-_-_-_-_-
-_-_-_-_-_-_-_""" 

]


def make_panel(h,l, y,x, str): 
	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

	win = curses.newwin(h,l, y,x) 
	win.erase() 
	panel = curses.panel.new_panel(win) 
	curses.panel.update_panels()
	return win, panel 


def rendergras(win, Y, X, H, W):	
	curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK )
	curses.panel.update_panels()

	(MY, MX) = win.getmaxyx()
	for i in range(H):
		win.addstr(Y+i, X, "/\\"  * min(W/2, MX), curses.color_pair(1)) 
	
	win.refresh()


def renderNyan(nyanwin, X, Y, TICK):
	nyanwin.addstr(0,0, NYANCAT[TICK%2])
	tails = NYANCAT[2+TICK%2].split('\n')
	for i in range(len(tails)):
		nyanwin.addstr(5,5, str(i))
		curses.init_pair(3, 2+i, curses.COLOR_BLACK)
		nyanwin.addstr(5+i,0, tails[i], curses.color_pair(3))

	nyanwin.refresh()

def renderBackground(win, H, W, TICK):
	"""
		Generating a nyancat background :) 
	"""

	if TICK%3: return 
	N_PARTICLES = (H*W)/10
	win.clear()
	while N_PARTICLES > 0:
		N_PARTICLES -= 1


		for ch in ['o', '+']:
			Y,X = N_PARTICLES%((H-1)/random.randrange(1,8)), N_PARTICLES%((W-1)/random.randrange(1,8))

			curses.init_pair(2,random.randrange(0, 8), 0 )
			win.addstr(Y, X,ch,	curses.color_pair(2) )
	

	win.refresh()


def scene1(win):
	TICK = 0
	H = len(NYANCAT[0].split('\n'))+2
	L = len(NYANCAT[0].split('\n')[1])+4
	(MY, MX) = win.getmaxyx()

	X, Y = MX/2.0 - L/2.0, MY/2.0 - H/2.0

	(nyanwin, nyanpan ) = make_panel(H, L, Y, X, NYANCAT[0] )
	nyanpan.top()
	nyanwin.refresh()
	
	while 1:
		
		time.sleep(0.2) 
		(MY, MX) = win.getmaxyx()

		#renderBackground(win, MY, MX, TICK)
		renderNyan(nyanwin, Y,X, TICK)

		curses.panel.update_panels()
		#rendergras(win, 10, 0, 4, MX)
		win.refresh()
		TICK += 1




curses.wrapper(scene1)
