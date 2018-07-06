#!/usr/bin/env python
import argparse
import os
import subprocess
import sys


def reindexBags(source_folder):

    active_files = [f for f in os.listdir(source_folder) if f.endswith('active')]
    if len(active_files) > 0:
        print("start reindexing...")
        command = "rosbag reindex " + ' '.join(active_files)

        reindex_proc = subprocess.Popen(command, stdin=subprocess.PIPE, shell=True, cwd=source_folder,
                                         executable='/bin/bash')
        output, error = reindex_proc.communicate()
        if error:
            print("error occured while running 'rosbag reindex'")
            sys.exit(0)
        reindex_proc.wait()

        os.chdir(source_folder)
        [os.remove(f) for f in os.listdir(source_folder) if 'orig' in f]
        [os.rename(f, f[:-7]) for f in os.listdir(source_folder) if f.endswith('active')]
        print("finished reindexing")

    else:
        print("no active bag files in given source folder!")


def main():

    parser = argparse.ArgumentParser(description='command line tool ro reindex rosbag files')
    parser.add_argument('-s', '--source', action='store', dest='source_folder', help='specify the source folder', required=True)
    
    args = parser.parse_args()

    reindexBags(source_folder=args.source_folder)


if __name__ == '__main__':
    main()
