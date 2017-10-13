#!/usr/bin/env python

import os, logging, struct

logger = logging.getLogger(__name__)

def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--loglevel', default='INFO')
    parser.add_argument('settings_file')
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel.upper(), format="%(name)s - %(message)s")
    return args

def analyze_settings_file(path="./settings.set"):
    dirname, filename = os.path.split(path)
    with open(path, 'rb') as f:
        data = f.read()
    cntr = 0
    pos = 0x19
    while pos < len(data):
        size = struct.unpack('>L', data[pos+1:pos+5])[0]
        print("#: {:2d}  Offset: 0x{:04X}  Type: 0x{:02X}  Size: 0x{:04X}".format(cntr, pos, data[pos], size))
        chunk = data[pos+9:pos+9+size]
        new_filename = os.path.splitext(filename)[0] + '.' + str(cntr) + '_' + hex(data[pos]) + '.other'
        assert new_filename != filename
        with open(os.path.join(dirname, new_filename), 'wb') as f:
            f.write(chunk)
        pos += 9 + size
        cntr += 1
    if pos != len(data):
        print("Not aligned?")

if __name__ == "__main__":
    args = parse_args()
    analyze_settings_file(args.settings_file)
