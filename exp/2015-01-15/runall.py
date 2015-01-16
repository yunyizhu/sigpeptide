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

# use 5-fold crossvalidation to compute the averate error rate
# compute the error rate of tm and non_tm data seperately


numpy.random.shuffle(data)
error = numpy.zeros((4, 5))
for i in range(5):
    sub_set = numpy.array_split(data, 5)
    test_set = sub_set[i]
    del sub_set[i]
    train_set = numpy.concatenate(sub_set)
    posi_tm_set = test_set[ (test_set[:, 3]==1)&(test_set[:,4]==1), 0]
    posi_nontm_set = test_set[ (test_set[:, 3]==1)&(test_set[:,4]==0), 0]
    nega_tm_set = test_set[ (test_set[:, 3]==0)&(test_set[:,4]==1), 0]
    nega_nontm_set = test_set[ (test_set[:, 3]==0)&(test_set[:,4]==0), 0]
    
    m = build_model(train_set)
    
    posi_tm_seq = predict(m, posi_tm_set)
    posi_nontm_seq = predict(m, posi_nontm_set)
    nega_tm_seq = predict(m, nega_tm_set)
    nega_nontm_seq = predict(m, nega_nontm_set)
    
    posi_tm_type= is_sig(posi_tm_seq)
    posi_nontm_type= is_sig(posi_nontm_seq)
    nega_tm_type= is_sig(nega_tm_seq)
    nega_nontm_type= is_sig(nega_nontm_seq)
    
    error[0, i] = sum(nega_tm_type)/float(len(nega_tm_type)) #tm false positive
    error[1, i] = 1- sum(posi_tm_type)/float(len(posi_tm_type)) #tm false negative
    error[2, i] = sum(nega_nontm_type)/float(len(nega_nontm_type)) #nontm false positive
    error[3, i] = 1- sum(posi_nontm_type)/float(len(posi_nontm_type)) #nontm false negative

print 'tm', 'false positive', numpy.mean(error[0]), 'false negative', numpy.mean(error[1])
print 'nontm', 'false positive', numpy.mean(error[2]), 'false negative', numpy.mean(error[3])
    
