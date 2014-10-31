## workflow:

1. Scanning viral factor of vibrio cholera 

```
$ srst2 --input_pe SRR******_1.fastq SRR******_2.fastq --log --gene_db Vibrio_VF_clustered.fasta --output SRR******
```

2. Gene scanning output accession

```
$ find ./ -size -350c | grep fullgenes | sed "s/\.\/\|__fullgenes__gene__results.txt//g" > only_tcpA_genome_accession.txt
```

3. Get MLST type of only tcpA genome

```
$ srst2 --input_pe ...
```
