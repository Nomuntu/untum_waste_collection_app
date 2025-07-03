import sys
import os

def clean_file_of_hidden_characters(file_path):
    # Check if file exists
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return

    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace non-breaking spaces and other non-printable characters
    cleaned_content = ''.join(
        c if c.isprintable() or c in '\n\r\t' else ' ' for c in content
    )

    # Overwrite the file with cleaned content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)

    print(f"File '{file_path}' has been cleaned of hidden characters.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python clean_hidden_chars.py <file_path>")
    else:
        clean_file_of_hidden_characters(sys.argv[1])
