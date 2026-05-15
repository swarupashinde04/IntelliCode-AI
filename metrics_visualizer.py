import ast
import matplotlib.pyplot as plt

# Open sample code
with open("sample.py", "r") as file:
    code = file.read()

# Convert into AST
tree = ast.parse(code)

# Counters
functions = 0
loops = 0
variables = 0
if_blocks = 0

# Analyze nodes
for node in ast.walk(tree):

    if isinstance(node, ast.FunctionDef):
        functions += 1

    elif isinstance(node, (ast.For, ast.While)):
        loops += 1

    elif isinstance(node, ast.Assign):
        variables += 1

    elif isinstance(node, ast.If):
        if_blocks += 1

# Labels and values
labels = ["Functions", "Loops", "Variables", "If Blocks"]
values = [functions, loops, variables, if_blocks]

# Create graph
plt.bar(labels, values)

# Titles
plt.title("Code Metrics Analysis")
plt.ylabel("Count")

# Show graph
plt.show()