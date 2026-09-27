with open(r'C:\Users\ishti\.gemini\antigravity-ide\brain\71409d98-290c-43c3-a5f3-2bedd37872ae\.system_generated\steps\490\output.txt', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if len(l) > 0 and l[0] not in (' ', '\t', '\n'):
        print(f"Line {i+1}: {l.strip()[:100]}")
