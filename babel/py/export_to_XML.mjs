import { parse } from "@babel/parser";
import traverse from "@babel/traverse";
import xmlbuilder from "xmlbuilder";

import fs from 'fs';

// Load your JavaScript code
const code = fs.readFileSync('ast_output.json', 'utf-8');

// Parse the code using Babel
const ast = parse(code, {
  sourceType: 'module', // or 'script' depending on your code
  plugins: [
    'jsx', // if you have JSX code
    'typescript', // if you have TypeScript code
  ]
});

// XML builder
const xmlRoot = xmlbuilder.create('AST');

// Traverse the AST and generate XML
traverse(ast, {
  enter(path) {
    // Generate XML nodes for each AST node
    const node = path.node;
    const xmlNode = xmlRoot.ele(node.type);

    // Add attributes
    for (const key in node) {
      if (node.hasOwnProperty(key) && key !== 'type') {
        xmlNode.att(key, node[key]);
      }
    }

    // Add XML node to parent
    if (path.parentPath) {
      const parentXmlNode = path.parentPath.node;
      if (parentXmlNode) {
        xmlRoot.get(path.parentPath.node.type).ele(xmlNode);
      }
    }
  }
});

// Output XML
const xmlString = xmlRoot.end({ pretty: true });
console.log(xmlString);
