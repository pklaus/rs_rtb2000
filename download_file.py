#!/usr/bin/env python

from helpers import parse_args, get_instrument, write, query, ieee_488_2_block_data

import os

def download_file(path, device=None, backend=None):
    dirname, filename = os.path.split(path)
    inst = get_instrument(device, backend=backend)
    data = inst.write('MMEM:CDIR "' + dirname + '"')
    data = inst.query_raw('MMEM:DATA? "' + filename + '"')
    data = ieee_488_2_block_data(data)
    with open(filename, 'wb') as f:
        f.write(data)

if __name__ == "__main__":
    def add_more_args(parser):
        parser.add_argument('--filename')
    args = parse_args(add_more_args)
    download_file(args.filename, args.device, args.backend)
