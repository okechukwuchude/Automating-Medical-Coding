import os
import json
import stanza

def extract_info_from_json(json_file_path, sentences):
    # Open the JSON file
    with open(json_file_path, 'r') as file:
        # Load JSON data from the file
        data = json.load(file)
        
        # Extract 'hadm_id' from the JSON data
        hadm_id = data.get('hadm_id', None)
        
        # If 'hadm_id' is not found, print a warning message
        if hadm_id is None:
            print(f"Warning: 'hadm_id' not found in {json_file_path}")
            return None
        
        # Extract 'notes' from the JSON data
        notes = data.get('notes', [])
        
        # Iterate through each note
        for note in notes:
            # Concatenate relevant text fields into a single sentence
            text = f"{note.get('description', '')} {' '.join([annotation.get('covered_text', '') for annotation in note.get('annotations', [])])}"
            # Append the sentence to the sentences list
            sentences.append((hadm_id, text))

def search_files(folder_path, sentences):
    # Recursively search for JSON files in the folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.json'):
                # Construct the full path to the JSON file
                json_file_path = os.path.join(root, filename)
                print("Processing:", json_file_path)
                # Call extract_info_from_json function to extract information from the JSON file
                extract_info_from_json(json_file_path, sentences)
                # Print a separator after processing each file
                print("=" * 50)

# Initialize Stanza pipeline
stanza.download('en')  # Download English model
nlp = stanza.Pipeline('en')  # Initialize English pipeline

# Specify the path to the main folder containing subfolders with JSON files
main_folder_path = r"C:\Users\okechukwu chude\Documents\NLP\text extraction\Automating-Medical-Coding\with_text\gold"

# Initialize list to store sentences
sentences = []

# Call the search_files function to start searching for JSON files in the main folder and its subfolders
search_files(main_folder_path, sentences)

# Process sentences with Stanza
for hadm_id, text in sentences:
    doc = nlp(text)
    print(f"HADM_ID: {hadm_id}")
    for sentence in doc.sentences:
        print("Tokens:", [token.text for token in sentence.tokens])
