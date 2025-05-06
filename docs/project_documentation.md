# SWE Bench Project Documentation

## Project Overview
This project is focused on working with the SWE Bench dataset, specifically the SWE Bench Lite version. The goal is to create tools and utilities to process and analyze the dataset effectively.

## Current Project Structure
```
.
├── backend/
│   └── load_swe_bench.py
├── SWE-bench/
│   ├── swebench/
│   │   ├── versioning/
│   │   ├── harness/
│   │   ├── collect/
│   │   ├── inference/
│   │   └── __init__.py
│   ├── docs/
│   ├── tests/
│   └── [various configuration files]
├── logs/
├── Predictions/
└── main.ipynb
```

## Implemented Components

### 1. Data Loading Module (`backend/load_swe_bench.py`)
A Python module designed to load and process the SWE Bench Lite JSONL file.

#### Features:
- JSONL file parsing
- Error handling for file not found and JSON parsing errors
- Type hints for better code clarity
- Configurable file path input
- Empty line skipping
- Returns a list of dictionaries containing issue data

#### Code Structure:
```python
def load_swe_bench_lite(file_path: str = "lite.jsonl") -> List[Dict]:
    """
    Load and parse a SWE Bench Lite JSONL file.
    
    Args:
        file_path (str): Path to the JSONL file
        
    Returns:
        List[Dict]: List of dictionaries, each representing one issue
    """
```

#### Error Handling:
- `FileNotFoundError`: Raised when the specified file cannot be found
- `ValueError`: Raised when there are JSON parsing errors

## Current Status
- Basic data loading infrastructure is in place
- The `lite.jsonl` file is not yet present in the workspace
- Project structure follows best practices with separation of concerns:
  - Backend code in `backend/` directory
  - Documentation in `docs/` directory
  - Main project code in `SWE-bench/` directory

## Next Steps
1. Obtain or create the `lite.jsonl` file
2. Test the data loading functionality
3. Implement additional data processing features
4. Add data validation and transformation capabilities
5. Create visualization and analysis tools

## Dependencies
- Python 3.x
- Standard library modules:
  - `json`
  - `typing`

## Usage Example
```python
from backend.load_swe_bench import load_swe_bench_lite

# Load the dataset
issues = load_swe_bench_lite("path/to/lite.jsonl")

# Process the loaded data
for issue in issues:
    # Process each issue
    pass
```

## Notes
- The project follows a modular structure for easy maintenance and scalability
- Error handling is implemented to ensure robust data processing
- Type hints are used throughout the code for better code clarity and IDE support
- The documentation is maintained in Markdown format for easy reading and version control 