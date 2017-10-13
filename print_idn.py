#!/usr/bin/env python

import time
from helpers import get_instrument

def print_idn(device=None, backend=None):
    inst = get_instrument(device, backend=backend)
    query = "*IDN?"
    start = time.time()
    idn = inst.query(query)
    end = time.time()
    print(" -> " + query)
    print(" <- " + idn)
    print(f"This took {(end-start)*1000:.1f} ms.")

if __name__ == "__main__":
    print_idn()
