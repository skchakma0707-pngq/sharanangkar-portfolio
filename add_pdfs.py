# -*- coding: utf-8 -*-
import os

pdf_mapping = {
    1: "Research Proposal_ “The Perception of BTRC Regulation for Digital, Social Media and  OTT Platform, 2021 (Draft) among Content Creators and  Communication Experts”.pdf",
    3: "Polarizations in International Relation.pdf",
    4: "Press Release for Biju Festival & seasonal feature.pdf",
    5: "বজলুর রহমান, সাংবাদিক।.pdf",
    6: "Trashion Show Report.pdf",
    8: "Project Green Dhaka_ Empowering Students Through Environmental Education and Indoor Planting.pdf",
    9: "Exploring Student Perspectives through Transect Walk and Resource Mapping_ A Case Study of ULAB Campus.pdf",
    10: "ICT for Development.pdf",
    11: "Health Communication .pdf",
    12: "Public Health Emergency - Emergency and Risk Communication During a Foodborne Illness Outbreak in Dhaka, Bangladesh.pdf",
    14: "Tourism-Induced Soil Pollution in the Chittagong Hill Tracts_ Environmental Challenges and Sustainable Solutions.pdf"
}

for pid, filename in pdf_mapping.items():
    filepath = f"project-{pid}.html"
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        button_html = f'''
    <div style="margin-top: 3rem; text-align: center;">
      <a href="pdfs/{filename}" target="_blank" class="btn btn-primary" style="display: inline-block; padding: 12px 24px; background-color: var(--primary); color: #fff; text-decoration: none; border-radius: 8px; font-weight: 600; transition: background-color 0.3s; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);">📄 View Full PDF</a>
    </div>
  </section>'''
        
        if "📄 View Full PDF" not in content:
            content = content.replace('  </section>\n\n  <!-- ===== FOOTER ===== -->', button_html + '\n\n  <!-- ===== FOOTER ===== -->')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filepath}")
