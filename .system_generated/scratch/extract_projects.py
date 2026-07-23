import re
import os

def process():
    file_path = 'c:\\Desktop\\sharanangkar\\index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find all project cards
    # A project card looks like:
    # <div class="project-card glass-card reveal-up" style="--delay:0s">
    #   <div class="project-number">01</div>
    #   <h3>BTRC Regulation Study</h3>
    #   <p>...</p>
    #   <div class="project-meta">...</div>
    #   <div class="project-arrow" style="...">View Details &rarr;</div>
    # </div>
    
    # We will use regex to extract project details and replace the card with an <a> tag link
    
    # Let's parse them manually by finding '<div class="project-card'
    cards = re.finditer(r'(<div class="project-card.*?>)(.*?)(<div class="project-arrow".*?>.*?</div>\s*</div>)', html, re.DOTALL)
    
    new_html = html
    projects = []
    
    for i, match in enumerate(cards):
        idx = i + 1
        full_card = match.group(0)
        start_tag = match.group(1)
        content = match.group(2)
        end_tag = match.group(3)
        
        # Extract title and desc
        title_match = re.search(r'<h3>(.*?)</h3>', content)
        title = title_match.group(1) if title_match else f"Project {idx}"
        
        p_match = re.search(r'<p>(.*?)</p>', content, re.DOTALL)
        desc = p_match.group(1) if p_match else ""
        
        meta_match = re.search(r'<div class="project-meta">(.*?)</div>', content, re.DOTALL)
        meta = meta_match.group(1) if meta_match else ""
        
        projects.append({
            'id': idx,
            'title': title,
            'desc': desc,
            'meta': meta
        })
        
        # Replace the <div class="project-arrow"> with an anchor tag wrapping it
        # Actually, let's just make the whole card clickable, or just the View Details button.
        # User wants "when anyone click on any project it will enter in a new page"
        # Best way is to wrap the whole card contents in an <a> tag, or add an onclick handler.
        # Let's change the project-arrow to an actual <a> tag.
        
        new_arrow = f'<a href="project-{idx}.html" class="project-arrow" style="font-size: 0.9rem; font-weight: 500; text-decoration: none; color: inherit; display: inline-block; margin-top: 1rem;">View Details &rarr;</a>\n        </div>'
        
        # We can just replace the end tag
        new_card = start_tag + content + new_arrow
        new_html = new_html.replace(full_card, new_card)
        
    # Remove modal html
    modal_regex = r'<!-- ===== PROJECT MODAL ===== -->.*?</div>\s*</div>'
    new_html = re.sub(modal_regex, '', new_html, flags=re.DOTALL)
    
    # Fix social links: Move them to be visibly beside the avatar.
    # The previous social card was:
    # <div class="hero-social-card">...</div>
    # Let's remove it and place a new one vertically next to the image.
    social_card_regex = r'<div class="hero-social-card">.*?</div>'
    new_html = re.sub(social_card_regex, '', new_html, flags=re.DOTALL)
    
    # We will inject the social links inside the hero-content instead, or absolutely positioned but better.
    # User said: "communication channel need to show in first page beside the image of the man"
    # Let's put it inside `.hero-avatar` but with a clear relative positioning or just a flex row below it.
    new_social_html = """
      <div class="hero-social-card-new" style="margin-top: 2rem; display: flex; gap: 1.5rem; justify-content: center;">
        <a href="https://wa.me/8801781091604" target="_blank" title="WhatsApp" style="font-size: 1.8rem; text-decoration: none; transition: transform 0.3s; display: inline-block;">📞</a>
        <a href="https://www.linkedin.com/in/sharananngkar-chakma-b453b4306/?locale=en" target="_blank" title="LinkedIn" style="font-size: 1.8rem; text-decoration: none; transition: transform 0.3s; display: inline-block;">🔗</a>
        <a href="https://www.facebook.com/saranankara.canama/" target="_blank" title="Facebook" style="font-size: 1.8rem; text-decoration: none; transition: transform 0.3s; display: inline-block;">📘</a>
      </div>
    """
    
    # Let's insert it right after the avatar-badge-card
    badge_card = """<div class="avatar-badge-card">
        <div class="abc-icon">📸</div>
        <div>
          <div class="abc-title">Visual Storyteller</div>
          <div class="abc-sub">&amp; Photographer</div>
        </div>
      </div>"""
    
    if badge_card in new_html:
        new_html = new_html.replace(badge_card, badge_card + new_social_html)

    # Write the updated index.html
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_html)

    # Now generate the 13 project pages
    template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{title} | Sharananngkar Chakma</title>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="style.css"/>
  <style>
    .project-detail-hero {{
      padding: 150px 0 100px;
      text-align: center;
      background: linear-gradient(180deg, rgba(30, 30, 40, 0) 0%, rgba(30, 30, 40, 1) 100%);
    }}
    .project-detail-content {{
      max-width: 800px;
      margin: 0 auto;
      padding: 0 20px 100px;
    }}
    .back-btn {{
      display: inline-block;
      margin-bottom: 2rem;
      color: var(--primary);
      text-decoration: none;
      font-weight: 500;
      transition: color 0.3s;
    }}
    .back-btn:hover {{
      color: var(--text-light);
    }}
    .project-meta-box {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 1.5rem;
      margin-top: 2rem;
      display: flex;
      justify-content: center;
      gap: 2rem;
    }}
  </style>
</head>
<body>
  <!-- ===== NAVBAR ===== -->
  <nav class="navbar scrolled" id="navbar">
    <div class="nav-brand">
      <span class="brand-initials">SC</span>
      <span class="brand-name">Sharananngkar</span>
    </div>
    <ul class="nav-links">
      <li><a href="index.html#projects" class="nav-link">Back to Portfolio</a></li>
    </ul>
  </nav>

  <section class="project-detail-hero">
    <div class="container">
      <a href="index.html#projects" class="back-btn">&larr; Back to Projects</a>
      <h1 class="hero-title">{title}</h1>
      <div class="project-meta-box">
        {meta}
      </div>
    </div>
  </section>

  <section class="project-detail-content">
    <h3 style="margin-bottom: 1rem; font-size: 1.5rem;">Project Overview</h3>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">{desc}</p>
    <br><br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">This project was undertaken as part of my comprehensive academic and professional development. It demonstrates practical application of theory, strategic planning, and effective communication methodologies.</p>
  </section>

  <!-- ===== FOOTER ===== -->
  <footer class="footer">
    <div class="container">
      <div class="footer-content">
        <p class="footer-copy">© 2026 Sharananngkar Chakma</p>
      </div>
    </div>
  </footer>
</body>
</html>"""

    for p in projects:
        page_content = template.format(title=p['title'], meta=p['meta'], desc=p['desc'])
        with open(f"c:\\Desktop\\sharanangkar\\project-{p['id']}.html", 'w', encoding='utf-8') as pf:
            pf.write(page_content)
            
    # Also clean script.js modal logic
    with open('c:\\Desktop\\sharanangkar\\script.js', 'r', encoding='utf-8') as f:
        js = f.read()
    js = re.sub(r'/\* ---- PROJECT MODAL ---- \*/.*', '', js, flags=re.DOTALL)
    with open('c:\\Desktop\\sharanangkar\\script.js', 'w', encoding='utf-8') as f:
        f.write(js)

if __name__ == '__main__':
    process()
    print("Projects generated and HTML updated.")
