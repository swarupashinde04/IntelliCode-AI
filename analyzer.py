import ast
# Open sample code file :
with open('sample.py','r')as file :
          code = file.read()
# Convert code into AST tree :
tree = ast.parse(code)
# Counters :
function_count = 0
variable_count = 0
loop_count = 0
# Traverse through code structure :
for node in ast.walk(tree) :
    if isinstance(node, ast.FunctionDef) :
        function_count += 1
    elif isinstance(node, ast.Assign) :
        variable_count += 1
    elif isinstance(node, (ast.For, ast.While)) :
        loop_count += 1

# Print the counts :
print(f"Functions: {function_count}")
print(f"Variables: {variable_count}")
print(f"Loops: {loop_count}")
