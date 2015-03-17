#!/usr/bin/python
import matplotlib.pyplot as plt
import sys
sys.path.append('../../src')
sys.path.append('../../src/hmmpytk')
from data_reader import *
from hmm import *
import hmm_faster
import numpy
import random

#read in hmm model
m = hmm_faster.HMM()
m.read_from_file('model.txt')

human_data = read_test_data( 'proteom_human.txt' )

posi_tm_set = random.sample(human_data[ (human_data[:, 1]==1)&(human_data[:,2]==1), 0], 2000)
posi_nontm_set = random.sample(human_data[ (human_data[:, 1]==1)&(human_data[:,2]==0), 0], 2000)
nega_tm_set = random.sample(human_data[ (human_data[:, 1]==0)&(human_data[:,2]==1), 0], 2000)
nega_nontm_set = random.sample(human_data[ (human_data[:, 1]==0)&(human_data[:,2]==0), 0], 2000)
    
posi_tm_seq = predict(m, posi_tm_set)
posi_nontm_seq = predict(m, posi_nontm_set)
nega_tm_seq = predict(m, nega_tm_set)
nega_nontm_seq = predict(m, nega_nontm_set)
    
posi_tm_type= is_sig(posi_tm_seq)
posi_nontm_type= is_sig(posi_nontm_seq)
nega_tm_type= is_sig(nega_tm_seq)
nega_nontm_type= is_sig(nega_nontm_seq)

error1 = sum(nega_tm_type)/float(len(nega_tm_type)) #tm false positive
error2 = 1- sum(posi_tm_type)/float(len(posi_tm_type)) #tm false negative
error3 = sum(nega_nontm_type)/float(len(nega_nontm_type)) #nontm false positive
error4 = 1- sum(posi_nontm_type)/float(len(posi_nontm_type)) #nontm false negative
print 'tm false positive', error1, 'false negative', error2
print 'nontm false positive', error3, 'false negative', error4
