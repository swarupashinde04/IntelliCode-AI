import streamlit as st
import ast
import matplotlib.pyplot as plt
from radon.complexity import cc_visit

st.title("IntelliCode AI")

uploaded_file = st.file_uploader(
    "Upload Python File",
    type=["py"]
)

if uploaded_file is not None:

    code = uploaded_file.read().decode("utf-8")

    st.code(code, language="python")

    tree = ast.parse(code)

    function_count = 0
    variable_count = 0
    loop_count = 0

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            function_count += 1

        elif isinstance(node, ast.Assign):
            variable_count += 1

        elif isinstance(node, (ast.For, ast.While)):
            loop_count += 1

    results = cc_visit(code)

    complexity_score = 0

    for item in results:
        complexity_score += item.complexity

    st.write("Functions:", function_count)
    st.write("Variables:", variable_count)
    st.write("Loops:", loop_count)
    st.write("Complexity:", complexity_score)

    labels = ["Functions", "Variables", "Loops"]

    values = [
        function_count,
        variable_count,
        loop_count
    ]

    fig, ax = plt.subplots()

    ax.bar(labels, values)

    st.pyplot(fig)
    st.subheader("AI Recommendations")

    if loop_count > 3:
        st.warning("Too many loops detected. Try reducing nested loops.")

    if variable_count > 10:
        st.warning("Large number of variables detected.")

    if complexity_score > 10:
        st.error("High code complexity detected.")

    if (
        loop_count <= 3 and
        variable_count <= 10 and
        complexity_score <= 10
    ):
        st.success("Code quality looks good!")