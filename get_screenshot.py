#!/usr/bin/env python

from helpers import get_instrument, write, query, ieee_488_2_block_data

def get_screenshot(device=None, backend=None):
    inst = get_instrument(device, backend=backend)
    if query(inst, "HCOPy:LANGuage?") != "PNG":
        write(inst, "HCOPy:LANGuage PNG")
    data = inst.query_raw("HCOPy:DATA?")
    data = ieee_488_2_block_data(data)
    with open('tmp.png', 'wb') as f:
        f.write(data)

if __name__ == "__main__":
    get_screenshot()
