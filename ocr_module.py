from paddleocr import PaddleOCR
import re

# Initialize PaddleOCR with English language
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Patterns for entity extraction
patterns = {
    '1': ('item_weight', r"(\d+(\.\d+)?)\s?(kg|kilogram|gram|ounce|g|lbs|pound|ton|microgram|milligram|carat)"),
    '2': ('item_volume', r"(\d+(\.\d+)?)\s?(ml|cup|gallon|oz|liters|millilitre|cubic foot|fluid ounce|decilitre|cubic inch|litre|quart|pint|centilitre)"),
    '3': ('voltage', r"(\d+(\.\d+)?)\s?(V|volt)"),
    '4': ('wattage', r"(\d+(\.\d+)?)\s?(W|watt|horsepower|kilowatt|kilowatt hour|milliampere hour)"),
    '5': ('maximum_weight_recommendation', r"(\d+(\.\d+)?)\s?(kg|g|lbs|pound|kilogram|gram|ounce|ton|microgram|milligram|carat)"),
    '6': ('height', r"(\d+(\.\d+)?)\s?(cm|in|mm|centimetre|millimetre|inch|metre|foot)"),
    '7': ('depth', r"(\d+(\.\d+)?)\s?(cm|in|mm|centimetre|millimetre|inch|metre|foot)"),
    '8': ('width', r"(\d+(\.\d+)?)\s?(cm|in|mm|centimetre|millimetre|inch|metre|foot)"),
    '9': ('maximum_current_recommendation', r"(\d+(\.\d+)?)\s?(A|ampere|milliampere|mA|microampere)")
}


# Function to extract text from an image using PaddleOCR
def extract_text(image_path):
    # OCR processing
    result = ocr.ocr(image_path, cls=True)
    # Concatenate all text results
    text = "\n".join([line[1][0] for line in result[0]])
    return text.strip()

# Function to extract specific entity from text
def extract_entity(text, entity_key):
    if entity_key not in patterns:
        return None, "Invalid entity key"
    
    entity_name, pattern = patterns[entity_key]
    match = re.search(pattern, text, re.IGNORECASE)
    return entity_name, match.group(0) if match else None
