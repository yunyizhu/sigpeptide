# Generate synthetic data
import random

amino_acid = ['A', 'C', 'E', 'D', 'G', 'F', 'I', 'H', 'K', 'M', 'L',
              'N', 'Q', 'P', 'S', 'R', 'T', 'W', 'V', 'Y', 'X']


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


if __name__ == '__main__':
    # Negative synthetic data
    num_data = 100
    length = 100
    filename = '../data/synthetic/negative.fa'
    generate_negative_samples(filename, num_data, length)
