# Codon Table Generator

A small Python bioinformatics program that accepts a DNA or RNA nucleotide sequence, groups it into codons, and translates each codon with the standard genetic code.

## Project objectives

- Store all 64 RNA codons and their amino-acid meanings.
- Accept DNA or RNA input and validate nucleotide symbols.
- Convert DNA input to RNA by replacing thymine (T) with uracil (U).
- Split a sequence into groups of three nucleotides.
- Translate complete codons and report an incomplete tail separately.
- Identify start (AUG) and stop (UAA, UAG, UGA) codons.
- Report sequence length, GC content, and amino-acid counts.

## Requirements

- Python 3.8 or newer is recommended.
- No third-party packages are required.

## Run the program

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the script (the filename contains a space):

```bash
python "codon table.py"
```

On Windows, this may also work:

```powershell
py "codon table.py"
```

Choose `1` for DNA or `2` for RNA, then enter the sequence. Lowercase letters are accepted, and whitespace within the sequence is ignored.

## Example

For DNA input:

```text
ATGGCTTTTTAA
```

The RNA sequence is `AUGGCUUUUUAA`, which is grouped as:

| Codon | Meaning |
| --- | --- |
| AUG | Methionine (start codon) |
| GCU | Alanine |
| UUU | Phenylalanine |
| UAA | Stop codon |

The program also prints the codon positions, the translated amino-acid sequence, GC percentage, amino-acid counts, and the full 64-codon table.

## Input rules and notes

- DNA accepts only A, T, G, and C.
- RNA accepts only A, U, G, and C.
- Empty sequences and invalid characters produce an error message.
- Complete codons are translated from left to right in the supplied reading frame; the program does not search for an open reading frame or stop translation at the first stop codon.
- If the sequence length is not divisible by three, the trailing one or two nucleotides are shown as an incomplete codon and are not translated.
- GC content is calculated as `(G + C) / sequence length × 100`.
- This educational script uses the standard genetic code. Mitochondrial and other variant genetic codes are not included.

## Main functions

| Function | Purpose |
| --- | --- |
| `validate_dna(sequence)` | Checks DNA symbols. |
| `validate_rna(sequence)` | Checks RNA symbols. |
| `dna_to_rna(dna_sequence)` | Converts T bases to U. |
| `divide_into_codons(sequence)` | Returns complete codons and any incomplete tail. |
| `translate_codons(codons)` | Maps codons to amino-acid labels. |
| `find_start_codons(codons)` | Returns one-based positions of AUG. |
| `find_stop_codons(codons)` | Returns positions and labels of stop codons. |
| `calculate_gc_content(sequence)` | Calculates the G/C percentage. |
| `count_amino_acids(amino_acids)` | Counts each translated label. |
| `display_codon_table()` | Prints the complete codon dictionary. |

## Tests

Run the automated unit tests from the project folder:

```bash
python -m unittest test_codon_table.py
```

The tests cover the codon dictionary, DNA/RNA validation, DNA-to-RNA conversion, incomplete codons, translation, start/stop positions, GC content, and amino-acid counts.

You can also try these cases manually:

1. Valid DNA: `ATGGCTTTTTAA`
2. Valid RNA: `AUGGCUUUUUAA`
3. Lowercase input: `atggct`
4. Whitespace in a sequence: `ATG GCT TAA`
5. Invalid DNA character: `ATGX`
6. Invalid RNA character: `AUTG`
7. Incomplete sequence: `ATGGC`
8. Empty input
9. Sequence without start or stop codons: `GCCGCC`

## Learning outcomes

This project demonstrates dictionaries, functions, loops, conditional logic, string handling, input validation, and introductory DNA/RNA sequence analysis.

## Possible future improvements

- Read sequence files in FASTA format.
- Allow users to select alternative genetic codes.
- Export results to a text or CSV file.
