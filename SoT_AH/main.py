"""
@Author https://github.com/DougTheDruid
@Source https://github.com/DougTheDruid/SoT-ESP-Framework
For community support, please contact me on Discord: DougTheDruid#2784
"""
import json
from multiprocessing.sharedctypes import Value
from pickle import FALSE, TRUE
from ssl import SSLSession
from Ship_Inputs.sloop_input import *
from Ship_Inputs.brig_input import *
from Ship_Inputs.galleon_input import *
import base64
import pyglet
from pyglet.text import Label
from pyglet.gl import Config
from helpers import SOT_WINDOW, SOT_WINDOW_H, SOT_WINDOW_W, main_batch, \
    version, logger
from sot_hack import SoTMemoryReader
import logging
import threading
from shipType import *


#hops = 0

#Simulate Keypresses
#from pynput.keyboard import Key, Controller

#keyboard = Controller



#autoInput()

print("\nWhat ship would you like to hop with: ")
shipType = input("\n(1) Sloop\n(2) Brig\n(3) Galleon\n")



#PlayerFile Loaded
#with open("findingplayers.json") as infile:
    #OFFSETS = json.load(infile)

# See explanation in Main, toggle for a non-graphical debug
DEBUG = False
# Pyglet clock used to track time via FPS
clock = pyglet.clock.Clock()


def update_all(_):
    """
    Triggers an entire read_actors call in our SoT Memory Reader. Will
    re-populate all of the display objects if something entered the screen
    or render distance.
    """
    smr.read_actors()
   


def load_graphics(_):
    """
    Our main graphical loop which updates all of our "interesting" items.
    During a "full run" (update_all()), a list of the objects near us and we
    care about is generated. Each of those objects has a ".update()" method
    we use to re-poll data for that item (required per display_object.py)
    """
    # Update our players coordinate information
    smr.update_my_coords()

    # Initialize a list of items which are no longer valid in this loop
    to_remove = []

    # For each actor that is stored from the most recent run of read_actors
    for actor in smr.display_objects:
        # Call the update function within the actor object
        actor.update(smr.my_coords)

        # If the actor isn't the actor we expect (per .update), prepare to nuke
        if actor.to_delete:
            to_remove.append(actor)

    # Clean up any items which arent valid anymore
    for removable in to_remove:
        smr.display_objects.remove(removable)


if __name__ == '__main__':
    
    
    logger.info(base64.b64decode("RG91Z1RoZURydWlkJ3MgRVNQIEZyYW1ld29yayBTdGFydGluZw==").decode("utf-8"))
    logger.info(f"Hack Version: {version}")
    
    # Initialize our SoT Hack object, and do a first run of reading actors
    smr = SoTMemoryReader()
    smr.read_actors()

        # Custom Debug mode for using a literal python interpreter debugger
        # to validate our fields. Does not generate a GUI.
    if DEBUG:
        while FALSE:
            smr.read_actors()

    # You may want to add/modify this custom config per the pyglet docs to
    # disable vsync or other options: https://tinyurl.com/45tcx6eu
    config = Config(double_buffer=True, depth_size=24, alpha_size=8)

    # Create an overlay window with Pyglet at the same size as our SoT Window
    window = pyglet.window.Window(SOT_WINDOW_W, SOT_WINDOW_H,
                                vsync=False, style='overlay', config=config,
                                caption="Autohopper")
    window.set_caption('AutoHopper')
    hwnd = window._hwnd  # pylint: disable=protected-access

    # Move our window to the same location that our SoT Window is at
    window.set_location(SOT_WINDOW[0], SOT_WINDOW[1])
    #while(True):
    @window.event
    def on_draw():
        """
        The event which our window uses to determine what to draw on the
        screen. First clears the screen, then updates our player count, then
        draws both our batch (think of a canvas) & fps display
        """
        window.clear()

        #Update our player count Label & player list
            
        smr = SoTMemoryReader()
        smr.read_actors()
        player_count.text = f"Player Count: {len(smr.server_players)}"
        player_list.text = "\n".join(smr.server_players)
        
        #print(player_count.text)
        #print(player_list.text)
        print(smr)
        #Draw our main batch & FPS counter at the bottom left
        main_batch.draw()
        fps_display.draw()

        out_file = open("serverplayers.json", "w") 
        json.dump(player_list.text, out_file, indent = 4, sort_keys = False) 
        out_file.close()

        
        #Finding players in game and matching too the server players
        f = open('findingplayers.json')
        data = f.read()
        #data = json.load(f)
        f.close()
        for x in smr.server_players:
            print("Name = " + x)
            #for myvalue in data['Players']:
                #mystring = "hello"
                #mystring = i
            if data.find(x)>0 :
                print("found player = " + x)
                

                #quit()
        # Closing file
        

#if shipType == 3:
            

    

    # We schedule an "update all" to scan all actors every 5seconds
    pyglet.clock.schedule_interval(update_all, 5)


    # We schedule a check to make sure the game is still running every 3 seconds
    pyglet.clock.schedule_interval(smr.rm.check_process_is_active, 3)

    # Runs through the macro to leave and join servers
    #print("ShipType = " + shipType)
    #if shipType.find("1") != -1:
        #pyglet.clock.schedule_interval(sloopInput(),180)
        #print("ShipType = " + shipType)

    #if shipType.find("2") != -1:
        #pyglet.clock.schedule_interval(brigInput(),180)
        #print("ShipType = " + shipType)

    #if shipType.find("3") != -1:
        #pyglet.clock.schedule_interval(galleonInput(),180)
        #print("ShipType = " + shipType)
    # We schedule an basic graphics load which is responsible for drawing
    # our interesting information to the screen. Max 144fps, can set unlimited
    # pyglet.clock.schedule(load_graphics)
    pyglet.clock.schedule_interval(load_graphics, 1/144)

    # Adds an FPS counter at the bottom left corner of our pyglet window
    # Note: May not translate to actual FPS, but rather FPS of the program
    fps_display = pyglet.window.FPSDisplay(window)
    
    #pyglet.clock.schedule_interval(shipinputType, 10)



    #loop

    # Our base player_count label in the top-right of our screen. Updated
    # in on_draw()
    player_count = Label("Player Count: {}",
                        x=SOT_WINDOW_W * 0.85,
                        y=SOT_WINDOW_H * 0.9, batch=main_batch)

    # The label for showing all players on the server under the count
    #if False:   #pylint: disable=using-constant-test
    player_list = Label("\n".join(smr.server_players), x=SOT_WINDOW_W * 0.85,
                            y=(SOT_WINDOW_H-25) * 0.89, batch=main_batch, width=300,
                            multiline=True)
    #player_list=players.json

    #if players.json in player_list:
    #print("Found them")
    #else:
    #print("Not work")
    # Note: The width of 300 is the max pixel width of a single line
    # before auto-wrapping the text to the next line. Updated in on_draw()

    # Runs our application and starts to use our scheduled events to show data
    pyglet.app.run()
    # Note - ***Nothing past here will execute as app.run() is a loop***


