import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('<div class="contact-form-wrap reveal-right">')
if start != -1:
    end = content.find('</section>', start)
    new_content = content[:start] + '      </div>\n    </div>\n  </section>' + content[end + 10:]
    with codecs.open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Updated index.html')
else:
    print('Not found')
