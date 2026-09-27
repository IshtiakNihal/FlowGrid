import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\ishti\.gemini\antigravity-ide\brain\71409d98-290c-43c3-a5f3-2bedd37872ae\.system_generated\steps\490\output.txt', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

canvases = re.findall(r'(\[CANVAS\].*?)(?=\[CANVAS\]|\Z)', text, re.DOTALL)

for c in canvases:
    lines = c.strip().split('\n')
    header = lines[0]
    print("=" * 60)
    print(header)
    for l in lines[1:]:
        # If it's a top-level child of canvas (starts with 2 or 4 spaces)
        if re.match(r'^\s{2,6}\[(FRAME|COMPONENT|GROUP|INSTANCE)\]', l):
            print("  ", l.strip()[:140])
        elif 'text="FlowGrid' in l:
            print("   -> Title:", l.strip()[:140])
