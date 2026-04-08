"""
Skeleton Loader for HA4M dataset.
First multi-modal manufacturing assembly dataset (very large, 2.92 TB).
"""

from pathlib import Path
from typing import Dict, Any

import sys
from pathlib import Path as PathLib
sys.path.insert(0, str(PathLib(__file__).parent))

from utils import get_dataset_dir, print_download_instructions


def load_ha4m(data_root: str = "./data") -> Dict[str, Any]:
    dataset_name = "HA4M"
    dataset_dir = get_dataset_dir(data_root, dataset_name)

    print(f"Looking for data at: {dataset_dir}")

    # HA4M is extremely large (2.92 TB)
    has_data = dataset_dir.exists() and (
        any(dataset_dir.rglob("*.mp4")) or 
        any(dataset_dir.rglob("*.png")) or 
        (dataset_dir / "annotations").exists() or 
        (dataset_dir / "RGB").exists() or 
        (dataset_dir / "depth").exists()
    )

    if not has_data:
        print_download_instructions(
            dataset_name=dataset_name,
            download_link="https://www.scidb.cn/en/detail?dataSetId=c8d743ad2ea549dfa938cea320a38c46",
            expected_location=str(dataset_dir),
            expected_structure="""
    ha4m/
    ├── RGB/                  ← RGB videos
    ├── depth/                ← depth data
    ├── IR/                   ← infrared
    ├── point_clouds/         ← point clouds
    ├── skeleton/             ← skeleton data
    └── annotations/          ← 12 assembly actions
            """
        )
        raise FileNotFoundError(f"HA4M data not found at {dataset_dir}. "
                              "This is a massive 2.92 TB dataset — download from SciDB.")

    print("HA4M folder found. Returning basic structure (full parsing not implemented due to size).")

    # Rough estimate
    video_files = list(dataset_dir.rglob("*.mp4"))
    total_samples_estimate = len(video_files)

    return {
        "description": "HA4M: First multi-modal manufacturing assembly dataset with 41 subjects building an epicyclic gear train. "
                       "Includes RGB, depth, IR, point clouds, and skeleton data for 12 assembly actions.",
        "metadata": {
            "total_samples": total_samples_estimate,
            "modalities": ["rgb", "depth", "ir", "point_clouds", "skeleton_data"],
            "subjects": 41,
            "actions": 12,
            "note": "Extremely large dataset (2.92 TB). Full loader can be expanded when partial data is available.",
            "estimated_samples": total_samples_estimate
        },
        "samples": []
    }