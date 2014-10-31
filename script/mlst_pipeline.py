import subprocess

with open('mlst.txt', 'r') as f:
    accs = f.read().split("\n")

for acc in accs:
    subprocess.call('fastq-dump --split-files ../sra/%s.sra' % acc, shell=True)
    subprocess.call('srst2 --input_pe %s_1.fastq %s_2.fastq --log --mlst_delimiter _ --mlst_db Vibrio_cholerae.fasta --mlst_definitions vcholerae.txt --output %s' % (acc, acc, acc), shell=True)
    subprocess.call('rm *.fastq', shell=True)
