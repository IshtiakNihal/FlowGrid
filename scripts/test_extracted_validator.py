import os, subprocess, re

test_dir = 'scratch/test_extracted_zip'
extracted_html = os.path.join(test_dir, 'prototype/index.html')
with open(extracted_html, 'r', encoding='utf-8') as f:
    html_content = f.read()

start = html_content.find('function validateBDPhone')
end = html_content.find('function handleFormSubmit')
func_code = html_content[start:end].strip()


test_script = """
""" + func_code + """

const tests = [
  { input: '01711000000', expected: true, label: 'Standard 11-digit mobile' },
  { input: '01711-000000', expected: true, label: 'Hyphenated mobile' },
  { input: '+880 1711 000000', expected: true, label: 'International format with spaces' },
  { input: '+8801711000000', expected: true, label: 'International contiguous format' },
  { input: '+880 01711-000000', expected: true, label: 'Country code + trunk zero' },
  { input: '০১৭১১০০০০০০', expected: true, label: 'Native Bengali numerals' },
  { input: '+৮৮০ ০১৭১১-০০০০০০', expected: true, label: 'Bengali numerals + country code + trunk zero' },
  { input: 'abcdefgh', expected: false, label: 'Letters rejected' },
  { input: 'তানভীর আহমেদ', expected: false, label: 'Bengali letters rejected' },
  { input: '12345678', expected: false, label: 'Too short (8 digits)' },
  { input: '01234567890', expected: false, label: 'Invalid operator 012' },
  { input: '01711000000@#$', expected: false, label: 'Arbitrary punctuation rejected' },
  { input: '', expected: false, label: 'Empty input rejected' }
];

let allPassed = true;
tests.forEach((t, i) => {
  const res = validateBDPhone(t.input);
  const pass = res === t.expected;
  if (!pass) allPassed = false;
  console.log(`Test ${i+1}: [${pass ? 'PASS' : 'FAIL'}] "${t.input}" -> ${res} (${t.label})`);
});

if (allPassed) {
  console.log('\\nALL 13 TESTS PASSED PERFECTLY!');
} else {
  console.log('\\nSOME TESTS FAILED');
  process.exit(1);
}
"""

with open('scratch/test_val.js', 'w', encoding='utf-8') as f:
    f.write(test_script)

runner = subprocess.run(['node', 'scratch/test_val.js'], capture_output=True, text=True)
print(runner.stdout)
if runner.returncode != 0:
    print('Error:', runner.stderr)
