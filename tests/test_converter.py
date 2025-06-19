import dna_seq_converter as conv


def test_basic_translation():
    dna = "ATGCGA"
    rna = conv.dna_to_rna(dna)
    assert rna == "UACGCU"
    codons = conv.rna_to_codons(rna)
    assert codons == ["UAC", "GCU"]
    amino = conv.codons_to_amino_acids(codons)
    assert amino == ["Y", "A"]
