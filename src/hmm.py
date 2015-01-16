import sys
sys.path.append('hmmpytk')
import hmm_faster
import data_reader

def uni_set(s):
    u=set()
    for i in s:
        for j in i:
            u.add(j)
    return list(u)

def build_model(train_data):
    states = ['h8', 'h9', 'h2', 'h3', 'h1', 'h6', 'h7',
                  'h4', 'h5', 'c10', 'C', 'O', 'c9', 'c8', 'c3',
                  'c2', 'c1', 'c7', 'c6', 'c5', 'c4', 'h18', 'h10',
                  'h11', 'h12', 'h13', 'h14', 'h15', 'h16', 'h17', 'n8',
                  'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7']

    amino_acid = ['A', 'C', 'E', 'D', 'G', 'F', 'I', 'H', 'K', 'M', 'L', 'N',
                  'Q', 'P', 'S', 'R', 'T', 'W', 'V', 'Y', 'X']
    
    st_group=[ ['n1'],
               ['n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8'],
               ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10',
                'h11','h12','h13','h14','h15','h16','h17','h18'],
               ['c1'],['c2'],['c3'],['c4'],['c5'],['c6'],
               ['c7', 'c8', 'c9', 'c10'],
               ['C'], ['O']]
    model = hmm_faster.HMM(states=states, observations=amino_acid)
    model.train2(train_data[:,2], train_data[:,0], st_group)
    return model


def predict(model, ob_seqs, max_len = 100):
    st_seqs = []
    for peptide in ob_seqs:
        if len(peptide)>max_len:
            peptide = peptide[:100]
        st_seqs.append( model.viterbi(peptide) )
    return st_seqs

if __name__=='__main__':
    file_list="training_list.txt"
    train_data = data_reader.read_training_data( file_list )
    m = build_model(train_data)
    print 'states:', m.get_states()
    print 'obs:', m.get_observations()
    print 'init_matrix:', m.get_initial_matrix()
    print 'tran_matrix:', m.get_transition_matrix()
    print 'emit_matrix:', m.get_emission_matrix()
