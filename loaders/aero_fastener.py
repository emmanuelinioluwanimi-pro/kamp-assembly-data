"""
Loader for Aero Fastener dataset - adapted to your folder structure.
"""

from pathlib import Path
import pandas as pd
from typing import Dict, Any, List

# Use absolute import to avoid previous issues
import sys
from pathlib import Path as PathLib
sys.path.insert(0, str(PathLib(__file__).parent))

from utils import get_dataset_dir, check_data_exists, print_download_instructions


def load_aero_fastener(data_root: str = "./data") -> Dict[str, Any]:
    dataset_name = "Aero Fastener"
    
    # Force correct path - use data_root directly + slug
    dataset_dir = get_dataset_dir(data_root, dataset_name)
    
    meta_path = dataset_dir / "meta.csv"
    inner_data_dir = dataset_dir / "data"

    print(f"Looking for data at: {dataset_dir}")
    print(f"meta.csv exists: {meta_path.exists()}")
    print(f"inner data folder exists: {inner_data_dir.exists()}")

    if not check_data_exists(dataset_dir, ["meta.csv"]):
        print_download_instructions(
            dataset_name=dataset_name,
            download_link="https://data.mendeley.com/public-api/zip/26674p3hvg/download/1",
            expected_location=str(dataset_dir),
            expected_structure="""
    aero_fastener/
    ├── meta.csv
    └── data/
        ├── x9999040.csv
        ├── x9999041.csv
        └── ...
            """
        )
        raise FileNotFoundError(f"Aero Fastener data not found at {dataset_dir}")

    # Load metadata
    meta_df = pd.read_csv(meta_path)
    print(f"Loaded meta.csv with {len(meta_df)} rows. Columns: {list(meta_df.columns)}")

    samples: List[Dict] = []
    
    # Create a map from possible ID to filename
    csv_files = {f.stem: f for f in inner_data_dir.glob("*.csv")}
    
    for idx, row in meta_df.iterrows():
        # Try different possible ID columns
        exp_id = None
        for col in ["experiment_id", "idx", "trial", "id", "file", "Experiment", "filename"]:
            if col in meta_df.columns and pd.notna(row[col]):
                exp_id = str(row[col]).strip()
                break
        
        if not exp_id:
            exp_id = f"row_{idx}"
        
        # Look for matching CSV file (many files start with 'x')
        csv_path = None
        if exp_id in csv_files:
            csv_path = csv_files[exp_id]
        else:
            # Fallback: look for any file containing the ID
            for name, path in csv_files.items():
                if exp_id in name or str(idx) in name:
                    csv_path = path
                    break
        
        if csv_path and csv_path.exists():
            try:
                df = pd.read_csv(csv_path)
                sample = {
                    "sample_id": exp_id,
                    "paths": {
                        "time_series": str(csv_path.relative_to(dataset_dir.parent))
                    },
                    "labels": {
                        "outcome": row.get("label", row.get("outcome", row.get("class", row.get("success", "unknown"))))
                    },
                    "metadata": {k: v for k, v in row.to_dict().items() if pd.notna(v)},
                    "data_shape": df.shape
                }
                samples.append(sample)
            except Exception as e:
                print(f"Warning: Could not load {csv_path.name}: {e}")
        else:
            print(f"Warning: No CSV file found for ID '{exp_id}'")
    
    if not samples:
        raise ValueError(f"No matching CSV files found in {inner_data_dir}. Found {len(csv_files)} CSV files.")

    print(f"Successfully matched {len(samples)} samples.")

    return {
        "description": "Robotic screwing experiments with aeronautical threaded fasteners (force-torque + kinematics data).",
        "metadata": {
            "total_samples": len(samples),
            "modalities": ["force_torque", "kinematics", "time_series"],
            "outcomes": ["mounted", "jammed", "not_mounted"]
        },
        "samples": samples
    }