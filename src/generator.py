# Generate synthetic data
import random
import data_reader
from hmm import build_model

amino_acid = ['A', 'C', 'E', 'D', 'G', 'F', 'I', 'H', 'K', 'M', 'L',
              'N', 'Q', 'P', 'S', 'R', 'T', 'W', 'V', 'Y', 'X']

states = ['h8', 'h9', 'h2', 'h3', 'h1', 'h6', 'h7',
                  'h4', 'h5', 'c10', 'C', 'O', 'c9', 'c8', 'c3',
                  'c2', 'c1', 'c7', 'c6', 'c5', 'c4', 'h18', 'h10',
                  'h11', 'h12', 'h13', 'h14', 'h15', 'h16', 'h17', 'n8',
                  'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7']


def generate_negative_sequence(length):
    seq = ''
    for i in xrange(length):
        index = int(random.random()*len(amino_acid))
        seq += amino_acid[index]
    return seq


def generate_negative_samples(filename, n, length):
    print 'Generate negative samples, saved to:', filename
    with open(filename, 'w') as f:
        for i in xrange(n):
            seq = generate_negative_sequence(length)
            f.write('> seq ' + str(i) + '\n')
            f.write(seq + '\n')


def cumsum(seq):
    temp_sum = 0
    temp_list = []
    for s in seq:
        temp_sum += s
        temp_list += [temp_sum]
    return temp_list


def draw(bag, prob):
    cumprob = cumsum(prob)
    p = random.random()
    index = 0
    for i in xrange(len(bag)):
        if p < cumprob[i]:
            index = i
            break
    return bag[index]


def generate_positive_sequence(pi, A, B, length):
    seq = ''
    state = draw(states, pi)
    while len(seq) < length:
        state_index = states.index(state)
        observation = draw(amino_acid, B[state_index])
        seq += observation
        state = draw(states, A[state_index])
    return seq


def generate_positive_samples(filename, n, length, pi, A, B):
    print 'Generate positive samples. Saved to:', filename
    with open(filename, 'w') as f:
        for i in xrange(n):
            seq = generate_positive_sequence(pi, A, B, length)
            f.write('> seq '+str(i) + '\n')
            f.write(seq + '\n')


if __name__ == '__main__':
    # random synthetic data
    num_data = 100
    length = 100
    #filename = '../data/synthetic/random.fa'
    #generate_negative_samples(filename, num_data, length)

    # Positive synthetic data
    #file_list = "training_list.txt"
    #train_data = data_reader.read_training_data( file_list )
    #m = build_model(train_data)
    #pi = m.get_initial_matrix()
    #A = m.get_transition_matrix()
    #B = m.get_emission_matrix()
    #pi[11] = 0; pi[31] = 1.0 # Rigged the transition matrix so it always start at Methionin state
    #filename = '../data/synthetic/positive.fa'
    #generate_positive_samples(filename, num_data, length, pi, A, B)

# Negative synthetic data
    file_list = "training_list.txt"
    train_data = data_reader.read_training_data( file_list )
    m = build_model(train_data)
    pi = m.get_initial_matrix()
    A = m.get_transition_matrix()
    B = m.get_emission_matrix()
    pi[11] = 1.0; pi[31] = 0 # Rigged the transition matrix so it always start at Methionin state
    filename = '../data/synthetic/negative.fa'
    generate_positive_samples(filename, num_data, length, pi, A, B)
