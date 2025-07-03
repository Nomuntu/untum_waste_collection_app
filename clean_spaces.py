
import os

def clean_non_breaking_spaces(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    cleaned_content = content.replace('\u00A0', ' ')
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(cleaned_content)
                    print(f"Cleaned: {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

clean_non_breaking_spaces('.'
