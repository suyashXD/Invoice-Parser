import os
import sys
import unittest

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

# Now, you should be able to import the NER module
from app.NER.ner_engine import perform_ner

class TestNEREngine(unittest.TestCase):
    def test_perform_ner(self):
        # Sample text with known entities
        sample_text = "John Doe works at XYZ Corp and lives in New York."

        # Perform NER on the sample text
        entities = perform_ner(sample_text)

        # Define the expected entities
        expected_entities = {
            "PERSON": ["John Doe"],
            "ORG": ["XYZ Corp"],
            "GPE": ["New York"]
        }

        # Compare the extracted entities with the expected entities
        self.assertEqual(entities, expected_entities)

if __name__ == '__main__':
    unittest.main()
