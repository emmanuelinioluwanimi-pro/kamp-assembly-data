# test_loaders.py - Simple version
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from loaders import load_dataset, list_available_datasets

print("=== KAMP Assembly Data Catalog ===\n")

list_available_datasets()

while True:
    name = input("\nEnter a dataset name to load (or 'exit' to quit): ").strip()
    if name.lower() == 'exit':
        break
    if not name:
        continue

    try:
        data = load_dataset(name)
        print("\n" + "="*60)
        print(f"Dataset: {data['dataset_name']}")
        print(f"Description: {data['description']}")
        print(f"Download Link: {data['download_link']}")
        print(f"Note: {data['note']}")
        print("\nMetadata:")
        for k, v in data['metadata'].items():
            print(f"  {k}: {v}")
        print("="*60)
    except Exception as e:
        print(f"Error: {e}")