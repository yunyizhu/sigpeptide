from hmmpytk import hmm_faster

# The twenty amino acids, abbreviated into single letter
amino_acid = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']

states = ['met', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6',
          'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8',
          'c1', 'c2', 'c3', 'c4', 'c5', 'c6',
          'm1', 'm2', 'm3', 'm4', 'end']


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
    print init_matrix
    print trans_matrix
    print emit_matrix
