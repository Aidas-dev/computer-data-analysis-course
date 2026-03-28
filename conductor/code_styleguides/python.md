# Python Style Guide for Data Analysis

## General Principles
- Follow PEP 8 conventions for Python code
- Prioritize readability and reproducibility
- Write code that is easy to understand and modify

## Naming Conventions
- **Variables/functions:** `snake_case` (e.g., `data_frame`, `load_data()`)
- **Classes:** `PascalCase` (e.g., `DataProcessor`)
- **Constants:** `UPPER_CASE` (e.g., `MAX_ITERATIONS`)
- **Private variables:** `_prefix` (e.g., `_internal_cache`)

## Jupyter Notebook Specific

### Cell Organization
- Each cell should perform a single logical operation
- Import statements should be in the first code cell
- Use markdown cells to separate major sections

### Imports
```python
# Standard library first
import os
from pathlib import Path

# Third-party libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Local imports
# from my_module import my_function
```

### Code Comments
- Use inline comments sparingly—prefer self-documenting code
- Add comments to explain *why*, not *what*
- Use docstrings for functions:
```python
def load_dataset(filepath):
    """Load and preprocess the dataset from the given filepath.
    
    Args:
        filepath: Path to the CSV file
        
    Returns:
        pandas.DataFrame: Loaded and cleaned dataset
    """
```

## Data Analysis Best Practices

### Data Loading
- Use relative paths for data files
- Document data source and any preprocessing applied
```python
data_path = Path("data") / "dataset.csv"
df = pd.read_csv(data_path, sep=";", decimal=",")
```

### Data Exploration
- Always check for missing values
- Document data types and ranges
- Use ydata-profiling for comprehensive reports

### Visualization
- Always label axes and provide titles
- Use consistent color schemes
- Include brief interpretation of plots

## Error Handling
- Use try-except blocks for file operations
- Validate data before processing
- Provide informative error messages

## Reproducibility
- Set random seeds for reproducibility:
```python
np.random.seed(42)
```
- Document package versions used
- Ensure notebooks run from top to bottom without errors
