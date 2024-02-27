//To run this program use this command: node parser.mjs

//npm install --save-dev @babel/parser
import { convertCSV } from './csv_to_json.js';

import { parse } from "@babel/parser";

import fs from 'fs';

//file is in the same folder
const csvFilePath = 'sample.csv';

//manually converting csv to json
let json = convertCSV(csvFilePath);

// const codeSample =
//   `
// function add(a, b) {
//     return a + b;
// }

// let result = add(2, 3);
// console.log(result);
// `;

const ast = parse(json, {
  sourceType: "module",
  plugins: [
    "jsx",
    "flow",
  ],
});

//output 1
console.log(ast);

//output 2
const jsonString = JSON.stringify(ast, null, 2);
//file is saved in the same folder
fs.writeFileSync('ast_output.json', jsonString);




//================================================CSV parser works but only provides limited details
// const csv = require('csv-parser');
// const readStream = fs.createReadStream(csvFilePath);

// readStream.pipe(csv())
//     .on('data', (row) => {
//         console.log(row);
//     })
//     .on('end', () => {
//         console.log('CSV file parsing finished');
//     });