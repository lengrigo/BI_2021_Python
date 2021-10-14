while True:
    command = input("Enter command: ")
    av_commands = ["transcribe", "reverse", "complement", "reverse complement"]
    complement_letters_DNA = {"A": "T", "T": "A", "C": "G", "G": "C", "a": "t", "t": "a", "c": "g", "g": "c"}
    complement_letters_RNA = {"A": "U", "U": "A", "C": "G", "G": "C", "a": "u", "u": "a", "c": "g", "g": "c"}
    if command == "exit":
        print("Good bye!")
        exit(0)
    if command in av_commands:
        print("Enter DNA or RNA sequence: ")
        seq = str(input())
        new_seq = ""
        count_DNA = 0
        count_RNA = 0
        for i in seq:
            if i in complement_letters_DNA:
                count_DNA += 1
            if i in complement_letters_RNA:
                count_RNA += 1
        if count_DNA == len(seq) or count_RNA == len(seq):
            if command == "transcribe":
                for i in range(len(seq)):
                    if seq[i] == "T":
                        new_seq += "U"
                    else:
                        new_seq += seq[i]
                print(new_seq)
            elif command == "reverse":
                print(seq[::-1])
            elif command == "complement":
                if count_DNA == len(seq):
                    for i in seq:
                        new_seq += complement_letters_DNA[i]
                if count_RNA == len(seq):
                    for i in seq:
                        new_seq += complement_letters_RNA[i]
                print(new_seq)
            elif command == "reverse complement":
                if count_DNA == len(seq):
                    for i in seq:
                        new_seq += complement_letters_DNA[i]
                if count_RNA == len(seq):
                    for i in seq:
                        new_seq += complement_letters_RNA[i]
                print(new_seq[::-1])
        else:
            print("It is not a DNA or RNA sequence! Try again!")
    else:
        print("There is no such command, try another one")
