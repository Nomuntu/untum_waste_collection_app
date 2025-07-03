import os
import re

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    cleaned_content = re.sub(r'[\u00A0\u200B-\u200D\uFEFF]', ' ', content)
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

def clean_project_directory(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.py'):
                filepath = os.path.join(root, filename)
                clean_file(filepath)
                print(f"Cleaned: {filepath}")

clean_project_directory('.')
