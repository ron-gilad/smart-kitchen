#!/usr/bin/env python

import os.path
import cv2
import urllib2 
import numpy as np
from color_detection import *
from image_utils import *

# This method is run on the server after receiving the difference image.
# When this happens, the script will call a color detection algorithm, and
# update the website to reflect the change in the number of items.

def Detect(device):

    color = "No color found"
    direction = 0 # -1 means outside, 1 means inside.

    new_image = cv2.imread('/upload/new.jpg')
    # If the old image exists:
    if os.path.isfile('/upload/old.jpg') :
        old_image = cv2.imread('/upload/old.jpg')
        cv2.imwrite('/upload/old.jpg', new_image)
        # Generate a diff images.
        diff_image_positive = diff_func(old_image, new_image);
        diff_image_negative = diff_func(new_image, old_image);
        # Detect the dominant color of each diff image.
        color_in  = ColorDetection.detect_color(diff_image_positive)
        color_out = ColorDetection.detect_color(diff_image_negative)
        # If color_in is "background", it means that something was inserted
        # into the container.
        if (color_in == "background"):
            direction =  1
            color = color_in
        # Otherwise, something was removed from the container.
        else:
            direction = -1
            color = color_out
    # Otherwise, there is no old image:
    else:
        cv2.imwrite('/upload/old.jpg', new_image)
        color = ColorDetection.detect_color(new_image)

    if color in "red green yellow":
        # Compute the flow of items between the devices, and calculate the
        # amounts according to the newly detected item.
        isOrganic = False
        if color in "red green":
            isOrganic = True

        lastDevice = localStorage.load("lastDevice")
        nextDevice = "None"

        api = """http://localhost/admin/api.php?"""
        url_args = None

        # Newly added item to the counter.
        if lastDevice == "None" and device == "fridge":
            url_args = """color=""" + color + """&op=Add&consumed="""
        # Control the flow between stages.
        elif isOrganic == True and lastDevice == "fridge" and device == "bin":
            url_args = """color=""" + color + """&op=Remove&consumed=Bad"""
        elif isOrganic == True and lastDevice == "fridge" and device == "countertop":
            url_args = """color=""" + color + """&op=Remove&consumed=Good"""
        elif isOrganic == False and lastDevice == "fridge" and device == "bin":
            url_args = """color=""" + color + """&op=Remove&consumed=Bad"""
        elif isOrganic == False and lastDevice == "countertop" and device == "bin":
            url_args = """color=""" + color + """&op=Remove&consumed=Good"""
        # Reached a mid-stage. No need to add or remove anything, but
        # keep track of the current device for the next iteration.
        else:
            nextDevice = device
            localStorage.save("lastDevice", nextDevice)
            return

        # Push the item to the local web server.
        urllib2.urlopen(api + url_args).read()

        # Store the next device, so the next iteration will know from where
        # the item came.
        localStorage.save("lastDevice", nextDevice)
    return
