import random


# Task 1
def fasta_reader(path: str):
    sequences = {}
    with open(path) as fasta_file:
        for line in fasta_file:
            if line.startswith(">"):
                name = line.strip()
            else:
                if name not in sequences:
                    sequences[name] = ''
                sequences[name] += line.strip()

    for key, value in sequences.items():
        yield key, value


# Task 2
class ChangeFastaSequence:
    def __init__(self, path):
        self.path = path
        self.fasta = fasta_reader(self.path)

    def __iter__(self):
        return self

    def change(self, seq):
        prob = random.randint(1, 2)
        subseq_length = random.randrange(1,
                                         len(seq) // 3)  # length of subsequence that we will be duplicated or deleted
        subseq_start = random.randrange(0, len(seq) - subseq_length)  # start position
        subseq_stop = subseq_start + subseq_length  # stop position
        if prob == 1:  # making deletion
            resulted_sequence = seq[:subseq_start] + seq[subseq_stop:]
            # print('deletion')
        else:  # making insertion
            subseq = seq[subseq_start:subseq_stop]
            resulted_sequence = seq[:subseq_stop] + subseq + seq[subseq_stop:]
            # print('insertion')
        return resulted_sequence

    def __next__(self):
        try:
            id_, seq = next(self.fasta)
        except StopIteration:
            self.fasta = fasta_reader(self.path)
            id_, seq = next(self.fasta)
        return id_, self.change(seq)
