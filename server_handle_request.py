#!/usr/bin/env python

import sys
import server_detect
from boto.s3.connection import S3Connection
 
# This script is run on the AWS server.
# When the server receives an HTTP request, it will run this script and
# initialize the image detection algorithm.

BUCKET_NAME = 'ronhandler'
# The original IDs are hidden with asterisks to prevent a security breach.
AWS_ACCESS_KEY_ID = '********************'
AWS_SECRET_ACCESS_KEY = '****************************************'

filename="new.jpg"
aws_connection = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
bucket = aws_connection.get_bucket(BUCKET_NAME)
print('Downloading from bucket...')
k = bucket.get_key('new.jpg')
if k == None:
    print('Error. Could not find key in bucket.')
    exit(1)
k.get_contents_to_filename('/upload/new.jpg')
print('Deleting from bucket...')
bucket.delete_key(k)

device = None
script_name = sys.argv[0]
if "server_bin_handle_request" in script_name:
    device = "bin"
elif "server_fridge_handle_request" in script_name:
    device = "fridge"
elif "server_countertop_handle_request" in script_name:
    device = "countertop"

print('Detecting color...')
detect.Detect(device)
