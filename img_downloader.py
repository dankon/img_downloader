#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
This is simple script for download all images by URLs in plaintext file.
"""

def img_downlader(file_loc, img_destiantion='/downloaded_imgs/'):
    """
    To run downloader is necessary to provide text file location (file_loc)
    and optionally download image destination (img_destiantion, which 
    default value is /downloaded_imgs/).
    """
    pass
    

if __name__:
    print "Start program"
    file_loc = raw_input("Please provide file name for URLs container:\n")
    img_downlader(file_loc)
    print "Stop program"
