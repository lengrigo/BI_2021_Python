# This program will convert concentration from mol/l into gram/l
print("Enter concentration in mol/l: ")
concentration_mol = float(input())
print("Enter number of nucleotides: ")
num = int(input())
if concentration_mol < 0 or num < 0:
    print("Concentration and amount of nucleotides are always positive numbers")
concentration_gram = round(concentration_mol / (345 * num), 4)
print(f'Concentration of oligonucleotide is - {concentration_gram}, gram/l')
