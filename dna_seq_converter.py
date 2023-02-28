
file_name = input("Enter the file name of the DNA sequence you want transcribed into mRNA and translated into its amino acid sequence in the local directory: ")
file = open(file_name, 'r')
dna = file.read().upper()
print("DNA: "+ dna)
rna = ""

# Generate the RNA string
for base in dna:  
  if base == "T":
    rna += "A"
  elif base == "A":
    rna += "U"
  elif base == "C":
    rna += "G"
  elif base == "G":
    rna += "C"    

#makes a list of rna codons and then prints rna and codon list
rna_seq = [(rna[i:i+3]) for i in range(0,len(rna), 3)]
print("RNA: "+rna)
print("Codon List:", rna_seq)

# mRNA Codon dictionary that will be used to translate the RNA sequence into the amino acid sequence. 
rna_codon_dict = {"UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V",
           "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
           "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
           "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
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



#this blocks creates an empty amino_acid list
#it finds the value(amino acid) for each codon in the dictonary and appends it to this list which is then printed
amino_acid=[]
for x in range(len(rna_seq)):
  amino_acid.append(rna_codon_dict[rna_seq[x]])
print("Amino Acid Sequence:", amino_acid)

#This section writes the amino acid sequence that is generated to a new comma separated text file labeled aa_seq.txt
aa_seq = amino_acid 
textfile = open("aa_seq.txt", "w")
for element in aa_seq:
    textfile.write(element + ",")
textfile.close()   
