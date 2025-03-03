import os
import nbformat

AUTOGRADED_DIR = "autograded"
OUTPUT_FILE = "errors.md"

def extract_errors():
    errors = []
    for dirpath, dirnames, filenames in os.walk(AUTOGRADED_DIR):
        student_path = os.path.join(dirpath)
        if not os.path.isdir(student_path):
            continue
        
        for notebook in os.listdir(student_path):
            if notebook.endswith(".ipynb"):
                print(notebook)
                notebook_path = os.path.join(student_path, notebook)
                with open(notebook_path, "r", encoding="utf-8") as f:
                    nb = nbformat.read(f, as_version=4)
                    for cell in nb.cells:
                        if cell.cell_type == "code" and "outputs" in cell:
                            for output in cell["outputs"]:
                                if output.output_type == "error":
                                    errors.append(f"❌ **{notebook}**: {output.ename} - {output.evalue}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        if errors:
            f.write("## ❌ Errors Found in Autograded Notebooks\n\n")
            f.write("\n".join(errors))
        else:
            f.write("✅ No errors found.")

if __name__ == "__main__":
    extract_errors()