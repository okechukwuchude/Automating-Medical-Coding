import os
import json

def extract_info_from_json(json_file_path):
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
            # Print 'hadm_id' for reference
            print("hadm_id:", hadm_id)
            # Print 'note_id', 'category', and 'description' of the note
            print("note_id:", note.get('note_id', 'N/A'))
            print("category:", note.get('category', 'N/A'))
            print("description:", note.get('description', 'N/A'))
            
            # Extract 'annotations' from the note
            annotations = note.get('annotations', [])
            
            # Iterate through each annotation in the note
            for annotation in annotations:
                # Print annotation details: 'begin', 'end', 'code', 'code_system', 'description', 'type', 'covered_text'
                print("begin:", annotation.get('begin', 'N/A'))
                print("end:", annotation.get('end', 'N/A'))
                print("code:", annotation.get('code', 'N/A'))
                print("code_system:", annotation.get('code_system', 'N/A'))
                print("description:", annotation.get('description', 'N/A'))
                print("type:", annotation.get('type', 'N/A'))
                print("covered_text:", annotation.get('covered_text', 'N/A'))
            
            # Print a separator after each note
            print("-" * 50)

def main(folder_path):
    # Recursively search for JSON files in the folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.json'):
                # Construct the full path to the JSON file
                json_file_path = os.path.join(root, filename)
                print("Processing:", json_file_path)
                # Call extract_info_from_json function to extract information from the JSON file
                extract_info_from_json(json_file_path)
                # Print a separator after processing each file
                print("=" * 50)

if __name__ == "__main__":
    # Specify the path to the folder containing JSON files
    folder_path = r"C:\Users\okechukwu chude\Documents\NLP\text extraction\Automating-Medical-Coding\with_text\gold"
    # Call the main function to start processing JSON files in the folder
    main(folder_path)
