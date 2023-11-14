import base64
import os
import json

folder_path = input()

# Function to convert a file to Base64
def file_to_base64(file_path):
    try:
        with open(file_path, 'rb') as pdf_file:
            # Read the PDF file as binary data
            pdf_binary_data = pdf_file.read()

            # Encode the binary data as Base64
            base64_data = base64.b64encode(pdf_binary_data).decode('utf-8')

            return base64_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        # Construct the full file path
        full_file_path = os.path.join(folder_path, filename)

        # Extract the file name without the extension
        file_name_without_extension = os.path.splitext(filename)[0]

        # Convert the PDF to Base64
        base64_pdf = file_to_base64(full_file_path)

        if base64_pdf:
            # Create the JSON structure
            data = {
                "email": {
                    "Attachments": [
                        {
                            "Name": filename,
                            "ContentBytes": base64_pdf
                        }
                    ]
                }
            }

            # Define the output JSON file path
            output_json_file = f'{file_name_without_extension}.json'

            # Write the JSON data to the output file
            with open(output_json_file, 'w') as json_file:
                json.dump(data, json_file, indent=4)

            # Print a message indicating where the data was saved
            print(f"JSON data for {filename} saved to {output_json_file}")
