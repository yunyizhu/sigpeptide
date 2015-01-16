from hmmpytk import hmm_faster

def uni_set(l):
    u=set()
    for i in l:
        for j in i:
            u.add(j)
    return u

def train(train_data):
    

def build_model(train_data):
    amino_aid = list(uni_set(train_data[:, 0]))
    states = list(uni_set(train_data[:, 2]))
    model = hmm_faster.HMM(states=states, observations=amino_acid)


# Train a hidden markov model from protein sequence
def train(seq):
    model = hmm_faster.HMM(states=states, observations=amino_acid)
    model.randomize_matrices()
    model.train(ob_seq=seq, max_iteration=100, delta=0.001)

    return model.get_model()


# Train multiple sequences
def train_multiple_seqs(seqs):
    seq = []
    for s in seqs:
        seq += s

    return train(seq)


if __name__=='__main__':
    positive_sample = 'MKLAITLALVTLALLCSPASAGICPRFAHVIENLLLGTPSSYETSLKEFEPDDTMKDAGMQMKKVLDSLPQTTRENIMKLTEKIVKSPLCM'
    positive_model = train(positive_sample)

    negative_sample = 'MSLMDPLANALNHISNCERVGKKVVYIKPASKLIGRVLKVMQDNGYIGEFEFIEDGRAGIFKVELIGKINKCGAIKPRFPVKKFGYEKFEKRYLPARDFGILIVSTTQGVMSHEEAKKRGLGGRLLAYVY'
    negative_model = train(negative_sample)

    positive_samples = ['MKFFASLSKRFAPVLSLVVLVAGTLLLSAAPASAATVQIKMGTDKYAPLYEPKALSISAGDTVEFVMNKVGPHNVIFDKVPAGESAPALSNTKLAIAPGSFYSVTLGTPGTYSFYCTPHRGAGMVGTITVE',
                        'MKVVIFIFALLATICAAFAYVPLPNVPQPGRRPFPTFPGQGPFNPKIKWPQGY']
    (st, obs, init_matrix, trans_matrix, emit_matrix) = train_multiple_seqs(positive_samples)
    print 'init_matrix',init_matrix
    print 'trans_matrix',trans_matrix
    print 'emit_matrix',emit_matrix
