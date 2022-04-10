import matplotlib.pyplot as plt
from Bio import Seq
from Bio import SeqIO
from Bio.SeqUtils import GC


# task 1
class BioinformaticsStudent:
    def __init__(self, name, course, city, skills=None):
        self.skills = skills
        if self.skills is None:
            self.skills = set()
        self.name = name
        self.course = course
        self.city = city

    def subjects_semester1(self):
        bio_subjects = ['Discrete math,',
                        'Statistics and R,',
                        'Python programming,',
                        'Command line,',
                        'Bioinformatics practice']
        programmer_subjects = ['Algorithms,',
                               'Statistics,',
                               'Molecular biology,',
                               'Bioinformatics practice']
        if self.course == 'Bioinformatics for biologists':
            print(*bio_subjects)
        elif self.course == 'Algorithmic bioinformatics':
            print(*programmer_subjects)

    def subjects_semester2(self):
        bio_subjects = ['Introduction to ML,',
                        'Python programming,',
                        'Jornal club,',
                        'Molecular phylogenetics and evolution,',
                        'Bioinformatics practice,',
                        'Project']
        programmer_subjects = ['ML,',
                               'Statistics,',
                               'Jornal club,',
                               'Molecular phylogenetics and evolution,',
                               'Bioinformatics practice,',
                               'Project']
        if self.course == 'Bioinformatics for biologists':
            print(*bio_subjects)
        elif self.course == 'Algorithmic bioinformatics':
            print(*programmer_subjects)

    def learning(self, new_skill):
        self.skills.add(new_skill)

    def meeting(self, student):
        if self.city == student.city:
            print(f'{self.name} and {student.name} can meet offline in {self.city}!')
        else:
            print(f'{self.name} and {student.name} can meet only online')

    def skills_show(self):
        print(f'{self.name} can', *self.skills)


# task 2
class Rna:
    def __init__(self, sequence):
        self.sequence = Seq.Seq(sequence)

    def translation(self):
        translated_sequence = self.sequence.translate()
        return translated_sequence

    def reverse_transcription(self):
        dna = self.sequence.back_transcribe()
        return dna


# task 3
class PositiveSet(set):
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__(*args)
        else:
            for i in args:
                if i > 0:
                    super(PositiveSet, self).add(i)

    def add(self, *args):
        for number in args:
            if number > 0:
                super(PositiveSet, self).add(number)


# task 4
class Fasta:
    def __str__(self):
        return self.path
    __repr__ = __str__

    def __init__(self, path):
        self.path = path
        self.sequences = [sequence.seq for sequence in SeqIO.parse(path, 'fasta')]

    def seq_amount(self):
        return len(self.sequences)

    def length_hist(self):
        lengths = [len(sequence) for sequence in self.sequences]
        fig, axis = plt.subplots(figsize=(15, 7))
        axis.hist(lengths)
        plt.xlabel("Sequence length")
        plt.ylabel("Sequences count")
        plt.show()

    def gc_count(self):
        gc_count = [GC(sequence) for sequence in self.sequences]
        return gc_count

    def four_mers(self):
        four_mer = {}
        for sequence in self.sequences:
            for i in range(4):
                for j in range(i, len(sequence), 4):
                    mer = sequence[i+j:i+j+4]
                    if len(mer) == 4:
                        if mer in four_mer.keys():
                            four_mer[mer] += 1
                        else:
                            four_mer[mer] = 1
        four_mers_sum = sum(four_mer.values())
        four_mer = dict(sorted(four_mer.items(), key=lambda x: x[0]))
        for key, value in four_mer.items():
            four_mer[key] = value/four_mers_sum
        fig, axis = plt.subplots(figsize=(15, 7))
        axis.bar(x=list(range(len(four_mer))), height=four_mer.values())
        axis.set_xticks(range(0, len(four_mer), 1))
        axis.set_xticklabels(four_mer.keys(), rotation=90)
        plt.xlabel("4-mer")
        plt.ylabel("4-mer count")
        plt.show()

    def metrics(self):
        return self.seq_amount(), self.gc_count()
