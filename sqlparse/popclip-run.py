#!/usr/bin/env python3
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(str(current_dir) + '/lib')
import sqlparse

query = os.environ.get('POPCLIP_TEXT', '')
print(sqlparse.format(query, reindent=True, keyword_case='upper'))
