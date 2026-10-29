Codon Table Generator Project Overview

The Codon Table Generator is a Python project that translates DNA and RNA sequences into their corresponding amino acids using the standard genetic code.

A codon is a group of three nucleotides. Each codon represents an amino acid or a stop signal during protein synthesis.

Objectives

Accept DNA and RNA sequences from the user. Check that the sequence contains valid nucleotide symbols. Convert DNA sequences into RNA when required. Divide the sequence into groups of three nucleotides and translate each codon into its corresponding amino acid. Identify start and stop codons and show any incomplete nucleotides at the end of the sequence.

Features

The program includes all 64 RNA codons in the standard genetic code. It accepts DNA sequences containing A, T, G and C, and RNA sequences containing A, U, G and C. It checks for invalid characters, converts DNA to RNA, divides sequences into codons, and displays the translated amino acid sequence. It also reports start and stop codons, sequence length, GC content, amino acid counts, and any incomplete codon at the end.

Example

DNA sequence: ATGGCTTTTTAA

RNA sequence: AUGGCUUUUUAA

Codons: AUG - GCU - UUU - UAA

Corresponding amino acids: Methionine - Alanine - Phenylalanine - Stop

Start codon: AUG

Stop codon: UAA

How to Run the Project

Install Python 3 and download or clone this repository. Open the project folder in your Python editor, such as IDLE or VS Code, and run the file named codon table.py. Choose whether to enter a DNA or RNA sequence, then type the sequence when prompted.

Input Notes

The sequence can contain lowercase or uppercase letters, and spaces between bases are ignored. If an invalid character is entered, the program displays an error. If the sequence length is not divisible by three, the remaining one or two nucleotides are shown as an incomplete codon and are not translated. Translation follows the reading frame from the beginning of the supplied sequence and uses the standard genetic code.

Technologies Used

Python 3, dictionaries, loops, conditional statements, functions, and string handling.

Learning Outcomes

This project demonstrates basic Python programming and introductory bioinformatics concepts, including DNA/RNA sequence validation, codon division, and amino acid translation.

Future Enhancements

The project could be extended to read FASTA files, save results to a file, or support additional genetic codes.

Author: Abhinand PV
