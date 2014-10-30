#!/usr/bin/env python
import subprocess


with open('acc.txt', 'r') as f:
    accs = f.read().split("\n")

for acc in accs:
    subprocess.call('fastq-dump --split-files ../sra/%s.sra' % acc, shell=True)
    subprocess.call('srst2 --input_se %s_1.fastq %s_2.fastq --log --gene_db gene.db --output %s' % (acc, acc, acc), shell=True)
    subprocess.call('rm %s_1.fastq %s_2.fastq' % (acc, acc), shell=True)
