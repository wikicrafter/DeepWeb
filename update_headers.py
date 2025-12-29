import os
import re

# Mapping of file titles to their box-drawing ASCII art
headers = {
    "0x00_what_is_deep_web.md": """```text
 ██████╗ ███████╗███████╗██████╗     ██╗    ██╗███████╗██████╗ 
 ██╔══██╗██╔════╝██╔════╝██╔══██╗    ██║    ██║██╔════╝██╔══██╗
 ██║  ██║█████╗  █████╗  ██████╔╝    ██║ █╗ ██║█████╗  ██████╔╝
 ██║  ██║██╔══╝  ██╔══╝  ██╔═══╝     ██║███╗██║██╔══╝  ██╔══██╗
 ██████╔╝███████╗███████╗██║         ╚███╔███╔╝███████╗██████╔╝
 ╚═════╝ ╚══════╝╚══════╝╚═╝          ╚══╝╚══╝ ╚══════╝╚═════╝ 
```""",
    "0x01_myths_and_misconceptions.md": """```text
 ███╗   ███╗██╗   ██╗████████╗██╗  ██╗███████╗
 ████╗ ████║╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔════╝
 ██╔████╔██║ ╚████╔╝    ██║   ███████║███████╗
 ██║╚██╔╝██║  ╚██╔╝     ██║   ██╔══██║╚════██║
 ██║ ╚═╝ ██║   ██║      ██║   ██║  ██║███████║
 ╚═╝     ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝╚══════╝
```""",
    "0x02_how_tor_works.md": """```text
 ████████╗ ██████╗ ██████╗ 
 ╚══██╔══╝██╔═══██╗██╔══██╗
    ██║   ██║   ██║██████╔╝
    ██║   ██║   ██║██╔══██╗
    ██║   ╚██████╔╝██║  ██║
    ╚═╝    ╚═════╝ ╚═╝  ╚═╝
```""",
    "0x03_what_is_pgp.md": """```text
 ██████╗  ██████╗ ██████╗ 
 ██╔══██╗██╔════╝ ██╔══██╗
 ██████╔╝██║  ███╗██████╔╝
 ██╔═══╝ ██║   ██║██╔═══╝ 
 ██║     ╚██████╔╝██║     
 ╚═╝      ╚═════╝ ╚═╝     
```""",
    "0x04_dont_use_windows.md": """```text
 ██╗    ██╗██╗███╗   ██╗██████╗  ██████╗ ██╗    ██╗███████╗
 ██║    ██║██║████╗  ██║██╔══██╗██╔═══██╗██║    ██║██╔════╝
 ██║ █╗ ██║██║██╔██╗ ██║██║  ██║██║   ██║██║ █╗ ██║███████╗
 ██║███╗██║██║██║╚██╗██║██║  ██║██║   ██║██║███╗██║╚════██║
 ╚███╔███╔╝██║██║ ╚████║██████╔╝╚██████╔╝╚███╔███╔╝███████║
  ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚══════╝
```""",
}

# For files without custom headers, use a generic "MODULE" header
generic_header = """```text
 ███╗   ███╗ ██████╗ ██████╗ ██╗   ██╗██╗     ███████╗
 ████╗ ████║██╔═══██╗██╔══██╗██║   ██║██║     ██╔════╝
 ██╔████╔██║██║   ██║██║  ██║██║   ██║██║     █████╗  
 ██║╚██╔╝██║██║   ██║██║  ██║██║   ██║██║     ██╔══╝  
 ██║ ╚═╝ ██║╚██████╔╝██████╔╝╚██████╔╝███████╗███████╗
 ╚═╝     ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
```"""

base_path = r"c:\Development\DeepWeb\data"

for filename in os.listdir(base_path):
    if filename.endswith('.md'):
        filepath = os.path.join(base_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Get the appropriate header
        new_header = headers.get(filename, generic_header)
        
        # Replace the old ASCII art (everything between first ``` and second ```)
        pattern = r'^```text\n.*?```'
        replacement = new_header
        
        new_content = re.sub(pattern, replacement, content, count=1, flags=re.DOTALL | re.MULTILINE)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("All headers updated successfully!")
