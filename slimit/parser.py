#pip install slimit
#pip install python-minifier
#pip install js2xml
from slimit.parser import Parser
from slimit.visitors.nodevisitor import ASTVisitor

text = """
var x = {
   "key1": "value1",
    "key2": "value2"
};
"""

class MyVisitor(ASTVisitor):
    def visit_Object(self, node):
        """Visit object literal."""
        for prop in node:
            left, right = prop.left, prop.right
            print ('Property key=%s, value=%s' % (left.value, right.value))
            # visit all children in turn
            self.visit(prop)


parser = Parser()
tree = parser.parse(text)
visitor = MyVisitor()
visitor.visit(tree)

