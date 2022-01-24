
#established data source with the filename
file = open('sample_dna.txt', 'r')
# creates a variable to represent the dna sequence and converts the data to all upper case letters.
dna = file.read().upper()

#prints the origianl DNA sequence to the console for viewing and comparison
print ("DNA: ", dna)

#initializes the rna seq variable before the for loop begins
rna = ""

# Generate the RNA string
for i in dna:
    # Replace all occurrences of T with A
    if i == "T":
      rna += "A"
    # Replace all occurrences of A with U
    elif i == "A":
      rna += "U"
    # Replace all occurrences of C with G
    elif i == "C":
      rna += "G"
    # Replace all occurrences of G with C
    elif i == "G":
      rna += "C"    

# Print the RNA string
print( "RNA: ", rna)

# mRNA Codon dictionary that will be used to translate the RNA sequence into the amino acid sequence. 
rna_codon_dict = {"AUG" : "M", "CUU" : "L", "AUU" : "I", "GUU" : "V",
           "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
           "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
           "UUG" : "L", "CUG" : "L", "UUU" : "F", "GUG" : "V",
           "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
           "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
           "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
           "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
           "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D",
           "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
           "UAA" : "STOP", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
           "UAG" : "STOP", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
           "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G",
           "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
           "UGA" : "STOP", "CGA" : "R", "AGA" : "R", "GGA" : "G",
           "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" 
           }




num_codons = int(len(rna)/(3))
limit = num_codons
print("# of RNA codons: ", num_codons)

#initializes the amino acid list
aa_seq = []
rna_seq = [(rna[i:i+3]) for i in range(0,len(rna), 3)]
print("codon list:                ", rna_seq)

#this block iterates through the rna codon list and the codon dictionary to
#check for the presence of a known codon and then prints the amino acid to 
#a new list called aa_seq
amino_acid=[]
for x in range(len(rna_seq)):
    amino_acid.append(rna_codon_dict[rna_seq[x]])

print("the amino acid sequence is:" ,amino_acid)

#This section writes the amino acid sequence that is generated to a new comma separated text file labeled aa_seq.txt
aa_seq = amino_acid 
textfile = open("aa_seq.txt", "w")
for element in aa_seq:
    textfile.write(element + ",")
textfile.close()   
