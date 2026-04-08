"""
Skeleton Loader for NIST MOAD dataset.
Uses the same pattern as Aero Fastener and Assemble Them All.
"""

from pathlib import Path
from typing import Dict, Any

import sys
from pathlib import Path as PathLib
sys.path.insert(0, str(PathLib(__file__).parent))

from utils import get_dataset_dir, print_download_instructions


def load_nist_moad(data_root: str = "./data") -> Dict[str, Any]:
    dataset_name = "NIST MOAD"
    dataset_dir = get_dataset_dir(data_root, dataset_name)

    print(f"Looking for data at: {dataset_dir}")

    # Check if the folder exists and has any content
    if not dataset_dir.exists() or len(list(dataset_dir.iterdir())) == 0:
        print_download_instructions(
            dataset_name=dataset_name,
            download_link="No direct link. Use the official download script: scripts/download_moad.py with downloader_config.json",
            expected_location=str(dataset_dir),
            expected_structure="""
    nist_moad/
    ├── objects/           ← individual parts
    ├── meshes/            ← .obj or .ply files
    ├── point_clouds/
    ├── images/
    └── cad_models/
    
    Note: Download using the provided Python script from the official repo.
            """
        )
        raise FileNotFoundError(f"NIST MOAD data not found at {dataset_dir}. Please run the download script first.")

    # If folder exists but we can't parse it yet, return a minimal valid structure
    # (User can improve this later when they have the data)
    print("NIST MOAD folder found. Returning basic structure (full parsing not implemented yet).")

    return {
        "description": "NIST Manufacturing Objects and Assemblies Dataset (MOAD) - RGB images, colored point clouds, 3D meshes, and CAD models for NIST Assembly Task Boards 1-4.",
        "metadata": {
            "total_samples": 0,
            "modalities": ["rgb_images", "point_clouds", "cad_models", "3d_meshes"],
            "note": "Dataset downloaded via script. Full loader parsing can be added once structure is known.",
            "download_method": "Python script (download_moad.py)"
        },
        "samples": []   # Empty for now - user can extend later
    }