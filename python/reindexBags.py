#!/usr/bin/env python
import argparse
import os
import subprocess


def reindex_rosbags(source_folder):

    active_files = [f for f in os.listdir(source_folder) if f.endswith('active')]
    active_files_concat = ' '.join(active_files)
    command = "rosbag reindex " + active_files_concat

    reindex_proc = subprocess.Popen(command, stdin=subprocess.PIPE, shell=True, cwd=source_folder,
                                     executable='/bin/bash')
    output, error = reindex_proc.communicate()
    reindex_proc.wait()

    os.chdir(source_folder)
    orig_files = [f for f in os.listdir(source_folder) if 'orig' in f]
    for file in orig_files:
        os.remove(file)

    reindexed_files = [os.rename(f, f[:-7]) for f in os.listdir(source_folder) if f.endswith('active')]
    reindexed_files_concat = ' '.join(reindexed_files)

    print("Following files successfully reindexed: {}".format(reindexed_files_concat))


def main():

    parser = argparse.ArgumentParser(description='command line tool ro reindex rosbag files')
    parser.add_argument('-s', '--source', action='store', dest='source_folder', help='specify the source folder', required=True)
    #parser.add_argument('-t', '--target', action='store', dest='target_folder', help='specify the target folder', required=True)
    
    args = parser.parse_args()

    reindex_rosbags(source_folder=args.source_folder)


if __name__ == '__main__':
    main()
