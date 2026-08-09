# -*- coding: utf-8 -*-
import os
import re

for i in range(1, 15):
    filepath = f"project-{i}.html"
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the start of Project Details block
    h3_start = content.find('<h3 style="margin-bottom: 1rem; font-size: 1.5rem;">Project Details</h3>')
    
    # Find the end of the ul and the following <br>
    ul_end_pos = content.find('</ul>', h3_start)
    br_end_pos = content.find('<br>', ul_end_pos)
    
    if h3_start == -1 or ul_end_pos == -1 or br_end_pos == -1:
        print(f"Skipping {filepath} (Project Details not found)")
        continue
        
    details_block = content[h3_start:br_end_pos + 4] # including <br>
    
    # Remove from original location
    content = content.replace(details_block, "")
    
    # modify CSS
    old_css_regex = re.compile(r'\.project-meta-box\s*\{.*?\}', re.DOTALL)
    new_css = '''.project-meta-box {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 2rem;
      margin: 2rem auto 0;
      text-align: left;
      max-width: 800px;
      width: 100%;
    }'''
    content = old_css_regex.sub(new_css, content)
    
    # Replace the contents of .project-meta-box
    box_start = content.find('<div class=\"project-meta-box\">')
    box_end = content.find('</div>', box_start)
    
    # Remove the old ?? Summer 2022 / ?? Research things from meta-box by slicing
    styled_details = details_block.replace('<h3 style=\"margin-bottom: 1rem; font-size: 1.5rem;\">', '<h3 style=\"margin-bottom: 1rem; font-size: 1.5rem; color: #fff;\">')
    styled_details = styled_details.replace('color: var(--text-light);', 'color: rgba(255, 255, 255, 0.9);')
    # Let's drop the <br> from the end
    styled_details = styled_details.replace('<br>', '')
    
    new_box = f'<div class=\"project-meta-box\">\n      {styled_details}\n    </div>'
    
    content = content[:box_start] + new_box + content[box_end + 6:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")
