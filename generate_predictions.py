import json
import time
import openai
import os

# Optionally set your OpenAI API key here or use environment variable
openai.api_key = os.getenv("OPENAI_API_KEY") #or "sk-your-key-here"

def load_dataset(path="SWE-bench/data/lite.jsonl"):
    """Loads the SWE-bench Lite dataset from a JSONL file."""
    with open(path) as f:
        return [json.loads(line) for line in f]

def make_prompt(entry, include_docs=True):
    """Constructs a prompt for the LLM based on the issue entry."""
    files = "\n\n".join(
        f"File: {name}\n{content}" for name, content in entry["relevant_files"].items()
    )

    docs = "\n\n".join(
        f"File: {name}\n{doc}" for name, doc in entry.get("documentation", {}).items()
    ) if include_docs else ""

    return f"""
You are an experienced software engineer. Below is a GitHub issue describing a bug.

Issue Title: {entry['issue_title']}
Issue Description:
{entry['issue_body']}

Relevant Files:
{files}

{"Documentation:\n" + docs if include_docs and docs else ""}

Please return a patch to fix the issue as a unified git diff (starting with `diff --git a/...`).
"""

def query_openai(prompt):
    """Queries OpenAI's GPT-4 with the given prompt and returns the response text."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("Error:", e)
        time.sleep(5)
        return ""

def generate_predictions(entries, with_docs=True, output_path="predictions.jsonl"):
    """Generates and saves patch predictions for all entries."""
    with open(output_path, "w") as f:
        for i, entry in enumerate(entries):
            print(f"{i+1}/{len(entries)}: {entry['instance_id']}")
            prompt = make_prompt(entry, include_docs=with_docs)
            response = query_openai(prompt)
            if response:
                result = {
                    "instance_id": entry["instance_id"],
                    "response": response
                }
                f.write(json.dumps(result) + "\n")
            else:
                print(f"⚠️ Skipped {entry['instance_id']} due to error.")

if __name__ == "__main__":
    entries = load_dataset("SWE-bench/data/lite.jsonl")

    # print("Generating predictions WITH documentation...")
    # generate_predictions(entries, with_docs=True, output_path="predictions_with_doc.jsonl")

    print("Generating predictions WITHOUT documentation...")
    generate_predictions(entries, with_docs=False, output_path="predictions_without_doc.jsonl")
