from radon.complexity import cc_visit

# Open sample code
with open("sample.py", "r") as file:
    code = file.read()

# Analyze complexity
results = cc_visit(code)

print("\n----- Complexity Report -----")

for item in results:

    print(f"\nFunction Name : {item.name}")
    print(f"Complexity    : {item.complexity}")

    # Risk classification
    if item.complexity <= 5:
        print("Risk Level   : LOW")

    elif item.complexity <= 10:
        print("Risk Level   : MEDIUM")

    else:
        print("Risk Level   : HIGH")