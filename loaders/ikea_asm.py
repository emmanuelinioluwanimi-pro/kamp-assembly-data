"""
Skeleton Loader for IKEA ASM dataset.
Large multi-modal furniture assembly dataset (420 GB).
"""

from pathlib import Path
from typing import Dict, Any

import sys
from pathlib import Path as PathLib
sys.path.insert(0, str(PathLib(__file__).parent))

from utils import get_dataset_dir, print_download_instructions


def load_ikea_asm(data_root: str = "./data") -> Dict[str, Any]:
    dataset_name = "IKEA ASM"
    dataset_dir = get_dataset_dir(data_root, dataset_name)

    print(f"Looking for data at: {dataset_dir}")

    # IKEA ASM is very large (420 GB) with multi-view RGB + depth
    has_data = dataset_dir.exists() and (
        any(dataset_dir.rglob("*.mp4")) or 
        any(dataset_dir.rglob("*.avi")) or 
        (dataset_dir / "videos").exists() or 
        (dataset_dir / "annotations").exists()
    )

    if not has_data:
        print_download_instructions(
            dataset_name=dataset_name,
            download_link="https://drive.google.com/drive/folders/1xkDp--QuUVxgl4oJjhCDb2FWNZTkYANq?usp=sharing",
            expected_location=str(dataset_dir),
            expected_structure="""
    ikea_asm/
    ├── videos/                  ← multi-view RGB + depth videos (very large)
    ├── annotations/             ← atomic actions, 16,764 annotated actions
    ├── pose/                    ← human pose data
    ├── segmentation/            ← object segmentation/tracking
    └── (4 furniture types: different assembly tasks)
            """
        )
        raise FileNotFoundError(f"IKEA ASM data not found at {dataset_dir}. "
                              "This is a 420 GB dataset — download from the Google Drive folder.")

    print("IKEA ASM folder found. Returning basic structure (full parsing not implemented yet due to size).")

    video_files = list(dataset_dir.rglob("*.mp4"))
    total_samples_estimate = len(video_files)

    return {
        "description": "IKEA ASM: 371 furniture assembly videos across 4 furniture types with 16,764 annotated actions. "
                       "Multi-view RGB + depth, human pose, object segmentation/tracking, and atomic action labels.",
        "metadata": {
            "total_samples": total_samples_estimate,
            "modalities": ["multi_view_rgb", "depth", "human_pose", "object_segmentation", "action_labels"],
            "furniture_types": 4,
            "annotated_actions": 16764,
            "note": "Extremely large dataset (420 GB). Full detailed loader can be implemented when partial data is available.",
            "estimated_samples": total_samples_estimate
        },
        "samples": []
    }