"""
Skeleton Loader for REASSEMBLE dataset.
Multimodal contact-rich robotic assembly and disassembly.
"""

from pathlib import Path
from typing import Dict, Any

import sys
from pathlib import Path as PathLib
sys.path.insert(0, str(PathLib(__file__).parent))

from utils import get_dataset_dir, print_download_instructions


def load_reassemble(data_root: str = "./data") -> Dict[str, Any]:
    dataset_name = "REASSEMBLE"
    dataset_dir = get_dataset_dir(data_root, dataset_name)

    print(f"Looking for data at: {dataset_dir}")

    # Expected files/folders from the dataset (based on the catalog)
    expected_files = ["data.zip", "poses.zip", "splits.zip", "README.txt"]
    expected_folders = ["data", "poses", "splits"]

    has_data = dataset_dir.exists() and any(
        (dataset_dir / f).exists() for f in expected_files + expected_folders
    )

    # Also check for extracted content
    if not has_data:
        for folder in expected_folders:
            if (dataset_dir / folder).exists():
                has_data = True
                break

    if not has_data:
        print_download_instructions(
            dataset_name=dataset_name,
            download_link="https://researchdata.tuwien.ac.at/records/0ewrv-8cb44/files/data.zip?download=1\n"
                         "https://researchdata.tuwien.ac.at/records/0ewrv-8cb44/files/poses.zip?download=1\n"
                         "https://researchdata.tuwien.ac.at/records/0ewrv-8cb44/files/splits.zip?download=1\n"
                         "https://researchdata.tuwien.ac.at/records/0ewrv-8cb44/files/README.txt?download=1",
            expected_location=str(dataset_dir),
            expected_structure="""
    reassemble/
    ├── data.zip          ← download and extract
    ├── poses.zip         ← download and extract
    ├── splits.zip        ← download and extract
    ├── README.txt
    └── (after extraction: data/, poses/, splits/ folders)
            """
        )
        raise FileNotFoundError(f"REASSEMBLE data not found at {dataset_dir}. Please download and extract the zip files.")

    # If data exists, return a basic valid structure (full parsing can be added later)
    print("REASSEMBLE folder found. Returning basic structure (full parsing not implemented yet).")

    # Try to count some files if possible
    rgb_files = list(dataset_dir.rglob("*.mp4")) + list(dataset_dir.rglob("*.png"))
    force_files = list(dataset_dir.rglob("*force*.csv")) + list(dataset_dir.rglob("*torque*.csv"))

    total_samples_estimate = len(rgb_files) + len(force_files)

    return {
        "description": "REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly on NIST Task Board 1. "
                       "Includes multi-view RGB, event camera, force-torque, audio, robot proprioception, and action labels.",
        "metadata": {
            "total_samples": total_samples_estimate,
            "modalities": ["rgb_video", "event_camera", "force_torque", "audio", "proprioception", "pose", "action_labels"],
            "note": "Dataset downloaded and extracted. Full loader parsing can be extended once the exact folder structure is known.",
            "estimated_samples": total_samples_estimate
        },
        "samples": []   # Empty for now - can be expanded when data structure is clear
    }