# -*- coding: utf-8 -*-
import re
import os

projects = {
    1: """
    <h3 style="margin-bottom: 1rem; font-size: 1.5rem;">Project Details</h3>
    <ul style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light); list-style-type: none; padding: 0;">
      <li style="margin-bottom: 0.5rem;"><strong>Course Code & Name:</strong> MSJ11102: Communication Research</li>
      <li style="margin-bottom: 0.5rem;"><strong>Project Name:</strong> The Perception of BTRC Regulation for Digital, Social Media and OTTPlatform, 2021 (Draft) among Content Creators and Communication Experts</li>
      <li style="margin-bottom: 0.5rem;"><strong>Date/Semester:</strong> Summer 2022</li>
    </ul>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">This research explores how content creators and communication experts perceive the proposed Bangladesh Telecommunication Regulatory Commission (BTRC) Regulation for Digital, Social Media and OTT Platforms, 2021 (Draft). As digital media, social media, and OTT platforms continue to transform entertainment and communication in Bangladesh, the proposed regulation has generated significant debate regarding online content governance, freedom of expression, and consumer protection.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">The study aims to examine whether the proposed regulation is viewed as a necessary framework for ensuring online safety and national security or as a potential restriction on creative freedom and independent content production. By collecting opinions from content creators and communication experts through qualitative in-depth interviews, the research seeks to identify both the anticipated benefits and possible challenges of implementing the regulation.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">The research specifically focuses on understanding stakeholders' perceptions, evaluating the expected impact of the regulation on digital content creation, and assessing the necessity of regulatory intervention in Bangladesh's rapidly expanding digital media ecosystem. Findings are expected to provide valuable insights for policymakers, researchers, media professionals, and digital content creators by highlighting concerns, expectations, and recommendations regarding future regulatory policies.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">This qualitative study employs convenience sampling, interviewing 20 participants (10 content creators and 10 communication experts). The research is planned over 120 days with an estimated budget of BDT 80,000, covering literature review, data collection, analysis, and report preparation.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">Overall, the study contributes to the growing discussion on balancing digital governance, freedom of expression, consumer protection, and the sustainable development of Bangladesh's digital content industry.</p>
    """,
    2: """
    <h3 style="margin-bottom: 1rem; font-size: 1.5rem;">Project Details</h3>
    <ul style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light); list-style-type: none; padding: 0;">
      <li style="margin-bottom: 0.5rem;"><strong>Course Code & Name:</strong> MSJ 2101: Communication & Technology</li>
      <li style="margin-bottom: 0.5rem;"><strong>Project Name:</strong> Stories of Successful protest (Blog Post)</li>
      <li style="margin-bottom: 0.5rem;"><strong>Date/Semester:</strong> Spring 2023</li>
    </ul>
    <br>
    <h4 style="font-size: 1.3rem; margin-bottom: 1rem;">Stories of Successful Protests in Bangladesh: The Role of Mobilization Theory</h4>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Category:</strong> Academic Blog | Social Movements | Digital Communication</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">This blog explores how Mobilization Theory explains the success of major social movements in Bangladesh, particularly the #MeToo Bangladesh and Safe Road Movement. It discusses how social media has transformed public participation by enabling citizens to organize collective action, raise awareness, and advocate for social justice. The article highlights the role of digital platforms in strengthening civic engagement and demonstrates how communication technologies can influence public opinion and contribute to meaningful social change.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Keywords:</strong> Mobilization Theory, Social Movement, #MeToo Bangladesh, Safe Road Movement, Digital Activism, Social Media, Communication for Development (C4D), Bangladesh.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Bloglink:</strong> <a href="https://sharananngkarchakma.blogspot.com/2023/04/stories-of-successful-protest.html" target="_blank" style="color: var(--primary); text-decoration: underline;">https://sharananngkarchakma.blogspot.com/2023/04/stories-of-successful-protest.html</a></p>
    """,
    3: """
    <h3 style="margin-bottom: 1rem; font-size: 1.5rem;">Project Details</h3>
    <ul style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light); list-style-type: none; padding: 0;">
      <li style="margin-bottom: 0.5rem;"><strong>Course Code & Name:</strong> MSJ 2201: Mass Communication</li>
      <li style="margin-bottom: 0.5rem;"><strong>Project Name:</strong> Polarizations in International Relation</li>
      <li style="margin-bottom: 0.5rem;"><strong>Date/Semester:</strong> Summer 23</li>
    </ul>
    <br>
    <h4 style="font-size: 1.3rem; margin-bottom: 1rem;">Polarization in International Politics</h4>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Category:</strong> Academic Blog | International Politics | Global Affairs</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">This blog examines the concept of polarization in international politics through the lens of contemporary global power dynamics. It explores how ideological divisions, geopolitical competition, and strategic alliances have reshaped international relations, with particular attention to the growing divide between Western countries and the strategic partnership of Russia and China.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">The article also reflects on a collaborative curriculum integration (CI) project where our team designed and exhibited a symbolic mask representing global polarization. Through visual storytelling, the artwork illustrated how political conflicts, particularly the Russia–Ukraine war, have contributed to increasing divisions in the international system. By combining academic research with creative expression, the project highlights the importance of understanding global conflicts, diplomacy, and the impact of polarization on today's interconnected world.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Keywords:</strong> International Politics, Polarization, Geopolitics, Russia, China, Western Alliance, Russia-Ukraine War, Curriculum Integration, Global Affairs.</p>
    """,
    4: """
    <h3 style="margin-bottom: 1rem; font-size: 1.5rem;">Project Details</h3>
    <ul style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light); list-style-type: none; padding: 0;">
      <li style="margin-bottom: 0.5rem;"><strong>Course Code & Name:</strong> GEF 1202: Advance English Writing Skills</li>
      <li style="margin-bottom: 0.5rem;"><strong>Project Name:</strong> Press Release for Biju Festival & seasonal feature</li>
      <li style="margin-bottom: 0.5rem;"><strong>Date/Semester:</strong> Spring 2022</li>
    </ul>
    <br>
    <h4 style="font-size: 1.3rem; margin-bottom: 1rem;">Biju, Sangrai, Baisu & Bihu: Celebrating the Cultural Heritage of the Jumma People</h4>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Category:</strong> Cultural Blog | Indigenous Heritage | Chittagong Hill Tracts</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">This blog explores the rich cultural heritage of the Jumma indigenous communities of the Chittagong Hill Tracts through their traditional New Year festivals - Biju, Sangrai (Sangraing), Baisu, Bishu, Sankran, and Bihu. It highlights the historical significance, cultural values, traditional rituals, indigenous cuisine, water festivals, religious practices, and community celebrations that strengthen unity, identity, and social harmony among different indigenous groups.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">The article also reflects on the importance of preserving indigenous cultural heritage, protecting the rights and identity of the Jumma people, and promoting cultural diversity in Bangladesh. Through photographs and firsthand observations, the blog documents the vibrant traditions, ceremonies, and festivities that continue to connect generations and celebrate the unique identity of the indigenous communities.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Keywords:</strong> Biju Festival, Sangrai Festival, Jumma People, Indigenous Culture, Chittagong Hill Tracts, Cultural Heritage, Bangladesh, Traditional Festivals, Indigenous Rights.</p>
    """,
    5: """
    <h3 style="margin-bottom: 1rem; font-size: 1.5rem;">Project Details</h3>
    <ul style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light); list-style-type: none; padding: 0;">
      <li style="margin-bottom: 0.5rem;"><strong>Course Code & Name:</strong> GEF 1203: Advance Bangla Writing Skills</li>
      <li style="margin-bottom: 0.5rem;"><strong>Project Name:</strong> বজলুর রহমান, সাংবাদিক</li>
      <li style="margin-bottom: 0.5rem;"><strong>Date/Semester:</strong> Summer 2022</li>
    </ul>
    <br>
    <h4 style="font-size: 1.3rem; margin-bottom: 1rem;">কিংবদন্তি সাংবাদিক বজলুর রহমান</h4>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Category:</strong> Biography | Journalism | Bangladesh</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">এই লেখায় বাংলাদেশের প্রখ্যাত সাংবাদিক, মুক্তিযোদ্ধা, সংস্কৃতিকর্মী ও রাজনীতিবিদ বজলুর রহমান-এর জীবন, কর্ম এবং দেশের সাংবাদিকতা ও জাতীয় উন্নয়নে তাঁর অসামান্য অবদান তুলে ধরা হয়েছে। তাঁর পেশাগত সাফল্য, মুক্তিযুদ্ধে ভূমিকা, অর্থনৈতিক চিন্তাভাবনা এবং গণমাধ্যমে নেতৃত্বের মাধ্যমে কীভাবে তিনি বাংলাদেশের ইতিহাসে একজন অনুকরণীয় ব্যক্তিত্ব হয়ে উঠেছেন, তা সংক্ষেপে উপস্থাপন করা হয়েছে।</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Keywords:</strong> Bazlur Rahman, Journalism, Liberation War, Bangladesh, Media, Biography, Freedom Fighter.</p>
    """,
    6: """
    <h3 style="margin-bottom: 1rem; font-size: 1.5rem;">Project Details</h3>
    <ul style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light); list-style-type: none; padding: 0;">
      <li style="margin-bottom: 0.5rem;"><strong>Course Code & Name:</strong> MSJ 2102: Convergence Communication 1</li>
      <li style="margin-bottom: 0.5rem;"><strong>Project Name:</strong> The threads of triumph</li>
      <li style="margin-bottom: 0.5rem;"><strong>Date/Semester:</strong> Spring 2024</li>
    </ul>
    <br>
    <h4 style="font-size: 1.3rem; margin-bottom: 1rem;">The Threads of Triumph</h4>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Category:</strong> Creative Project | Trashion Show | Curriculum Integration (CI)</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">The Threads of Triumph is a collaborative trashion fashion project inspired by the theme "Desired Difficulty." Using recycled materials such as cardboard, paper bags, OMR sheets, bubble wrap, and polythene, our team designed two symbolic outfits representing the journey from failure to success in student life. The project demonstrates that perseverance, resilience, and continuous effort are essential ingredients for achieving success. Through sustainable fashion and creative storytelling, this work highlights how challenges shape personal growth while promoting environmental awareness through the reuse of discarded materials.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Keywords:</strong> Desired Difficulty, Trashion Show, Sustainable Fashion, Recycled Materials, Curriculum Integration, Creative Project, Student Life, Teamwork.</p>
    """,
    7: """
    <h3 style="margin-bottom: 1rem; font-size: 1.5rem;">Project Details</h3>
    <ul style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light); list-style-type: none; padding: 0;">
      <li style="margin-bottom: 0.5rem;"><strong>Course Code & Name:</strong> MSJ 2202: Convergence Communication 2</li>
      <li style="margin-bottom: 0.5rem;"><strong>Project Name:</strong> Dark Hope</li>
      <li style="margin-bottom: 0.5rem;"><strong>Date/Semester:</strong> Spring 2024</li>
    </ul>
    <br>
    <h4 style="font-size: 1.3rem; margin-bottom: 1rem;">Dark Hope</h4>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Category:</strong> Short Film | Visual Storytelling | Curriculum Integration (CI)</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">Dark Hope is a conceptual short film inspired by the Curriculum Integration theme "Desired Difficulty." The project portrays the emotional and financial struggles many students face while pursuing higher education. Through symbolic visuals, such as candles, books, darkness, and empty wallets, the film illustrates how academic pressure, financial hardship, negative influences, and frustration can gradually diminish hope and dreams. Rather than focusing solely on success, the film encourages viewers to recognize the hidden challenges behind educational journeys and emphasizes the importance of resilience, positive choices, and perseverance in overcoming adversity.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Keywords:</strong> Desired Difficulty, Short Film, Student Life, Higher Education, Mental Health, Visual Storytelling, Curriculum Integration, Hope and Resilience.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Video link:</strong> <a href="https://youtu.be/Yxa3hbkOhiQ" target="_blank" style="color: var(--primary); text-decoration: underline;">https://youtu.be/Yxa3hbkOhiQ</a></p>
    """,
    8: """
    <h3 style="margin-bottom: 1rem; font-size: 1.5rem;">Project Details</h3>
    <ul style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light); list-style-type: none; padding: 0;">
      <li style="margin-bottom: 0.5rem;"><strong>Course Code & Name:</strong> MSJ 2262: C4D Planning & Process</li>
      <li style="margin-bottom: 0.5rem;"><strong>Project Name:</strong> Project Green Dhaka: Empowering Students Through Environmental Education and Indoor Planting</li>
      <li style="margin-bottom: 0.5rem;"><strong>Date/Semester:</strong> Summer 2024</li>
    </ul>
    <br>
    <h4 style="font-size: 1.3rem; margin-bottom: 1rem;">Project Green Dhaka: Empowering Students Through Environmental Education and Indoor Planting</h4>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Category:</strong> Communication for Development (C4D) | Environmental Sustainability | Academic Project</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">Project Green Dhaka is a Communication for Development (C4D) initiative designed to promote environmental sustainability through environmental education and indoor planting in schools. The project encourages students to develop environmentally responsible habits by integrating green practices into the education system. Focusing on pollution reduction, community participation, and long-term behavioral change, the initiative presents a sustainable model for creating greener learning environments while inspiring future generations to contribute to a cleaner and healthier Bangladesh.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Keywords:</strong> Environmental Education, Indoor Planting, Green Dhaka, Sustainability, C4D, Pollution Reduction, Climate Action, Student Engagement.</p>
    """,
    9: """
    <h3 style="margin-bottom: 1rem; font-size: 1.5rem;">Project Details</h3>
    <ul style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light); list-style-type: none; padding: 0;">
      <li style="margin-bottom: 0.5rem;"><strong>Course Code & Name:</strong> MSJ 3161: Participatory Research</li>
      <li style="margin-bottom: 0.5rem;"><strong>Project Name:</strong> Exploring Student Perspectives through Transect Walk and Resource Mapping: A Case Study of ULAB Campus</li>
      <li style="margin-bottom: 0.5rem;"><strong>Date/Semester:</strong> Summer 2025</li>
    </ul>
    <br>
    <h4 style="font-size: 1.3rem; margin-bottom: 1rem;">Exploring Student Perspectives through Transect Walk and Resource Mapping: A Case Study of ULAB Campus</h4>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Category:</strong> Participatory Research | Communication for Development (C4D) | Academic Project</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">This participatory research project explores students’ experiences and perspectives at the University of Liberal Arts Bangladesh (ULAB) using Transect Walk, Resource Mapping, and Farmers Field School (FFS) methodologies. By actively engaging students as co-researchers, the study identifies key strengths and challenges within the campus environment, including classrooms, library, cafeteria, toilets, common spaces, and recreational areas. Based on participants' insights, the project proposes practical, student-centered recommendations to improve campus facilities, promote sustainable development, and strengthen student participation in institutional decision-making.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Keywords:</strong> Participatory Research, Transect Walk, Resource Mapping, FFS, ULAB, Student Engagement, Campus Development, Communication for Development (C4D).</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Transect Walk Video Link:</strong> <a href="https://youtu.be/zlEJdzIxfQk?si=oLRnRa5sm81gGHTx" target="_blank" style="color: var(--primary); text-decoration: underline;">https://youtu.be/zlEJdzIxfQk?si=oLRnRa5sm81gGHTx</a></p>
    """,
    10: """
    <h3 style="margin-bottom: 1rem; font-size: 1.5rem;">Project Details</h3>
    <ul style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light); list-style-type: none; padding: 0;">
      <li style="margin-bottom: 0.5rem;"><strong>Course Code & Name:</strong> MSJ 3261: ICT for Development</li>
      <li style="margin-bottom: 0.5rem;"><strong>Project Name:</strong> ICT for Sustainable Development in Bangladesh: Challenges, Opportunities and Future Prospects</li>
      <li style="margin-bottom: 0.5rem;"><strong>Date/Semester:</strong> Fall 2024</li>
    </ul>
    <br>
    <h4 style="font-size: 1.3rem; margin-bottom: 1rem;">ICT for Sustainable Development in Bangladesh</h4>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Category:</strong> ICT | Sustainable Development | Academic Review</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">This paper examines the role of *Information and Communication Technology (ICT)* in advancing sustainable development in Bangladesh. It discusses how initiatives such as *Digital Bangladesh* and *Vision 2041* are transforming governance, education, healthcare, agriculture, and economic development through digital innovation. The study also highlights key challenges—including the digital divide, infrastructural limitations, policy implementation gaps, and socio-economic inequalities—while exploring future opportunities for smart cities, environmental sustainability, and youth empowerment. Overall, the paper emphasizes the importance of inclusive ICT policies and strategic investments to achieve long-term sustainable development in Bangladesh.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Keywords:</strong> ICT, Sustainable Development, Digital Bangladesh, Vision 2041, E-Governance, Digital Inclusion, Smart Cities, Bangladesh.</p>
    """,
    11: """
    <h3 style="margin-bottom: 1rem; font-size: 1.5rem;">Project Details</h3>
    <ul style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light); list-style-type: none; padding: 0;">
      <li style="margin-bottom: 0.5rem;"><strong>Course Code & Name:</strong> MSJ 3262: Health Communication</li>
      <li style="margin-bottom: 0.5rem;"><strong>Project Name:</strong> Health related problems and changing health behaviors in Chittagong Hill Tracts</li>
      <li style="margin-bottom: 0.5rem;"><strong>Date/Semester:</strong> Summer 2024</li>
    </ul>
    <br>
    <h4 style="font-size: 1.3rem; margin-bottom: 1rem;">Improving Healthcare Access and Health Behavior in the Chittagong Hill Tracts</h4>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Category:</strong> Communication for Development (C4D) | Public Health | Academic Project</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">This project focuses on improving healthcare access and promoting positive health behavior among communities in the *Chittagong Hill Tracts (CHT). It examines the major healthcare challenges faced by remote indigenous communities, including limited medical facilities, inadequate health services, low health awareness, and geographical barriers. Drawing on the **Health Belief Model* and *Social Learning Theory*, the project proposes community-based interventions such as health awareness campaigns, educational programs, behavior change communication, and strengthened community clinic services. The initiative aims to encourage preventive healthcare practices, improve trust in modern medical services, and contribute to equitable and sustainable healthcare development in the Chittagong Hill Tracts.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Keywords:</strong> Chittagong Hill Tracts, Public Health, Health Behavior Change, Communication for Development, Health Belief Model, Social Learning Theory, Community Health, Bangladesh.</p>
    """,
    12: """
    <h3 style="margin-bottom: 1rem; font-size: 1.5rem;">Project Details</h3>
    <ul style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light); list-style-type: none; padding: 0;">
      <li style="margin-bottom: 0.5rem;"><strong>Course Code & Name:</strong> MSJ 3263: Emergency Communication</li>
      <li style="margin-bottom: 0.5rem;"><strong>Project Name:</strong> Public Health Emergency - Emergency and Risk Communication During a Foodborne Illness Outbreak in Dhaka, Bangladesh</li>
      <li style="margin-bottom: 0.5rem;"><strong>Date/Semester:</strong> Fall 2025</li>
    </ul>
    <br>
    <h4 style="font-size: 1.3rem; margin-bottom: 1rem;">Emergency and Risk Communication for Foodborne Illness Outbreak</h4>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Category:</strong> Emergency Communication | Public Health | Crisis Management</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">This project presents a comprehensive *Emergency and Risk Communication (ERC)* plan for managing a simulated foodborne illness outbreak in Dhaka, Bangladesh. It demonstrates how timely public health communication, multilingual emergency alerts, evacuation guidance, prevention campaigns, shelter updates, and recovery strategies can help protect communities during a public health crisis. The project emphasizes transparent communication, community engagement, and coordinated action among government agencies, healthcare providers, and local stakeholders to reduce risks, prevent misinformation, and support an effective emergency response and recovery process.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Keywords:</strong> Emergency Risk Communication, Public Health, Crisis Communication, Foodborne Illness, DGHS, Bangladesh, Disaster Management, Health Communication.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Fb Page Link:</strong> <a href="https://www.facebook.com/profile.php?id=61584723801062" target="_blank" style="color: var(--primary); text-decoration: underline;">https://www.facebook.com/profile.php?id=61584723801062</a></p>
    """,
    13: """
    <h3 style="margin-bottom: 1rem; font-size: 1.5rem;">Project Details</h3>
    <ul style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light); list-style-type: none; padding: 0;">
      <li style="margin-bottom: 0.5rem;"><strong>Course Code & Name:</strong> MSJ 4161: Entertainment Education Communication</li>
      <li style="margin-bottom: 0.5rem;"><strong>Project Name:</strong> Going To America</li>
      <li style="margin-bottom: 0.5rem;"><strong>Date/Semester:</strong> Spring 2025</li>
    </ul>
    <br>
    <h4 style="font-size: 1.3rem; margin-bottom: 1rem;">Going To America</h4>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Category:</strong> Short Film | Drama | Satire | Screenplay</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">*Going To America* is a short drama that explores the dangers of false promises surrounding overseas education and the growing trend of scholarship scams targeting university students. Through the story of a young student tempted by an illegal agency, the film highlights the consequences of chasing shortcuts to success while neglecting education and family values. Blending humor with emotional storytelling, the project encourages critical thinking, responsible decision-making, and the importance of pursuing dreams through honesty, perseverance, and hard work rather than deception.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Keywords:</strong> Short Film, Drama, Satire, Scholarship Scam, Overseas Education, Student Life, Screenplay, Higher Education, Bangladesh.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Video Link:</strong> <a href="https://youtu.be/IzMdbsmmYhY" target="_blank" style="color: var(--primary); text-decoration: underline;">https://youtu.be/IzMdbsmmYhY</a></p>
    """,
    14: """
    <h3 style="margin-bottom: 1rem; font-size: 1.5rem;">Project Details</h3>
    <ul style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light); list-style-type: none; padding: 0;">
      <li style="margin-bottom: 0.5rem;"><strong>Course Code & Name:</strong> MSJ 4162: Environmental Communication</li>
      <li style="margin-bottom: 0.5rem;"><strong>Project Name:</strong> Tourism-Induced Soil Pollution in the Chittagong Hill Tracts: Environmental Challenges and Sustainable Solutions</li>
      <li style="margin-bottom: 0.5rem;"><strong>Date/Semester:</strong> Spring 2025</li>
    </ul>
    <br>
    <h4 style="font-size: 1.3rem; margin-bottom: 1rem;">Soil Pollution in the Chittagong Hill Tracts (CHT)</h4>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Category:</strong> Research Paper | Environmental Studies | Sustainable Tourism</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);">Soil Pollution in the Chittagong Hill Tracts (CHT) examines how rapid tourism development contributes to soil degradation, deforestation, waste generation, and environmental pollution in one of Bangladesh’s most ecologically sensitive regions. The paper explores the causes and consequences of soil pollution, its impact on agriculture, biodiversity, and local livelihoods, and emphasizes the importance of sustainable tourism, effective waste management, environmental policies, and community participation to protect the natural resources of the Chittagong Hill Tracts.</p>
    <br>
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light);"><strong>Keywords:</strong> Soil Pollution, Chittagong Hill Tracts (CHT), Sustainable Tourism, Environmental Degradation, Waste Management, Deforestation, Biodiversity, Agriculture, Bangladesh.</p>
    """
}

for i in range(1, 15):
    filepath = f"project-{i}.html"
    if not os.path.exists(filepath):
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # replace everything between <section class="project-detail-content"> and </section>
    pattern = re.compile(r'(<section class="project-detail-content">)(.*?)(</section>)', re.DOTALL)
    
    new_html = r"\g<1>\n" + projects[i] + "\n  " + r"\g<3>"
    content = pattern.sub(new_html, content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
print("Updated all 14 projects.")
