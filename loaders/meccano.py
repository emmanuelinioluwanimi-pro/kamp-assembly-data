"""
Skeleton Loader for MECCANO dataset.
Egocentric toy motorbike assembly with gaze data.
"""

from pathlib import Path
from typing import Dict, Any

import sys
from pathlib import Path as PathLib
sys.path.insert(0, str(PathLib(__file__).parent))

from utils import get_dataset_dir, print_download_instructions


def load_meccano(data_root: str = "./data") -> Dict[str, Any]:
    dataset_name = "MECCANO"
    dataset_dir = get_dataset_dir(data_root, dataset_name)

    print(f"Looking for data at: {dataset_dir}")

    # Expected structure for MECCANO
    expected_folders = ["videos", "frames", "annotations", "gaze"]
    expected_files = ["*.mp4", "*.json", "*.csv"]

    has_data = dataset_dir.exists()

    if has_data:
        # Check for common subfolders or files
        for folder in expected_folders:
            if (dataset_dir / folder).exists():
                has_data = True
                break
        # Also check for any video or annotation files
        if list(dataset_dir.rglob("*.mp4")) or list(dataset_dir.rglob("*.json")):
            has_data = True

    if not has_data:
        print_download_instructions(
            dataset_name=dataset_name,
            download_link="https://iplab.dmi.unict.it/legacy/MECCANO/#dat",
            expected_location=str(dataset_dir),
            expected_structure="""
    meccano/
    ├── videos/               ← egocentric videos
    ├── frames/               ← extracted frames
    ├── annotations/          ← action labels, object classes
    ├── gaze/                 ← gaze signals
    └── (possibly subject folders like P01, P02, ...)
            """
        )
        raise FileNotFoundError(f"MECCANO data not found at {dataset_dir}. Please download from the official website.")

    # Basic structure if data is present
    print("MECCANO folder found. Returning basic structure (full parsing not implemented yet).")

    # Try to give a rough count
    video_files = list(dataset_dir.rglob("*.mp4"))
    json_files = list(dataset_dir.rglob("*.json"))
    total_samples_estimate = len(video_files) + len(json_files)

    return {
        "description": "MECCANO dataset: Egocentric video recordings of 20 participants building a toy motorbike. "
                       "Includes RGB + depth video, gaze signals, and annotations for object recognition, detection, and action anticipation.",
        "metadata": {
            "total_samples": total_samples_estimate,
            "modalities": ["egocentric_rgb", "depth", "gaze_signals", "action_annotations", "object_labels"],
            "participants": 20,
            "note": "Dataset downloaded. Full loader can be expanded once the exact folder structure is known.",
            "estimated_samples": total_samples_estimate
        },
        "samples": []   # Placeholder - can be filled later
    }