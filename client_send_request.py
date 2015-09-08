#!/usr/bin/env python

import sys
import cv2
import os.path
import urllib2
import numpy as np
import boto
from boto.s3.key import Key
from image_utils import *

# This script is run upon Odroid's boot.
# When the system is up and running, the script will capture an image,
# After this, the script will upload the captured image to Amazon Web
# Service's bucket, and send an HTTP request to the server, notifying it
# on the arrival of the image.

cap = cv2.VideoCapture(0)
ret, new_image = cap.read()
# If the old image exists:
if os.path.isfile('old.jpg') :
    old_image = cv2.imread('old.jpg')
    cv2.imwrite('old.jpg', new_image)
# Otherwise, there is no old image:
else:
    cv2.imwrite('old.jpg', new_image)

cap = cv2.VideoCapture(0)
ret, new_image = cap.read()
if ret == False:
    exit(1)
filename = 'new.jpg'
cv2.imwrite(filename, new_image)

bucket_name = 'ronhandler'
# The original IDs are hidden with asterisks to prevent a security breach.
AWS_ACCESS_KEY_ID = '********************'
AWS_SECRET_ACCESS_KEY = '****************************************'

print('Connecting to AWS S3...')
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY,
        # Hardcoding the host parameter is a workaround for bug:
        # https://github.com/boto/boto/issues/621
        host="s3-eu-west-1.amazonaws.com")
bucket = conn.get_bucket(bucket_name) 
k = Key(bucket)
k.key = filename

testfile =  "/share/" + filename
print('Uploading "%s" to "%s/%s"...' % (testfile, bucket_name, k.key))

k.set_contents_from_filename(testfile)

print('Notifying the server that we have uploaded a file...')
url = """http://ec2-52-16-188-96.eu-west-1.compute.amazonaws.com/admin/run.php"""
urllib2.urlopen(url).read()
