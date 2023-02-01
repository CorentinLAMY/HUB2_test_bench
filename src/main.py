#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""main.py: test bench for HUB2 crash investigation"""

__author__ = "Corentin Lamy"
__copyright__ = "HUB2"
__license__ = "BRP"
__version__ = "1.0.0"
__email__ = "corentin.lamy@brp.com"
__status__ = "Developpement"


import commodo
import notification
import camera

import time

if __name__ == "__main__":
    commodo.heated_grip()
    time.sleep(1)
    commodo.applet_switcher()
    time.sleep(1)
    #notification.send_email()
