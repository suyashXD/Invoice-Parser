import re
from dateutil.parser import parse

def extract_dates_from_text(text):
    """
    Extract dates from the given text.

    Args:
        text (str): Input text.

    Returns:
        list: List of extracted dates in the format YYYY-MM-DD.
    """
    # Use regular expression to find dates in various formats
    date_formats = r"\d{4}[-/]\d{1,2}[-/]\d{1,2}"
    dates = re.findall(date_formats, text)

    # Parse and standardize dates to YYYY-MM-DD format
    standardized_dates = []
    for date in dates:
        try:
            parsed_date = parse(date, yearfirst=True, dayfirst=False)
            standardized_date = parsed_date.strftime("%Y-%m-%d")
            standardized_dates.append(standardized_date)
        except ValueError:
            # Handle cases where date parsing fails
            pass

    return standardized_dates

if __name__ == "__main__":
    # Replace 'sample_text' with the text extracted from the OCR module
    sample_text = "Invoice date: 2023-07-27, Due date: 2023-08-10"

    # Call the extract_dates_from_text function to extract dates from the text
    extracted_dates = extract_dates_from_text(sample_text)

    if extracted_dates:
        print("Extracted Dates:")
        print(extracted_dates)
    else:
        print("No dates found in the text.")
