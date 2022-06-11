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
from main import shipType


def shipinputType() :
    if shipType.find("1") != -1:
        #pyglet.clock.schedule_interval(sloopInput(),180)
        print("ShipType = " + shipType)
            
        (sloopInput)

    if shipType.find("2") != -1:        
        #pyglet.clock.schedule_interval(brigInput(),180)
        print("ShipType = " + shipType)
            
        (brigInput)

    if shipType.find("3") != -1:    
    #pyglet.clock.schedule_interval(galleonInput(),180)
        print("ShipType = " + shipType)
            
        (galleonInput)