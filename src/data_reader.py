#!/usr/bin/python
from numpy import array
from Bio import SeqIO
import matplotlib.pyplot as plt

def get_rg_len( rg_seq ):
        n_len = []
        h_len = []
        c_len = []
        for i in range( len(rg_seq) ):
                seq = ''.join(rg_seq[i])
                n_ind = seq.find('n')
                h_ind = seq.find('h')
                c_ind = seq.find('c')
                C_ind = seq.find('C')
                n_len.append( h_ind )
                h_len.append( c_ind - h_ind )
                c_len.append( C_ind - c_ind )
        return n_len, h_len, c_len

def region( nr_rg_seq):
        rg_seq = []
        for i in range( len(nr_rg_seq) ):
                seq = ''.join(nr_rg_seq[i])
                rg_seq.append( [j for j in seq if not j.isdigit()])
        return rg_seq

def number_region( rg_seq, n_max=8, h_max=18, c_max = 10):
        nr_rg_seq = []
        for i in range( len(rg_seq) ):
                seq = rg_seq[i][:]
                tmp = ''.join(seq)
                n_ind = tmp.find('n')
                h_ind = tmp.find('h')
                c_ind = tmp.find('c')
                C_ind = tmp.find('C')
                if C_ind > -1:
                        n_state = n_max
                        site = h_ind - 1
                        while site > n_ind:
                                seq[site] = 'n' + str(max(n_state, 2))
                                n_state = n_state - 1
                                site = site-1
                        seq[0] = 'n1'

                        h_state = h_max
                        site = c_ind -1
                        while site > h_ind:
                                seq[site] = 'h' + str(h_state)
                                site = site - 1
                                h_state = h_state -1
                        seq[site] = 'h1'

                        c_state = 1
                        site = C_ind -1
                        while site >= c_ind:
                                seq[site] = 'c' + str(c_state)
                                site = site - 1
                                c_state = c_state + 1
                nr_rg_seq.append(seq)
        return nr_rg_seq
                        
def rg_replace(old):
        new = old.replace('M', 'O')
        new = new.replace('i', 'O')
        new = new.replace('o', 'O')
        return new

def is_sig(rg_seq):
        t = []
        for s in rg_seq:
                if s[0] == 'O':
                        t.append(0)
                else:
                        t.append(1)
        return array(t)

def read_training_data( file_list ):
        data = []
        with open( file_list, 'r' ) as f :
                dump = f.readline()
                for line in f:
                        tmp = line.split()
                        data_path = tmp[0]
                        is_signal = int(tmp[1])
                        is_tm = int(tmp[2])
                        for record in SeqIO.parse(data_path, "fasta"):
                                seq = record.seq.tostring().split('#')
                                data.append([list(seq[0]), list(seq[1]), list(rg_replace(seq[1])), is_signal, is_tm])
        data = array(data)
        data[ :, 2] = number_region( data[:, 2])
        return data

def read_test_data( file_list ):
        data = []
        with open( file_list, 'r' ) as f :
                dump = f.readline()
                for line in f:
                        tmp = line.split()
                        data_path = tmp[0]
                        is_signal = int(tmp[1])
                        is_tm = int(tmp[2])
                        for record in SeqIO.parse(data_path, "fasta"):
                                seq = record.seq.tostring()
                                data.append([list(seq), is_signal, is_tm] )
        data = array(data)
        return data

if __name__ == "__main__" :
        file_list="training_list.txt"
        data = read_training_data( file_list )

        #summary of the region lengths
        n_len, h_len, c_len = get_rg_len( data[ data[:, 3] == 1, 1 ] )
        print 'n length range:', min(n_len), max(n_len)
        print 'h length range:', min(h_len), max(h_len)
        print 'c length range:', min(c_len), max(c_len)

        #fig = plt.figure()
        #p1 = fig.add_subplot(131)
        #p1.hist(n_len, bins=max(n_len) - min(n_len), normed=True)
        #p1.set_title('n region')
        #p2 = fig.add_subplot(132)
        #p2.hist(h_len, bins=max(h_len) - min(h_len), color='green',normed=True)
        #p2.set_title('h region')
        #p3 = fig.add_subplot(133)
        #p3.hist(c_len, bins=max(c_len) - min(c_len), color='red', normed=True)
        #p3.set_title('c region')
        #plt.show()
        
