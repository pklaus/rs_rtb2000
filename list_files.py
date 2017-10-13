#!/usr/bin/env python

from helpers import get_instrument, write, query, ieee_488_2_block_data

import os, re

split_regex = ''',(?=(?:[^'"]|'[^']*'|"[^"]*")*$)'''

def strip_result(result):
    match = re.match('"(.*),,\d*"', result)
    return match.group(1)

def list_files(device=None, backend=None, paths=None):
    inst = get_instrument(device, backend=backend)
    if not paths:
        paths = (
              '/INT',
              '/INT/SETTINGS',
              '/INT/DATA',
              '/INT/REFERENCE',
              '/INT/FORMULARY',
              '/INT/BUSTABLE',
              '/INT/SEARCH',
              '/INT/STATISTICS',
              '/INT/DEMO',
              '/INT/LOG',
              '/INT/SETTINGS',
              '/USB_FRONT' )
    inst.query('MMEMory:DRIVes?') # -> "/INT","/USB_FRONT"
    for path in paths:
        inst.write('MMEMory:MSIS "/' + path.split('/')[1] + '"') # change to this drive
        inst.write('MMEMory:CDIRectory "' + path + '"')
        # --- sub folders
        sub_folders = inst.query('MMEMory:DCATalog? "' + path + '/*"').strip()
        sub_folders = re.split(split_regex, sub_folders)
        sub_folders = [strip_result(s) for s in sub_folders]
        if sub_folders == ['.', '..']: sub_folders = []
        for sub_folder in sub_folders:
            #print(os.path.join(path, sub_folder) + '/')
            pass
        # --- files
        files = inst.query('MMEMory:CATalog? "' + path + '/*.*",WTIMe')
        files = re.split(split_regex, files)
        files = files[2:]
        files = [strip_result(f) for f in files]
        for f in files:
            print(os.path.join(path, f))

if __name__ == "__main__":
    list_files()
