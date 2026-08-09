import json
import re

with open('user_inputs.jsonl', 'r', encoding='utf-8') as f:
    text = f.read()

# Since Select-String output wraps lines, we can just find { ... }
objects = []
idx = 0
while True:
    start = text.find('{"step_index"', idx)
    if start == -1:
        break
    # find the next line that starts with C:\Users... which means the next match, or EOF
    next_start = text.find('C:\\Users\\HP', start + 1)
    if next_start == -1:
        obj_str = text[start:]
        idx = len(text)
    else:
        # the match ends before the next C:\Users... minus newlines
        obj_str = text[start:next_start].strip()
        idx = next_start
    
    # replace newlines in the JSON string that might have been broken by Select-String wrapping
    obj_str = re.sub(r'\n', '', obj_str)
    
    try:
        data = json.loads(obj_str)
        objects.append(data['content'])
    except Exception as e:
        print(f"Failed to parse object at {start}: {e}")

all_content = '\n'.join(objects)
print("Extracted total content length:", len(all_content))

import io
with io.open('raw_projects.txt', 'w', encoding='utf-8') as f:
    f.write(all_content)
