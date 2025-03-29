import os

def fix_file(file_path):
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Strip trailing newlines but keep a single newline at the end
    content = content.rstrip() + '\n'
    
    # Write the content back
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Fixed {file_path}")

if __name__ == "__main__":
    template_path = "web/templates/index.html"
    if os.path.exists(template_path):
        fix_file(template_path)
    else:
        print(f"File not found: {template_path}") 