# -*- coding: utf-8 -*-
#!/usr/bin/env python
import argparse
from Bio import SeqIO


__version__ = '0.0.1'

delimiter = '_'
take = ['adk', 'gyrB', 'mdh', 'metE', 'pntA', 'purM', 'pyrC']
st_seq = {}

def parse_args():
    parser = argparse.ArgumentParser(description="Connect all loci sequences")
    parser.add_argument('--version', action='version', version='%(prog)s ' + __version__)
    parser.add_argument('--profile', type=str, required=True, help="MLST profile file")
    parser.add_argument('--seq', type=str, required=True, help="MLST sequence file")

    return parser.parse_args()

def run(profile, seq):
    with open(profile, 'r') as pro_f:
        sts = pro_f.read().split('\n')
        sts.remove('')
        sts.remove('')
        sts.remove('ST\tadk\tgyrB\tmdh\tmetE\tpntA\tpurM\tpyrC\tclonal_complex')

    seq_dict = {}

    for seq in SeqIO.parse(seq, "fasta"):
        seq_dict[seq.id] = seq.seq

    for st in sts:
        profile = st.split('\t')

        loci = ''

        for i in take:
            loci = loci + str(seq_dict[i + delimiter + str(profile[int(take.index(i)) + 1])])

        st_seq['>ST' + str(profile[0])] = loci

    mlst = []

    for k, v in st_seq.items():
        string = k + '\n' + v + '\n'
        mlst.append(string)

    with open("data.txt", "w") as f:
        f.writelines(mlst)

def main():
    args = parse_args()
    run(args.profile, args.seq)

if __name__ == '__main__':
    main()
