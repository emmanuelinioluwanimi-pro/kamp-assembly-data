# test_loaders.py
# Place this in the project ROOT folder

import sys
from pathlib import Path

# Add current directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

from loaders import load_dataset, list_available_datasets

print("=== KAMP Assembly Loaders Test ===\n")

# Show all available datasets
list_available_datasets()

print("\n" + "="*60)

# Test the working loaders
datasets_to_test = [
    "Aero Fastener",
    "Assemble Them All",
    "NIST MOAD",
    "REASSEMBLE",
    "MECCANO",
    "IndustReal",
    "HA-ViD",
    "IKEA ASM",
    "HA4M"
]

# for name in datasets_to_test:
#     print(f"\n=== Testing {name} Loader ===\n")
#     try:
#         data = load_dataset(name, data_root="./data")
        
#         print("✅ Load successful!")
#         print(f"Returned keys: {list(data.keys())}")
#         print(f"Number of samples: {len(data.get('samples', []))}")
        
#         if data.get("samples"):
#             first = data["samples"][0]
#             print(f"First sample ID: {first.get('sample_id')}")
#             print(f"Sample keys: {list(first.keys())}")
            
#     except Exception as e:
#         print(f"❌ Error: {e}")
    
#     print("-" * 60)

print("\n🎉 Test completed!")

user_request = input(f"Dataset list: {', '.join(datasets_to_test)}\nEnter a dataset name to load (or 'exit' to quit): ")
while user_request.lower() != 'exit':
    print(f"\nAttempting to load dataset: {user_request}")
    try:
        data = load_dataset(user_request, data_root="./data")
        print("✅ Load successful!")
        print(f"Returned keys: {list(data.keys())}")
        print(f"Number of samples: {len(data.get('samples', []))}")
        
        if data.get("samples"):
            first = data["samples"][0]
            print(f"First sample ID: {first.get('sample_id')}")
            print(f"Sample keys: {list(first.keys())}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    
    user_request = input(f"\nDataset list: {', '.join(datasets_to_test)}\nEnter another dataset name to load (or 'exit' to quit): ")
