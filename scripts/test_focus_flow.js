const fs = require('fs');
const html = fs.readFileSync('prototype/index.html', 'utf8');

// Check that btnNewEnquiry exists
const btnMatch = html.match(/id="btnNewEnquiry"[^>]*>/);
console.log('btnNewEnquiry tag:', btnMatch ? btnMatch[0] : 'not found');

// Check resetForm implementation
const resetFormMatch = html.match(/function resetForm\(\)[\s\S]*?^    \}/m);
console.log('resetForm function:\n', resetFormMatch ? resetFormMatch[0] : 'not found');

// Check showState implementation
const showStateMatch = html.match(/function showState\(stateId\)[\s\S]*?^    \}/m);
console.log('showState function:\n', showStateMatch ? showStateMatch[0] : 'not found');
