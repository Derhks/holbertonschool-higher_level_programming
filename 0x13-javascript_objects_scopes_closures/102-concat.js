#!/usr/bin/node
const fs = require('fs');
const f1 = process.argv[2];
const f2 = process.argv[3];
const f3 = process.argv[4];
try {
  const d1 = fs.readFileSync(f1, 'utf8');
  const d2 = fs.readFileSync(f2, 'utf8');
  const content = d1 + '\n' + d2 + '\n';
  fs.writeFileSync(f3, content);
} catch (err) {
  console.error(err);
}
