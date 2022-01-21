
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
