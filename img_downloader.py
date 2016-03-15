#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
This is simple script for download all images by URLs in plaintext file.
"""
import sys

def img_downlader(file_loc, img_destiantion='/downloaded_imgs/'):
    """
    To run downloader is necessary to provide file location (file_loc)
    and optionally download image destination (img_destiantion, which
    default value is /downloaded_imgs/).
    """
    #TODO: 20160315-01 fix problem with IOError
    with open(file_loc, 'r') as urls_file:
        for url_line in urls_file.readlines():
            #TODO: 20160315-02 prepare checking if url_line is URL address
            url_line = url_line.strip()
            print "downloading image from %s \n" % url_line

if __name__:
    print "Start program"
    f_location = sys.argv[1] if len(sys.argv) > 1 else raw_input("""\
Please provide file name for URLs container:\n""")
    img_downlader(f_location)
    print "Stop program"
