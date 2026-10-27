
# CODON TABLE GENERATOR

# Project:
# Development of a Codon Table Generator
#
# Description:
# This program:
# 1. Creates a codon table containing all 64 codons.
# 2. Accepts DNA or RNA sequences from the user.
# 3. Validates the input sequence.
# 4. Converts DNA to RNA.
# 5. Divides the sequence into codons.
# 6. Translates codons into amino acids.
# 7. Identifies start and stop codons.
# 8. Handles incomplete codons.
# 9. Displays the complete codon table.
#
# Author: Abhinand PV




# 1. STANDARD GENETIC CODE


codon_table = {

    # --------------------------------------------------------
    # U - beginning
    # --------------------------------------------------------

    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",

    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",

    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UAA": "STOP",
    "UAG": "STOP",

    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGA": "STOP",
    "UGG": "Tryptophan",

    # --------------------------------------------------------
    # C - beginning
    # --------------------------------------------------------

    "CUU": "Leucine",
    "CUC": "Leucine",
    "CUA": "Leucine",
    "CUG": "Leucine",

    "CCU": "Proline",
    "CCC": "Proline",
    "CCA": "Proline",
    "CCG": "Proline",

    "CAU": "Histidine",
    "CAC": "Histidine",
    "CAA": "Glutamine",
    "CAG": "Glutamine",

    "CGU": "Arginine",
    "CGC": "Arginine",
    "CGA": "Arginine",
    "CGG": "Arginine",

    # --------------------------------------------------------
    # A - beginning
    # --------------------------------------------------------

    "AUU": "Isoleucine",
    "AUC": "Isoleucine",
    "AUA": "Isoleucine",
    "AUG": "Methionine (START)",

    "ACU": "Threonine",
    "ACC": "Threonine",
    "ACA": "Threonine",
    "ACG": "Threonine",

    "AAU": "Asparagine",
    "AAC": "Asparagine",
    "AAA": "Lysine",
    "AAG": "Lysine",

    "AGU": "Serine",
    "AGC": "Serine",
    "AGA": "Arginine",
    "AGG": "Arginine",

    # --------------------------------------------------------
    # G - beginning
    # --------------------------------------------------------

    "GUU": "Valine",
    "GUC": "Valine",
    "GUA": "Valine",
    "GUG": "Valine",

    "GCU": "Alanine",
    "GCC": "Alanine",
    "GCA": "Alanine",
    "GCG": "Alanine",

    "GAU": "Aspartic Acid",
    "GAC": "Aspartic Acid",
    "GAA": "Glutamic Acid",
    "GAG": "Glutamic Acid",

    "GGU": "Glycine",
    "GGC": "Glycine",
    "GGA": "Glycine",
    "GGG": "Glycine"
}


# ============================================================
# 2. DISPLAY CODON TABLE
# ============================================================

def display_codon_table():

    print("\n")
    print("=" * 75)
    print("                 STANDARD GENETIC CODON TABLE")
    print("=" * 75)

    print(f"{'Codon':<10} {'Amino Acid':<25} {'Type'}")
    print("-" * 75)

    for codon, amino_acid in codon_table.items():

        if codon == "AUG":
            codon_type = "START"

        elif codon in ["UAA", "UAG", "UGA"]:
            codon_type = "STOP"

        else:
            codon_type = "Amino Acid"

        print(f"{codon:<10} {amino_acid:<25} {codon_type}")

    print("=" * 75)


# ============================================================
# 3. VALIDATE DNA SEQUENCE
# ============================================================

def validate_dna(sequence):

    valid_bases = set("ATGC")

    for base in sequence:

        if base not in valid_bases:
            return False

    return True


# ============================================================
# 4. VALIDATE RNA SEQUENCE
# ============================================================

def validate_rna(sequence):

    valid_bases = set("AUGC")

    for base in sequence:

        if base not in valid_bases:
            return False

    return True


# ============================================================
# 5. CONVERT DNA TO RNA
# ============================================================

def dna_to_rna(dna_sequence):

    rna_sequence = dna_sequence.replace("T", "U")

    return rna_sequence


# ============================================================
# 6. DIVIDE SEQUENCE INTO CODONS
# ============================================================

def divide_into_codons(sequence):

    codons = []

    # Find the length that can be completely divided by 3
    complete_length = len(sequence) - (len(sequence) % 3)

    # Extract complete codons
    for i in range(0, complete_length, 3):

        codon = sequence[i:i + 3]

        codons.append(codon)

    # Check for incomplete codon
    incomplete_codon = sequence[complete_length:]

    return codons, incomplete_codon


# ============================================================
# 7. TRANSLATE CODONS
# ============================================================

def translate_codons(codons):

    amino_acids = []

    for codon in codons:

        amino_acid = codon_table.get(codon, "Unknown")

        amino_acids.append(amino_acid)

    return amino_acids


# ============================================================
# 8. FIND START CODONS
# ============================================================

def find_start_codons(codons):

    start_positions = []

    for i, codon in enumerate(codons):

        if codon == "AUG":

            start_positions.append(i + 1)

    return start_positions


# ============================================================
# 9. FIND STOP CODONS
# ============================================================

def find_stop_codons(codons):

    stop_positions = []

    for i, codon in enumerate(codons):

        if codon in ["UAA", "UAG", "UGA"]:

            stop_positions.append((i + 1, codon))

    return stop_positions


# ============================================================
# 10. DISPLAY TRANSLATION RESULT
# ============================================================

def display_translation(
    original_sequence,
    rna_sequence,
    codons,
    amino_acids,
    incomplete_codon
):

    print("\n")
    print("=" * 75)
    print("                    TRANSLATION RESULT")
    print("=" * 75)

    print("\nOriginal Sequence:")
    print(original_sequence)

    print("\nRNA Sequence:")
    print(rna_sequence)

    print("\nCodons:")
    print(" - ".join(codons))

    print("\n")

    print(f"{'No.':<8} {'Codon':<10} {'Amino Acid':<30}")
    print("-" * 75)

    for i, (codon, amino_acid) in enumerate(
        zip(codons, amino_acids), start=1
    ):

        print(f"{i:<8} {codon:<10} {amino_acid:<30}")

    # Incomplete codon
    if incomplete_codon:

        print("\nIncomplete Codon:")
        print(incomplete_codon)

        print(
            "The incomplete codon was not translated "
            "because a codon must contain 3 nucleotides."
        )


# ============================================================
# 11. DISPLAY START AND STOP CODONS
# ============================================================

def display_start_stop(codons):

    start_positions = find_start_codons(codons)

    stop_positions = find_stop_codons(codons)

    print("\n")
    print("=" * 75)
    print("                    START / STOP CODONS")
    print("=" * 75)

    # START CODONS

    if len(start_positions) > 0:

        print("\nStart Codon: AUG")

        print("Found at codon position(s):", end=" ")

        for position in start_positions:

            print(position, end=" ")

        print()

    else:

        print("\nStart Codon: AUG")

        print("No start codon found.")

    # STOP CODONS

    if len(stop_positions) > 0:

        print("\nStop Codon(s):")

        for position, codon in stop_positions:

            print(
                f"Position {position}: {codon}"
            )

    else:

        print("\nNo stop codon found.")


# ============================================================
# 12. MAIN PROGRAM
# ============================================================

def main():

    print("\n")
    print("=" * 75)
    print("                 CODON TABLE GENERATOR")
    print("=" * 75)

    print("\nThis program translates DNA/RNA sequences")
    print("using the standard genetic code.")

    # --------------------------------------------------------
    # Ask for sequence type
    # --------------------------------------------------------

    print("\nSelect sequence type:")

    print("1. DNA")

    print("2. RNA")

    sequence_type = input("\nEnter 1 or 2: ").strip()

    # --------------------------------------------------------
    # Validate sequence type
    # --------------------------------------------------------

    if sequence_type == "1":

        sequence_type = "DNA"

    elif sequence_type == "2":

        sequence_type = "RNA"

    else:

        print("\nERROR: Please enter 1 or 2.")

        return

    # --------------------------------------------------------
    # Get sequence from user
    # --------------------------------------------------------

    sequence = input(
        f"\nEnter your {sequence_type} sequence: "
    ).strip().upper()

    # --------------------------------------------------------
    # Check empty sequence
    # --------------------------------------------------------

    if sequence == "":

        print("\nERROR: Sequence cannot be empty.")

        return

    # --------------------------------------------------------
    # Validate sequence
    # --------------------------------------------------------

    if sequence_type == "DNA":

        if not validate_dna(sequence):

            print("\nERROR: Invalid DNA sequence.")

            print(
                "DNA can contain only A, T, G and C."
            )

            return

    else:

        if not validate_rna(sequence):

            print("\nERROR: Invalid RNA sequence.")

            print(
                "RNA can contain only A, U, G and C."
            )

            return

    # --------------------------------------------------------
    # Convert DNA to RNA
    # --------------------------------------------------------

    if sequence_type == "DNA":

        rna_sequence = dna_to_rna(sequence)

    else:

        rna_sequence = sequence

    # --------------------------------------------------------
    # Divide sequence into codons
    # --------------------------------------------------------

    codons, incomplete_codon = divide_into_codons(
        rna_sequence
    )

    # --------------------------------------------------------
    # Translate codons
    # --------------------------------------------------------

    amino_acids = translate_codons(codons)

    # --------------------------------------------------------
    # Display translation
    # --------------------------------------------------------

    display_translation(
        sequence,
        rna_sequence,
        codons,
        amino_acids,
        incomplete_codon
    )

    # --------------------------------------------------------
    # Display start and stop codons
    # --------------------------------------------------------

    display_start_stop(codons)

    # --------------------------------------------------------
    # Display amino acid sequence
    # --------------------------------------------------------

    print("\n")
    print("=" * 75)
    print("                    AMINO ACID SEQUENCE")
    print("=" * 75)

    print("\n")

    print(" - ".join(amino_acids))

    # --------------------------------------------------------
    # Display codon table
    # --------------------------------------------------------

    display_codon_table()

    # --------------------------------------------------------
    # End
    # --------------------------------------------------------

    print("\nProgram completed successfully.")

    print("=" * 75)


# ============================================================
# 13. RUN MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    main()
