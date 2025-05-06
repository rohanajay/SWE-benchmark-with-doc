import pandas as pd

# Load the Parquet file
df = pd.read_parquet('dev-00000-of-00001.parquet')

# Convert to JSONL
df.to_json('lite.jsonl', orient='records', lines=True)
