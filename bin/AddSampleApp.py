"""
Command line tool to attach an app to an existing sample.

To create a Sample/app pairing from scratch, use CreateSamples.py.
"""

import os
import sys

# Add relative path libraries
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.abspath(os.path.sep.join([SCRIPT_DIR, "..", "lib"])))

import Repository

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Attach an app to an existing sample')
    parser.add_argument('-s', '--sample', type=str, dest="sample", required=True, help='name of sample')
    parser.add_argument('-a', '--app', type=str, dest="app", required=True, help='name of app')

    args = parser.parse_args()

    Repository.AddSampleApp(args.sample, args.app)

