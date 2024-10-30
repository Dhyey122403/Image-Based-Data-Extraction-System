from ocr_module import extract_text, extract_entity, patterns
from mongo_integration import insert_entity_to_mongo

def main():
    # Get image path from user
    image_path = input("Enter the path of the image to process: ").strip()
    
    try:
        # Perform OCR
        text = extract_text(image_path)
        print("\nOCR completed. Text extracted from image:\n")
        print(text)

        # Display entity options to the user
        options = "\n".join([f"{key}: {desc[0]}" for key, desc in patterns.items()])
        print("\nChoose an entity to extract by entering the corresponding number:\n")
        print(options)

        # Get user's choice
        choice = input("\nEnter your choice: ").strip()

        # Extract entity based on user's choice
        entity_name, entity_value = extract_entity(text, choice)

        # Display result and insert into MongoDB
        if entity_value:
            print(f"\nExtracted {entity_name}: {entity_value}")
            insert_entity_to_mongo(entity_name, entity_value)
        else:
            print(f"\nNo {entity_name} found in the text.")
    
    except FileNotFoundError:
        print("Error: The specified image path does not exist.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
