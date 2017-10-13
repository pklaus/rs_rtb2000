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
    pos = data.find(b'BM')
    size = struct.unpack('<L', data[pos+2:pos+6])[0]
    img_filename = os.path.splitext(filename)[0] + '.bmp'
    assert img_filename != filename
    with open(os.path.join(dirname, img_filename), 'wb') as f:
        f.write(data[pos:pos+size])
    pos += size
    size = struct.unpack('>H', data[pos+3:pos+5])[0]
    pos += 9 # header length between bmp and ASCII SCPI setup cmds
    assert (pos+size) == len(data)
    cmds = data[pos:pos+size]
    cmds = cmds.decode('ascii')
    cmds_filename = os.path.splitext(filename)[0] + '.cmds'
    assert cmds_filename != filename
    with open(os.path.join(dirname, cmds_filename), 'w') as f:
        f.write(cmds)

if __name__ == "__main__":
    args = parse_args()
    analyze_settings_file(args.settings_file)
