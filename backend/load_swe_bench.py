import json
from typing import List, Dict

def load_swe_bench_lite(file_path: str = "lite.jsonl") -> List[Dict]:
    """
    Load and parse a SWE Bench Lite JSONL file.
    
    Args:
        file_path (str): Path to the JSONL file
        
    Returns:
        List[Dict]: List of dictionaries, each representing one issue
    """
    issues = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                # Skip empty lines
                if line.strip():
                    issue = json.loads(line)
                    issues.append(issue)
        return issues
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find file: {file_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing JSONL file: {str(e)}")

if __name__ == "__main__":
    # Example usage
    try:
        issues = load_swe_bench_lite()
        print(f"Successfully loaded {len(issues)} issues from SWE Bench Lite")
    except Exception as e:
        print(f"Error: {str(e)}") 