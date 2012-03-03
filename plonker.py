#!/usr/bin/python

import pyglet
from pyglet.window import key
import sys

elapsed_time = 0
max_time = 10

def usage ():
    print "Usage: plonker.py <interval>\n\n"
    print "Where <interval> is the number of seconds between bells"
    exit (1)

## Parse arguments
try:
    if (len(sys.argv) != 2):
        usage ()
    max_time = int(sys.argv[1])
except ValueError as e:
    usage ()

## Make window etc.
ding_sound = pyglet.resource.media('ding.mp3', streaming=False)
window = pyglet.window.Window()

@window.event
def on_key_press(symbol, modifiers):
    if (symbol == key.Q):
        exit (0)
    else:
        restart_timer()

@window.event
def on_draw():
    global elapsed_time
    global window

    window.clear()
    label = pyglet.text.Label(format_time_left (max_time - elapsed_time),
                              font_name='Inconsolata',
                              font_size=36,
                              x=window.width//2, y=window.height//2,
                              anchor_x='center', anchor_y='center')
    label.draw ()

def restart_timer():
    global elapsed_time
    elapsed_time = 0

def ding ():
    ding_sound.play()

def tick (dt):
    global elapsed_time
    elapsed_time += dt
    if (elapsed_time > max_time):
        ding ()
        restart_timer ()
pyglet.clock.schedule_interval(tick, 0.5)

def format_time_left (seconds):
    mins = int(seconds // 60)
    secs = int(seconds - 60*mins)
    if (seconds < 0):
        return 'Due!'
    elif (mins > 0):
        return '{}:{:02}'.format(mins, secs)
    else:
        return '{} seconds'.format(secs)

pyglet.app.run()
