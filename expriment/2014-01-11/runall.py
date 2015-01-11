#!/usr/bin/python
from numpy import array
from Bio import SeqIO
import matplotlib.pyplot as plt
import sys
sys.path.append('../../src')
from data_reader import *

file_list="training_list.txt"
data = read_training_data( file_list )
len(data)

#summary of the region lengths
n_len, h_len, c_len = get_rg_len( data[ data[:, 3] == 1, 1 ] )
print 'n length range:', min(n_len), max(n_len)
print 'h length range:', min(h_len), max(h_len)
print 'c length range:', min(c_len), max(c_len)

fig = plt.figure(figsize=(13.0, 8.0))
p1 = fig.add_subplot(131)
p1.hist(n_len, bins=max(n_len) - min(n_len), normed=True)
p1.set_title('n region')
p2 = fig.add_subplot(132)
p2.hist(h_len, bins=max(h_len) - min(h_len), color='green',normed=True)
p2.set_title('h region')
p3 = fig.add_subplot(133)
p3.hist(c_len, bins=max(c_len) - min(c_len), color='red', normed=True)
p3.set_title('c region')

fig.savefig('region_length_distribution.png')
        
