#!/usr/bin/python

#-*- coding: utf8 -*-

import xml.etree.ElementTree as ET
import string
from collections import Counter

list1 = '''<greeting> , 'Hello World!', </greeting>'''
pen = ET.fromstring(list1)
penContents = pen.getchildren()
for content in penContents:
    print('%-10s %3s' % (content.tag, content.get('e', 'e')))