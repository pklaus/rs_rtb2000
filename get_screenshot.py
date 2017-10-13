#!/usr/bin/env python

from helpers import parse_args, get_instrument, write, query, ieee_488_2_block_data
from datetime import datetime as dt

def get_screenshot(filename=None, device=None, backend=None):
    inst = get_instrument(device, backend=backend)
    if not filename: filename = dt.now().replace(microsecond=0).isoformat('_').replace(':','-') + '.png'
    if query(inst, "ACQuire:STATe?") not in ("STOP", "BRE"):
        write(inst, "STOP")
    if query(inst, "HCOPy:LANGuage?") != "PNG":
        write(inst, "HCOPy:LANGuage PNG")
    data = inst.query_raw("HCOPy:DATA?")
    data = ieee_488_2_block_data(data)
    with open(filename, 'wb') as f:
        f.write(data)

if __name__ == "__main__":
    def add_more_args(parser):
        parser.add_argument('--filename')
    args = parse_args(add_more_args)
    get_screenshot(args.filename, args.device, args.backend)
