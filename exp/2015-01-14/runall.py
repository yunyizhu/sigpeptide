#!/usr/bin/python
import matplotlib.pyplot as plt
import sys
sys.path.append('../../src')
sys.path.append('../../src/hmmpytk')
from data_reader import *
from hmm import *
import numpy

file_list="training_list.txt"
data = read_training_data( file_list )

# randomly split data into training set (80%) and testing set (20%),
#evaluate the prediction. Repeat 10 times.

for t in range(10):
    numpy.random.shuffle(data)
    train_set = data[:2554]
    test_set = data[2554:]
    posi_set = test_set[ test_set[:, 3]==1, 0]
    nega_set = test_set[ test_set[:, 3]==0, 0]
    m = build_model(train_set)
    posi_seq = predict(m, posi_set)
    nega_seq = predict(m, nega_set)
    posi_type= is_sig(posi_seq)
    nega_type= is_sig(nega_seq)
    posi_false = sum(nega_type)/float(len(nega_type))
    nega_false = 1- sum(posi_type)/float(len(posi_type))
    print 'false positive:', posi_false, 'false negative:', nega_false


#m = build_model(data)
#m.write_to_file('model.txt')
    
    
