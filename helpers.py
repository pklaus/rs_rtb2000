#!/usr/bin/env python

from universal_usbtmc.backend_factory import import_backend
import logging, time

logger = logging.getLogger(__name__)

def write(inst, cmd):
    start = time.time()
    inst.write(cmd)
    end = time.time()
    logger.info(" -> " + cmd)
    logger.debug(f"This took {(end-start)*1000:.1f} ms.")

def query(inst, cmd):
    start = time.time()
    resp = inst.query(cmd)
    end = time.time()
    logger.info(" -> " + cmd)
    logger.info(" <- " + resp)
    logger.debug(f"This took {(end-start)*1000:.1f} ms.")

def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--loglevel', default='INFO')
    parser.add_argument('--backend')
    parser.add_argument('device')
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel.upper(), format="%(name)s - %(message)s")
    return args

def get_instrument(device=None, backend=None):
    if not device:
        args = parse_args()
        device = args.device
        backend = args.backend
    backend = import_backend(backend)
    inst = backend.Instrument(device)
    return inst
