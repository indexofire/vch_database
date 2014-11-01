#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import subprocess
import argparse


__version__ = '0.0.1'

def parse_args():
    parser = argparse.ArgumentParser(description="MLST pipeline")

    parser.add_argument('--version', action='version', version='%(prog)s ' + __version__)
    parser.add_argument('--list_file', type=str, required=True, help='NCBI SRA accession list file')

    return parser.parse_args()

def pipeline(list_file):

    with open(list_file, 'r') as f:
        accs = f.read().split("\n")

    for acc in accs:
        subprocess.call('fastq-dump --split-files ../sra/%s.sra' % acc, shell=True)
        subprocess.call('srst2 --input_pe %s_1.fastq %s_2.fastq --log --mlst_delimiter _ --mlst_db Vibrio_cholerae.fasta --mlst_definitions vcholerae.txt --report_new_consensus --output %s' % (acc, acc, acc), shell=True)
        subprocess.call('rm *.fastq', shell=True)


def main():
    args = parse_args()
    pipeline(args.list_file)

if __name__ == '__main__':
    main()
