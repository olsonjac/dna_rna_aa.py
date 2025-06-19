# dna_rna_aa sequence converter

This project contains a simple command line tool for converting DNA sequences
to mRNA and translating them into the corresponding amino acid sequence.

## Usage

```
python3 dna_seq_converter.py path/to/dna.txt -o output.txt
```

The input file should contain a DNA sequence consisting of the characters `A`,
`T`, `C` and `G`. The resulting amino acid sequence will be written to
`output.txt` (or `aa_seq.txt` if not provided).

The script prints the DNA, RNA, the generated codon list and the amino acid
sequence to the console.
