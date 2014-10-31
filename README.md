#### Usage:

1. Scanning viral factor of vibrio cholera 

```
$ srst2 --input_pe SRR000001_1.fastq SRR000001_2.fastq --log --gene_db Vibrio_VF_clustered.fasta --output output
```



2. Gene scanning output accession

```
$ find ./ -size -350c | grep fullgenes | sed "s/\.\/\|__fullgenes__gene__results.txt//g" > only_tcpA_genome.txt

```
