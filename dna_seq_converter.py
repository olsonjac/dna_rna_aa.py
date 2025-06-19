"""DNA to RNA to Amino Acid sequence converter.

This script reads a DNA sequence from a text file, converts it to mRNA and
translates the codons into their corresponding amino acids. The resulting amino
acid sequence is written to a file.
"""

import argparse

RNA_CODON_DICT = {
    "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
    "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
    "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
    "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "UAA": "STOP", "CAA": "Q", "AAA": "K", "GAA": "E",
    "UAG": "STOP", "CAG": "Q", "AAG": "K", "GAG": "E",
    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
    "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "UGA": "STOP", "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G",
}

TRANSCRIPTION_MAP = str.maketrans({"A": "U", "T": "A", "C": "G", "G": "C"})


def read_dna(path: str) -> str:
    """Read a DNA sequence from a file and return it in uppercase."""
    with open(path, "r", encoding="utf-8") as f:
        return "".join(line.strip().upper() for line in f if line.strip())


def dna_to_rna(dna: str) -> str:
    """Convert a DNA sequence to mRNA."""
    invalid = set(dna) - {"A", "T", "C", "G"}
    if invalid:
        raise ValueError(f"Invalid bases in DNA sequence: {' '.join(sorted(invalid))}")
    return dna.translate(TRANSCRIPTION_MAP)


def rna_to_codons(rna: str) -> list[str]:
    """Split an RNA sequence into codons of length three."""
    return [rna[i:i + 3] for i in range(0, len(rna), 3) if len(rna[i:i + 3]) == 3]


def codons_to_amino_acids(codons: list[str]) -> list[str]:
    """Translate a list of RNA codons to amino acids."""
    return [RNA_CODON_DICT.get(c, "") for c in codons]


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description="Convert DNA file to amino acid sequence")
    parser.add_argument("input", help="Path to DNA text file")
    parser.add_argument("-o", "--output", default="aa_seq.txt", help="Output file for amino acid sequence")
    args = parser.parse_args(argv)

    dna = read_dna(args.input)
    print("DNA:", dna)

    rna = dna_to_rna(dna)
    print("RNA:", rna)

    codons = rna_to_codons(rna)
    print("Codon List:", codons)

    amino_acids = codons_to_amino_acids(codons)
    print("Amino Acid Sequence:", amino_acids)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(",".join(amino_acids))
    print(f"Amino acid sequence written to {args.output}")


if __name__ == "__main__":
    main()
