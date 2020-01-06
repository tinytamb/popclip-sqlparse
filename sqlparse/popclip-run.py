#!/usr/bin/env python3
import sys
import os
import unicodedata
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(str(current_dir) + '/lib')
import sqlparse

text = os.environ.get('POPCLIP_TEXT', '')
query = unicodedata.normalize('NFC', text)
print(sqlparse.format(query, reindent=True, keyword_case='upper'))
