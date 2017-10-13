#!/usr/bin/env python

from universal_usbtmc.backend_factory import import_backend

def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--backend')
    parser.add_argument('device')
    args = parser.parse_args()
    return args

def get_instrument(device=None, backend=None):
    if not device:
        args = parse_args()
        device = args.device
        backend = args.backend
    backend = import_backend(backend)
    inst = backend.Instrument(device)
    return inst
