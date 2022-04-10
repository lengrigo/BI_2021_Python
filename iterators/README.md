# Iterators homework
This time we are working with iterators and generators in Python

### Task 1
Python generator that takes path to fasta file and outputs sequence ids and sequence itself one by one.
  
### Task 2
Class `ChangeFastaSequence` reads sequences with changes.
- Class has a constructor with path to fasta file as argument
- Class object is iterable
- Iteration is infinite
- In each iteration class changes the sequence. It can randomly make one of two operations - delete part of sequence or duplicate it. The length of deleted or duplicated part also random and is equal to or less than one third of the full sequence length.
  
## Folder structure
`iterators.ipynb` - jupiter notebook with code, tests and comments  
`iterators.py` - file only with code  
`sequences.fasta` - fasta file with which code can be tested