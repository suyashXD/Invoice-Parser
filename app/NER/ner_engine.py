import spacy

def perform_ner(text):
    """
    Perform Named Entity Recognition (NER) on the given text.

    Args:
        text (str): Input text for NER.

    Returns:
        list: List of dictionaries containing entity text and label.
    """
    try:
        # Load spaCy NER model
        nlp = spacy.load("en_core_web_sm")

        # Process the text using spaCy NER
        doc = nlp(text)

        # Extract entities and their labels
        entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

        return entities
    except Exception as e:
        # Handle any exceptions that might occur during NER
        print(f"Error during NER: {e}")
        return []

if __name__ == "__main__":
    # Replace 'sample_text' with the text extracted from the OCR module
    sample_text = "This is a sample text containing invoice date, seller name, buyer name, addresses, and due date."

    # Call the perform_ner function to perform NER on the extracted text
    ner_results = perform_ner(sample_text)

    if ner_results:
        print("Named Entities:")
        print(ner_results)
    else:
        print("NER Failed. Check if spaCy and the OCR module are set up correctly.")
