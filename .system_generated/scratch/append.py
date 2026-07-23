def append_css():
    css = """

/* ===================================================
   MODAL STYLES
   =================================================== */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(5px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
}
.modal-overlay.active {
  opacity: 1;
  visibility: visible;
}
.modal-content {
  background: rgba(30, 30, 40, 0.95);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  padding: 2.5rem;
  max-width: 600px;
  width: 90%;
  position: relative;
  transform: translateY(20px);
  transition: transform 0.3s ease;
  box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}
.modal-overlay.active .modal-content {
  transform: translateY(0);
}
.modal-close {
  position: absolute;
  top: 15px;
  right: 15px;
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: white;
  font-size: 1.5rem;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.3s ease;
}
.modal-close:hover {
  background: rgba(255, 255, 255, 0.2);
}
"""
    with open('c:\\Desktop\\sharanangkar\\style.css', 'a', encoding='utf-8') as f:
        f.write(css)

def append_js():
    js = """

/* ---- PROJECT MODAL ---- */
const modal = document.getElementById('projectModal');
const modalClose = document.getElementById('modalClose');
const modalTitle = document.getElementById('modalTitle');
const modalDesc = document.getElementById('modalDesc');
const modalMeta = document.getElementById('modalMeta');

if (modal) {
  document.querySelectorAll('.project-card').forEach(card => {
    card.style.cursor = 'pointer';
    card.addEventListener('click', () => {
      const title = card.querySelector('h3') ? card.querySelector('h3').textContent : 'Project Details';
      const desc = card.querySelector('p').textContent;
      const meta = card.querySelector('.project-meta').innerHTML;
      
      modalTitle.textContent = title;
      modalDesc.textContent = desc;
      modalMeta.innerHTML = meta;
      
      modal.classList.add('active');
    });
  });

  modalClose.addEventListener('click', () => {
    modal.classList.remove('active');
  });
  modal.addEventListener('click', (e) => {
    if(e.target === modal) modal.classList.remove('active');
  });
}
"""
    with open('c:\\Desktop\\sharanangkar\\script.js', 'a', encoding='utf-8') as f:
        f.write(js)

if __name__ == '__main__':
    append_css()
    append_js()
    print("Appended CSS and JS.")
