"""
Skeleton Loader for IndustReal dataset.
Industrial procedural assembly with execution and procedural errors (egocentric).
"""

from pathlib import Path
from typing import Dict, Any

import sys
from pathlib import Path as PathLib
sys.path.insert(0, str(PathLib(__file__).parent))

from utils import get_dataset_dir, print_download_instructions


def load_industreal(data_root: str = "./data") -> Dict[str, Any]:
    dataset_name = "IndustReal"
    dataset_dir = get_dataset_dir(data_root, dataset_name)

    print(f"Looking for data at: {dataset_dir}")

    # Expected structure for IndustReal
    expected_folders = ["videos", "frames", "annotations", "labels", "errors"]
    has_data = dataset_dir.exists()

    if has_data:
        # Check for common subfolders or files
        for folder in expected_folders:
            if (dataset_dir / folder).exists():
                has_data = True
                break
        # Check for video or annotation files
        if list(dataset_dir.rglob("*.mp4")) or list(dataset_dir.rglob("*.json")) or list(dataset_dir.rglob("*.csv")):
            has_data = True

    if not has_data:
        print_download_instructions(
            dataset_name=dataset_name,
            download_link="https://data.4tu.nl/datasets/b008dd74-020d-4ea4-a8ba-7bb60769d224",
            expected_location=str(dataset_dir),
            expected_structure="""
    industreal/
    ├── videos/ or frames/          ← egocentric RGB videos/frames
    ├── annotations/                ← action labels
    ├── error_annotations/          ← procedural and execution errors
    ├── pose/ or gaze/              ← hand/pose/gaze tracking
    └── labels/ or ground_truth/
            """
        )
        raise FileNotFoundError(f"IndustReal data not found at {dataset_dir}. Please download from the official link.")

    # Basic structure if data folder exists
    print("IndustReal folder found. Returning basic structure (full parsing not implemented yet).")

    # Rough estimate of content
    video_files = list(dataset_dir.rglob("*.mp4"))
    json_files = list(dataset_dir.rglob("*.json"))
    csv_files = list(dataset_dir.rglob("*.csv"))
    total_samples_estimate = len(video_files) + len(json_files) + len(csv_files)

    return {
        "description": "IndustReal: Industrial procedural assembly dataset with 27 participants assembling a toy car. "
                       "Includes egocentric RGB video, action labels, and annotations for procedural errors and execution errors.",
        "metadata": {
            "total_samples": total_samples_estimate,
            "modalities": ["egocentric_rgb", "action_labels", "error_annotations", "pose_tracking", "gaze_tracking"],
            "participants": 27,
            "note": "Dataset includes both normal executions and error cases. Full loader parsing can be added later.",
            "estimated_samples": total_samples_estimate
        },
        "samples": []   # Placeholder
    }