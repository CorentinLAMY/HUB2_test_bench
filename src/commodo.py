#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""commodo.py: interface skidoo commodo to the computer"""

__author__ = "Corentin Lamy"
__copyright__ = "HUB2"
__license__ = "BRP"
__version__ = "1.0.0"
__email__ = "corentin.lamy@brp.com"
__status__ = "Developpement"

import time
import serial

__USB_port_commodo__ = 'COM3'
__serial_speed__ = 9600
__serial_timeout__ = 1
#, timeout=__serial_timeout__
commodo = serial.Serial(__USB_port_commodo__, __serial_speed__)

def heated_grip():
    """Heated Grip command for the commodo"""
    commodo.write(bytes(b'H'))
    time.sleep(0.1)
    #print('H')
    
def ride_settings():
    """Ride settings command for the commodo"""
    commodo.write(b'R')
    time.sleep(0.1)
    #print('R') 

def voice_assit():
    """Voice assistant command for the commodo"""
    commodo.write(b'V')
    time.sleep(0.1)
    #print('V') 

def applet_switcher():
    """Applet switcher command for the commodo"""
    commodo.write(b"A")
    time.sleep(0.1)
    #print('A') 

def ok():
    """Ok command for the commodo"""
    commodo.write(b'O')
    time.sleep(0.1)
    #print('O') 

def up():
    """Up command for the commodo"""
    commodo.write(b'U')
    time.sleep(0.1)
    #print('U') 

def down():
    """Down command for the commodo"""
    commodo.write(b'D')
    time.sleep(0.1)
    #print('D') 