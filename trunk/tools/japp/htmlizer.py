#
# Title: htmlizer script, prepare HTML for Drupal publishing
# Author: Sebastien Lelong, Copyright (c) 2008, all rights reserved.
# Adapted-by:
# Compiler:
#
# This file is part of jallib (http://jallib.googlecode.com)
# Released under the BSD license (http://www.opensource.org/licenses/bsd-license.php)
#
# Sources:
#
# Description: this script takes a HTML file as input, keeps "body" element's content
# and convert some URL to make them compatible with Drupal's. Output is printed in a
# "content" file, in a "topublish" directory, within the one containing original
# HTML files. It also pick used images from orignal "src" location, and put them in 
# an directory (so they are selected and ready for publishing)
#


import sys, os, re
import urlparse
from BeautifulSoup import BeautifulSoup

# we'll put images and attachments in general in this directory
DRUPAL_IMG_PATH_PREFIX = "/sites/default/files/"
# url aliasing by default prefixes with "content/", but we can define URLs we want
DRUPAL_CONTENT_PREFIX = "/content/"
# where to put all stuff to publish
OUTPUT_DIR="topublish"
# Filename for filtered HTML
OUTPUT_FILE="content"

try:
    hfile = sys.argv[1]    
except IndexError:
    print >> sys.stderr, "Please provide a HTML file as input"
    sys.exit(255)

# prepare ouput directory
dirn = os.path.dirname(hfile)
os.system("rm -f %s/%s/*" % (dirn,OUTPUT_DIR))
os.system("mkdir -p %s/%s/" % (dirn,OUTPUT_DIR))


html = BeautifulSoup(file(hfile).read())

# extract body content
body = html.findAll("body")
if len(body) == 0:
    print >> sys.stderr, "No <body> element found, assuming content corresponds to inner body"
    body = html
elif len(body) > 1:
    print >> sys.stderr, "More than one <body> element found, c'mon that's impossible, are you joking with me buddy ?..."
    sys.exit(1)
else:
    body = body[0]

# convert image URL (src attr) and copy them in ouput directory.
# Why ? Because when DITA compiler processes a DITA file, it resolves
# outer DITA topic, with their images. So you finally get more than needed...
# I, Seb, can't find an option in compiler to just produce HTML for one file
# (no outer topic) *and* still copy related images (I can do the first, without
# the second, using onlytopic.in.map=true, but the images don't get copied...)
imgs = body.findAll("img")
for img in imgs:
    origsrc = img['src']
    imgfn = os.path.basename(origsrc)
    img['src'] = DRUPAL_IMG_PATH_PREFIX + imgfn
    os.system("cp %s/%s %s/%s/" % (dirn,origsrc,dirn,OUTPUT_DIR))


# convert link URL
pat = re.compile("\.html",re.I)
as_ = body.findAll("a")
for a in as_:
    try:
        href = a['href']
        scheme, netloc, path, params, query, fragment = urlparse.urlparse(href)
        if scheme:
            # external link, skip it
            continue
        if not path:
            # must just an anchor, skip it
            continue
        # if we get here, url is a local file
        # remove html suffix, as we'll remove it in drupal
        path = pat.sub("",path)
        # add prefix for Drupal's content
        path = DRUPAL_CONTENT_PREFIX + path
        
        # back to <a> element
        a['href'] = urlparse.urlunparse((scheme, netloc, path, params, query, fragment))

    except KeyError:
        # no href, skip it
        continue

# remove title, because title will be put in mail's subject. So leaving it here would
# produce twice title
h1s = body.findAll("h1")
if not h1s:
    print >> sys.stderr, "No <h1> element found, assuming no title..."
else:
    # there should be only one element, but anyway remove first one
    h1s[0].replaceWith("")

# we're done
fout = file("%s/%s/%s" % (dirn,OUTPUT_DIR,OUTPUT_FILE),"w")
fout.write(body.renderContents())
