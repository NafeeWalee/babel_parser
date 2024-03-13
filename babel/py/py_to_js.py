import ast

def convert_python_to_js(python_code):
    python_ast = ast.parse(python_code)

    # Dictionary to map Python node types to equivalent JavaScript node types
    node_type_mapping = {
        'Module': 'Program',
        'FunctionDef': 'FunctionDeclaration',
        'Return': 'ReturnStatement',
        'Expr': 'ExpressionStatement',
        'Name': 'Identifier',
        'arguments': 'params',
        'Num': 'NumericLiteral',
        'BinOp': 'BinaryExpression',
        # Add more mappings as needed
    }

    def convert_node(node):
        node_type = node.__class__.__name__
        if node_type in node_type_mapping:
            js_node_type = node_type_mapping[node_type]
        else:
            raise NotImplementedError(f"Unsupported node type: {node_type}")

        if hasattr(node, 'value'):
            value = getattr(node, 'value')
        else:
            value = None

        if hasattr(node, 'id'):
            name = getattr(node, 'id')
        else:
            name = None

        if node_type == 'BinOp':
            operator = getattr(node.op, '__class__').__name__
            left = convert_node(node.left)
            right = convert_node(node.right)
            return {
                'type': js_node_type,
                'operator': operator,
                'left': left,
                'right': right
            }
        elif node_type == 'FunctionDef':
            params = [convert_node(arg) for arg in node.args.args]
            body = [convert_node(stmt) for stmt in node.body]
            return {
                'type': js_node_type,
                'id': {'type': 'Identifier', 'name': name},
                'params': params,
                'body': body
            }
        elif node_type == 'Return':
            return {
                'type': js_node_type,
                'argument': convert_node(node.value)
            }
        elif node_type == 'Name':
            return {
                'type': js_node_type,
                'name': name
            }
        elif node_type == 'Num':
            return {
                'type': js_node_type,
                'value': value
            }
        else:
            raise NotImplementedError(f"Conversion not implemented for node type: {node_type}")

    js_ast = [convert_node(node) for node in python_ast.body]
    return js_ast

# Read Python code from a file
with open('AtshaKeras_wildfireV2.py', 'r') as file:
    python_code = file.read()

# Convert Python code to JavaScript AST
js_ast = convert_python_to_js(python_code)
print(js_ast)

with open('output.js', 'w') as file:
    file.write(js_ast)