from radon.complexity import cc_visit
import matplotlib.pyplot as plt

# Open sample code
with open("sample.py", "r") as file:
    code = file.read()

# Analyze complexity
results = cc_visit(code)

# Store data
function_names = []
complexities = []

for item in results:
    function_names.append(item.name)
    complexities.append(item.complexity)

# Create graph
plt.bar(function_names, complexities)

# Labels
plt.xlabel("Functions")
plt.ylabel("Complexity")
plt.title("Function Complexity Analysis")

# Show graph
plt.show()