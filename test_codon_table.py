"""Basic regression tests for the Codon Table Generator."""
import importlib.util
from pathlib import Path
import unittest

SCRIPT_PATH = Path(__file__).with_name("codon table.py")
SPEC = importlib.util.spec_from_file_location("codon_table_generator", SCRIPT_PATH)
codon_app = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(codon_app)


class CodonTableTests(unittest.TestCase):
    def test_codon_table_has_64_entries(self):
        self.assertEqual(len(codon_app.codon_table), 64)

    def test_valid_dna_and_rna(self):
        self.assertTrue(codon_app.validate_dna("ATGC"))
        self.assertFalse(codon_app.validate_dna("AUGC"))
        self.assertTrue(codon_app.validate_rna("AUGC"))
        self.assertFalse(codon_app.validate_rna("ATGC"))

    def test_dna_to_rna(self):
        self.assertEqual(codon_app.dna_to_rna("ATGTAA"), "AUGUAA")

    def test_divide_complete_and_incomplete_codons(self):
        codons, tail = codon_app.divide_into_codons("AUGGCUA")
        self.assertEqual(codons, ["AUG", "GCU"])
        self.assertEqual(tail, "A")

    def test_translation(self):
        self.assertEqual(
            codon_app.translate_codons(["AUG", "GCU", "UAA"]),
            ["Methionine (START)", "Alanine", "STOP"],
        )

    def test_start_and_stop_positions_are_one_based(self):
        self.assertEqual(codon_app.find_start_codons(["AUG", "GCU", "AUG"]), [1, 3])
        self.assertEqual(codon_app.find_stop_codons(["AUG", "UAA", "UGA"]), [(2, "UAA"), (3, "UGA")])

    def test_gc_content(self):
        self.assertAlmostEqual(codon_app.calculate_gc_content("AUGGCC"), 66.6666667, places=5)
        self.assertEqual(codon_app.calculate_gc_content(""), 0.0)

    def test_amino_acid_counts(self):
        self.assertEqual(
            codon_app.count_amino_acids(["Alanine", "STOP", "Alanine"]),
            {"Alanine": 2, "STOP": 1},
        )


if __name__ == "__main__":
    unittest.main()
