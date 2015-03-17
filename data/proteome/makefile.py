#!/usr/bin/python
from Bio.Alphabet import generic_protein
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

dir = 'human/mouse/'

sig = [record.seq.tostring().upper() for record in SeqIO.parse(dir+'sigpeptide', 'fasta')]
sig = set(sig)
nonsig = [record.seq.tostring().upper() for record in SeqIO.parse(dir+'non_sig', 'fasta')]
nonsig = set(nonsig)
tm = [record.seq.tostring().upper() for record in SeqIO.parse(dir+'TM', 'fasta')]
tm = set(tm)
nontm = [record.seq.tostring().upper() for record in SeqIO.parse(dir+'non_TM', 'fasta')]
nontm = set(nontm)


signonsig = sig.intersection( nonsig )
sig = sig.difference(signonsig)
nonsig = nonsig.difference(signonsig)

tmnontm = tm.intersection( nontm )
tm = tm.difference(tmnontm)
nontm = nontm.difference(tmnontm)

sig_tm =  sig.intersection(tm) 
sig_nontm =  sig.intersection(nontm) 
nonsig_tm =  nonsig.intersection(tm) 
nonsig_nontm =  nonsig.intersection(nontm) 

sig_tm = [SeqRecord( Seq (seq,  generic_protein) ) for seq in sig_tm ]
sig_nontm = [SeqRecord( Seq (seq,  generic_protein) ) for seq in sig_nontm ]
nonsig_tm = [SeqRecord( Seq (seq,  generic_protein) ) for seq in nonsig_tm ]
nonsig_nontm = [SeqRecord( Seq (seq,  generic_protein) ) for seq in nonsig_nontm ]

SeqIO.write(sig_tm, dir+'sig_tm.faa', 'fasta')
SeqIO.write(sig_nontm, dir+'sig_nontm.faa', 'fasta')
SeqIO.write(nonsig_tm, dir+'nonsig_tm.faa', 'fasta')
SeqIO.write(nonsig_nontm, dir+'nonsig_nontm.faa', 'fasta')
