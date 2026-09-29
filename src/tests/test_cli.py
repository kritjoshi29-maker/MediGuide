import sys
import os
import unittest

# Add the src folder to Python's module search path
src_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "src"
)

sys.path.insert(0, src_path)

import cli


class TestMediGuideCLI(unittest.TestCase):

    def test_respiratory_symptoms_exist(self):
        symptoms = cli.get_symptoms("Respiratory")

        self.assertIn("Cough", symptoms)
        self.assertIn("Sneezing", symptoms)

    def test_digestive_symptoms_exist(self):
        symptoms = cli.get_symptoms("Digestive")

        self.assertIn("Nausea", symptoms)

    def test_skin_symptoms_exist(self):
        symptoms = cli.get_symptoms("Skin")

        self.assertIn("Itchy Skin", symptoms)

    def test_common_cold_full_match(self):
        symptoms = [
            "Cough",
            "Runny Nose",
            "Sneezing",
            "Sore Throat"
        ]

        results = cli.analyse_symptoms(
            "Respiratory",
            symptoms
        )

        self.assertEqual(
            results["Common Cold"],
            100.0
        )

    def test_empty_symptoms(self):
        results = cli.analyse_symptoms(
            "Respiratory",
            []
        )

        self.assertEqual(
            results["Common Cold"],
            0.0
        )


if __name__ == "__main__":
    unittest.main()
