import re

def update_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # We want to remove `<div class="project-tag">...</div>`
    html = re.sub(r'\s*<div class="project-tag">.*?</div>', '', html)
    
    # We want to change the course names to project titles. 
    # We will do this manually for the 14 projects to ensure they make sense.
    replacements = {
        '<h3>Communication Research</h3>': '<h3>BTRC Regulation Study</h3>',
        '<h3>Communication &amp; Technology</h3>': '<h3>Digital Media Landscapes</h3>',
        '<h3>Mass Communication</h3>': '<h3>Mass Media Systems Analysis</h3>',
        '<h3>Advanced English Writing</h3>': '<h3>Journalism & Editorial Writing</h3>',
        '<h3>Advanced Bangla Writing</h3>': '<h3>Bangla Media Production</h3>',
        '<h3>Convergence Communication I &amp; II</h3>': '<h3>Multimedia Storytelling</h3>',
        '<h3>C4D Planning &amp; Process</h3>': '<h3>C4D Strategic Campaign</h3>',
        '<h3>Participatory Research</h3>': '<h3>Community-Based Research</h3>',
        '<h3>ICT for Development</h3>': '<h3>Digital Inclusion Initiatives</h3>',
        '<h3>Health Communication</h3>': '<h3>Public Health Campaigns</h3>',
        '<h3>Emergency Communication</h3>': '<h3>Crisis Communication Strategies</h3>',
        '<h3>Entertainment-Education</h3>': '<h3>Behavior Change Media</h3>',
        '<h3>Environmental Communication</h3>': '<h3>Climate Advocacy & Communication</h3>'
    }
    
    for old, new in replacements.items():
        html = html.replace(old, new)
        
    # Inject the Modal HTML right before closing </body>
    modal_html = """
  <!-- ===== PROJECT MODAL ===== -->
  <div class="modal-overlay" id="projectModal">
    <div class="modal-content glass-card">
      <button class="modal-close" id="modalClose">&times;</button>
      <h3 id="modalTitle" style="margin-bottom: 0.5rem; font-size: 1.5rem;">Project Title</h3>
      <div class="project-meta" id="modalMeta" style="margin-bottom: 1rem;">
      </div>
      <p id="modalDesc" style="color: var(--text-light); line-height: 1.6;">Detailed description goes here.</p>
    </div>
  </div>
"""
    if 'id="projectModal"' not in html:
        html = html.replace('</body>', modal_html + '</body>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Updated HTML.")

if __name__ == '__main__':
    update_html('c:\\Desktop\\sharanangkar\\index.html')
