//npm install --save-dev @babel/parser
const babel_parser = require("@babel/parser");
const fs = require('fs');

const codeSample = 
`
function add(a, b) {
    return a + b;
}

let result = add(2, 3);
console.log(result);
`;

const ast = babel_parser.parse(codeSample, {
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
fs.writeFileSync('ast_jsonString_output.json', jsonString);