import re

def update_html():
    file_path = 'c:\\Desktop\\sharanangkar\\index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Add social card below the badge card
    social_html = """
      <div class="avatar-badge-card">
        <div class="abc-icon">📸</div>
        <div>
          <div class="abc-title">Visual Storyteller</div>
          <div class="abc-sub">&amp; Photographer</div>
        </div>
      </div>
      <div class="hero-social-card">
        <a href="https://wa.me/8801781091604" target="_blank" title="WhatsApp" class="social-icon">📞</a>
        <a href="https://www.linkedin.com/in/sharananngkar-chakma-b453b4306/?locale=en" target="_blank" title="LinkedIn" class="social-icon">🔗</a>
        <a href="https://www.facebook.com/saranankara.canama/" target="_blank" title="Facebook" class="social-icon">📘</a>
      </div>"""
      
    # Target exact badge block
    badge_block = """      <div class="avatar-badge-card">
        <div class="abc-icon">📸</div>
        <div>
          <div class="abc-title">Visual Storyteller</div>
          <div class="abc-sub">&amp; Photographer</div>
        </div>
      </div>"""
      
    if "hero-social-card" not in html:
        html = html.replace(badge_block, social_html)

    # Change all project arrows to say "View Details"
    html = html.replace('<div class="project-arrow">→</div>', 
                        '<div class="project-arrow" style="font-size: 0.9rem; font-weight: 500;">View Details &rarr;</div>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)


def append_css():
    css = """

/* ===================================================
   HERO SOCIAL CARD
   =================================================== */
.hero-social-card {
  position: absolute;
  bottom: 0px;
  right: -20px;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 0.8rem 1rem;
  border-radius: 50px;
  display: flex;
  gap: 1rem;
  z-index: 5;
  box-shadow: 0 10px 30px rgba(0,0,0,0.5);
  animation: float 4s ease-in-out infinite reverse;
}
.social-icon {
  text-decoration: none;
  font-size: 1.2rem;
  transition: transform 0.3s ease;
  display: inline-block;
}
.social-icon:hover {
  transform: scale(1.2) translateY(-3px);
}
@media (max-width: 991px) {
  .hero-social-card {
    right: 50%;
    transform: translateX(50%);
    bottom: -10px;
  }
}
"""
    with open('c:\\Desktop\\sharanangkar\\style.css', 'a', encoding='utf-8') as f:
        f.write(css)

if __name__ == '__main__':
    update_html()
    append_css()
    print("Done")
