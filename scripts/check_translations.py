import re

with open('prototype/index.html', encoding='utf-8') as f:
    content = f.read()

parts = content.split('<script>')
html_part = parts[0]
script_part = parts[1]

bn_ids = set()
for line in html_part.splitlines():
    if re.search(r'[\u0980-\u09FF]', line):
        m = re.search(r'id=["\']([^"\']+)["\']', line)
        if m:
            bn_ids.add(m.group(1))

missing = [i for i in sorted(bn_ids) if i not in script_part]
print('Missing IDs in script:', missing)

import sys
sys.stdout.reconfigure(encoding='utf-8')

# Also find lines with Bengali text that have NO ID
print('\nBengali lines without id:')
for i, line in enumerate(html_part.splitlines(), 1):
    if re.search(r'[\u0980-\u09FF]', line) and not re.search(r'id=["\']', line):
        print(f'{i}: {line.strip()}')
