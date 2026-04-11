"""
Minimal Loader for IKEA ASM
Returns only the requested metadata + download link
"""

from typing import Dict, Any


def load_ikea_asm(data_root: str = "./data") -> Dict[str, Any]:
    return {
        "dataset_name": "IKEA ASM",
        "description": "IKEA ASM: 371 furniture assembly videos across 4 furniture types with 16,764 annotated actions. Multi-view RGB + depth, human pose, object segmentation/tracking, and atomic action labels.",
        "metadata": {
            "size": "420.97 GB",
            "data_type": "Multi‑modal (RGB + depth + pose + object segmentation/tracking + action labels)",
            "license": "Creative Commons Attribution-NonCommercial 4.0 International License",
            "knowledge_type": "Multi-step furniture assembly, object manipulation, step-by-step planning",
            "modalities": ["multi_view_rgb", "depth", "human_pose", "object_segmentation", "action_labels"],
            "furniture_types": 4,
            "annotated_actions": 16764
        },
        "download_link": "https://drive.google.com/drive/folders/1xkDp--QuUVxgl4oJjhCDb2FWNZTkYANq?usp=sharing",
        "note": "This is a very large dataset (420 GB). Download from the Google Drive folder above."
    }