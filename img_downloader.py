#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
This is simple script for download all images by URLs in plaintext file.
The script requires requests module for working.
"""
import sys
import os
import re
import requests

URL_IMG_PATTERN = (r'^(http|ftp)s?://[a-zA-Z0-9-.:_/]+'
                   r'.(rgb|gif|pbm|pgm|ppm|tiff|rast|xbm|jpeg|jpg|bmp|png)$')


def download_image_by_url(url_address, img_location):
    """\
    Download single image by url address and save to target location.
    """
    req_img = requests.get(url_address, verify=False, stream=True)
    if req_img.status_code == 200:
        with open(img_location, 'wb') as output_file:
            #TODO: 20160315-04 fix issue with warnings
            output_file.write(req_img.content)
            print "Image has been downloaded to %s\n" % img_location
    else:
        print "ERROR: Page not found - image can not be download\n"    
    

def img_downlader(file_loc, img_destiantion='downloaded_imgs/'):
    """\
    Downloader grab all images from urls contained by plaintext file.
    
    To run downloader is necessary to provide file location (file_loc)
    and optionally download image destination folder
    (img_destiantion, which default value is downloaded_imgs/).
    """
    with open(file_loc, 'r') as urls_file:
        for url_address in urls_file.readlines():
            url_address = url_address.strip()
            if re.match(URL_IMG_PATTERN, url_address):
                print "Start downloading image from %s" % url_address
                img_location = img_destiantion + url_address.split('/')[-1]
                download_image_by_url(url_address, img_location)
            else:
                print "ERROR: Uncorrect url address (%s)\n" % url_address


if __name__:
    print "Start program\n"
    file_text = "Please provide file name for URLs container:\n"
    f_location = sys.argv[1] if len(sys.argv) > 1 else raw_input(file_text)
    while not os.path.isfile(f_location):
        f_location = raw_input("ERROR: File doesn't exist.\n" + file_text)
    img_downlader(f_location)
    print "Stop program"
