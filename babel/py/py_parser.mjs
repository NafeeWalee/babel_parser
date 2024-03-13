//To run this program use this command: 

import { parse } from "@babel/parser";

import fs from 'fs';

//file is in the same folder
const json = 'py2json.json';

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
fs.writeFileSync('py_ast_output.json', jsonString);