#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
This is simple script for download all images by URLs in plaintext file.
The script requires requests module for working.
"""
import sys
import requests


def img_downlader(file_loc, img_destiantion='downloaded_imgs/'):
    """\
    To run downloader is necessary to provide file location (file_loc)
    and optionally download image destination folder
    (img_destiantion, which default value is downloaded_imgs/).
    """
    #TODO: 20160315-01 fix problem with IOError
    with open(file_loc, 'r') as urls_file:
        for url_line in urls_file.readlines():
            #TODO: 20160315-02 prepare checking if url_line is URL address
            url_line = url_line.strip()
            print "Downloading image from %s" % url_line
            img_location = img_destiantion + url_line.split('/')[-1]
            #TODO: 20160315-03 check response of requests
            req_img = requests.get(url_line, verify=False, stream=True)
            with open(img_location, 'wb') as output_file:
                #TODO: 20160315-04 fix issue with warnings
                output_file.write(req_img.content)
                print "Image has been downloaded to %s\n" % img_location


if __name__:
    print "Start program"
    f_location = sys.argv[1] if len(sys.argv) > 1 else raw_input("""\
    Please provide file name for URLs container:\n""")
    img_downlader(f_location)
    print "Stop program"
