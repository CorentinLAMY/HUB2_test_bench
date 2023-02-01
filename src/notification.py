#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""notification.py: send notification via email when a crash is detected"""

__author__ = "Corentin Lamy"
__copyright__ = "HUB2"
__license__ = "BRP"
__version__ = "1.0.0"
__email__ = "corentin.lamy@brp.com"
__status__ = "Developpement"

import smtplib, ssl

# Receiver
receiver_email = "corentin.lamy@brp.com"

# Sender
port = 465  # For SSL
sender_email = "mecatro.brp@gmail.com"
password = "Brp!1234"

# Create a secure SSL context
context = ssl.create_default_context()

# Message
message = """\
Subject: Blackscreen test bench event

An event has been detected!"""

# Send notification function
def send_email():
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)