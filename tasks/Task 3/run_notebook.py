import sys
import nbformat
from nbclient import NotebookClient

# Set UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

# Read and execute the notebook
print("Loading notebook...")
with open('Task_3.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

print("Executing notebook...")
client = NotebookClient(nb, timeout=600, kernel_name='python3')
client.execute()

print("Saving executed notebook...")
with open('Task_3.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print("Notebook executed successfully!")
