"""
Skeleton Loader for HA-ViD dataset.
Large-scale human industrial assembly video dataset (226 GB).
"""

from pathlib import Path
from typing import Dict, Any

import sys
from pathlib import Path as PathLib
sys.path.insert(0, str(PathLib(__file__).parent))

from utils import get_dataset_dir, print_download_instructions


def load_ha_vid(data_root: str = "./data") -> Dict[str, Any]:
    dataset_name = "HA-ViD"
    dataset_dir = get_dataset_dir(data_root, dataset_name)

    print(f"Looking for data at: {dataset_dir}")

    # HA-ViD is extremely large (226 GB) — mostly videos + annotations
    has_data = dataset_dir.exists() and (
        any(dataset_dir.rglob("*.mp4")) or 
        (dataset_dir / "annotations").exists() or 
        (dataset_dir / "videos").exists()
    )

    if not has_data:
        print_download_instructions(
            dataset_name=dataset_name,
            download_link="https://www.dropbox.com/scl/fo/xm5la37s1apjw93vrrpnh/h?rlkey=dhk3k2fs53zmpa9b7ngg2ja69&e=1&st=06nxvqgo&dl=0",
            expected_location=str(dataset_dir),
            expected_structure="""
    ha_vid/
    ├── videos/                  ← multi-view RGB videos (very large)
    ├── annotations/             ← fine-grained action, object, tool, target labels
    ├── skeleton/ or pose/       ← skeleton data
    └── (possibly subject or task-specific folders)
            """
        )
        raise FileNotFoundError(f"HA-ViD data not found at {dataset_dir}. "
                              "This is a 226 GB dataset — download via the Dropbox link (may require request access).")

    print("HA-ViD folder found. Returning basic structure (full parsing not implemented yet due to size).")

    video_files = list(dataset_dir.rglob("*.mp4"))
    total_samples_estimate = len(video_files)

    return {
        "description": "HA-ViD: 3,222 videos of humans assembling products (1.5 million frames). "
                       "Fine-grained labels for subject, action, object, target, and tool usage. "
                       "Often used for human-robot collaboration research.",
        "metadata": {
            "total_samples": total_samples_estimate,
            "modalities": ["multi_view_rgb_video", "action_labels", "object_labels", "tool_labels", "skeleton_data"],
            "note": "Extremely large dataset (226 GB). Full detailed loader can be implemented once partial data is available.",
            "estimated_samples": total_samples_estimate
        },
        "samples": []
    }