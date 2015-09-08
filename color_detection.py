#!/usr/bin/env python

import cv2
import numpy as np

class ColorDetection(object):
    # HSV color ranges, max values are: 180-255-255
    BOUNDARIES = {
        'red1': ([0, 50, 50], [20, 200, 200]),
        'red2': ([160, 50, 50], [179, 200, 200]),
        'green': ([38, 50, 50], [75, 200, 200]),
        'yellow':([103, 50, 50], [145, 200, 200]),
        'background':([0, 201, 201], [179, 255, 255])
    }

    # This method receives an image and returns the dominant color in this
    # image. It uses the color ranges in BOUNDARIES in order to classify the
    # colors.

    @staticmethod
    def detect_color(detection_image):
        img_hsv = cv2.cvtColor(detection_image, cv2.COLOR_BGR2HSV)
        # Loop for all defined colors
        for k,v in ColorDetection.BOUNDARIES.iteritems():
            # Convert to numpy arrays
            lower_color = np.array(v[0], np.uint8)
            upper_color = np.array(v[1], np.uint8)
            # Create mask from color bounds
            mask = cv2.inRange(img_hsv, lower_color, upper_color)
            # Count found color pixels
            amount_not_zero = cv2.countNonZero(mask)
            if amount_not_zero > 9000:
                if k=='red1' or k=='red2':
                    return 'red'
                else:
                    return k
            else:
                # Did not find k.
                continue
        return "No color found"
