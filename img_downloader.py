#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
This is simple script for download all images by URLs in plaintext file.
The script requires requests module for working.
"""
import sys
import requests


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
    #TODO: 20160315-01 fix problem with IOError
    with open(file_loc, 'r') as urls_file:
        for url_address in urls_file.readlines():
            #TODO: 20160315-02 prepare checking if url_address is URL address
            url_address = url_address.strip()
            print "Start downloading image from %s" % url_address
            img_location = img_destiantion + url_address.split('/')[-1]
            download_image_by_url(url_address, img_location)


if __name__:
    print "Start program\n"
    f_location = sys.argv[1] if len(sys.argv) > 1 else raw_input("""\
    Please provide file name for URLs container:\n""")
    img_downlader(f_location)
    print "Stop program"
