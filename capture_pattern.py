#!/usr/bin/env python

from helpers import get_instrument, write, query

setup_cmds = """
TRIGger:A:SOURce CH1
TRIGger:A:TYPE EDGE
TRIGger:A:LEVel1:VALue 50e-3
RUN
ACQuire:STATe?
"""

def capture_pattern(device=None, backend=None):
    inst = get_instrument(device, backend=backend)
    for cmd in setup_cmds.strip().split('\n'):
        if cmd.endswith('?'):
            query(inst, cmd)
        else:
            write(inst, cmd)

if __name__ == "__main__":
    capture_pattern()
