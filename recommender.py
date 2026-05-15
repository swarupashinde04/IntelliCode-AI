import ast
from radon.complexity import cc_visit

# Open sample code
with open("sample.py", "r") as file:
    code = file.read()

# Parse AST
tree = ast.parse(code)

# Counters
functions = 0
loops = 0
variables = 0
if_blocks = 0

# Count metrics
for node in ast.walk(tree):

    if isinstance(node, ast.FunctionDef):
        functions += 1

    elif isinstance(node, (ast.For, ast.While)):
        loops += 1

    elif isinstance(node, ast.Assign):
        variables += 1

    elif isinstance(node, ast.If):
        if_blocks += 1

# Complexity analysis
results = cc_visit(code)

max_complexity = 0

for item in results:

    if item.complexity > max_complexity:
        max_complexity = item.complexity

# Recommendations
print("\n----- IntelliCode AI Suggestions -----\n")

if loops > 3:
    print("Too many loops detected.")
    print("Recommendation: Optimize iterations.\n")

if variables > 10:
    print("Large number of variables detected.")
    print("Recommendation: Reduce unnecessary variables.\n")

if if_blocks > 5:
    print("Too many conditional statements.")
    print("Recommendation: Simplify logic structure.\n")

if max_complexity > 5:
    print("High code complexity detected.")
    print("Recommendation: Split large functions into smaller ones.\n")

if loops <= 3 and variables <= 10 and max_complexity <= 5:
    print("Code quality looks good.")