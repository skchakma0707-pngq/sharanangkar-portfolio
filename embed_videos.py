# -*- coding: utf-8 -*-
import os

projects_to_embed = {
    7: {
        'old': '<p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Video link:</strong> <a href="https://youtu.be/Yxa3hbkOhiQ" target="_blank" style="color: var(--primary); text-decoration: underline;">https://youtu.be/Yxa3hbkOhiQ</a></p>',
        'new': '''<p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Video link:</strong></p>
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; margin-top: 1rem; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
  <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" src="https://www.youtube.com/embed/Yxa3hbkOhiQ" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>'''
    },
    9: {
        'old': '<p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Transect Walk Video Link:</strong> <a href="https://youtu.be/zlEJdzIxfQk?si=oLRnRa5sm81gGHTx" target="_blank" style="color: var(--primary); text-decoration: underline;">https://youtu.be/zlEJdzIxfQk?si=oLRnRa5sm81gGHTx</a></p>',
        'new': '''<p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Transect Walk Video Link:</strong></p>
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; margin-top: 1rem; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
  <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" src="https://www.youtube.com/embed/zlEJdzIxfQk" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>'''
    },
    12: {
        'old': '<p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Fb Page Link:</strong> <a href="https://www.facebook.com/profile.php?id=61584723801062" target="_blank" style="color: var(--primary); text-decoration: underline;">https://www.facebook.com/profile.php?id=61584723801062</a></p>',
        'new': '''<p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Fb Page Link:</strong></p>
<div style="margin-top: 1rem; text-align: center; background: #fff; padding: 10px; border-radius: 12px; display: inline-block;">
  <iframe src="https://www.facebook.com/plugins/page.php?href=https%3A%2F%2Fwww.facebook.com%2Fprofile.php%3Fid%3D61584723801062&tabs=timeline&width=340&height=500&small_header=false&adapt_container_width=true&hide_cover=false&show_facepile=true&appId" width="340" height="500" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>
</div>'''
    },
    13: {
        'old': '<p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Video Link:</strong> <a href="https://youtu.be/IzMdbsmmYhY" target="_blank" style="color: var(--primary); text-decoration: underline;">https://youtu.be/IzMdbsmmYhY</a></p>',
        'new': '''<p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Video Link:</strong></p>
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; margin-top: 1rem; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
  <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" src="https://www.youtube.com/embed/IzMdbsmmYhY" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>'''
    }
}

for pid, data in projects_to_embed.items():
    filepath = f"project-{pid}.html"
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if data['old'] in content:
            content = content.replace(data['old'], data['new'])
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filepath}")
        else:
            print(f"Could not find old text in {filepath}")
