"""
Minimal Loader for HA-ViD
Returns only the requested metadata + download link
"""

from typing import Dict, Any


def load_ha_vid(data_root: str = "./data") -> Dict[str, Any]:
    return {
        "dataset_name": "HA-ViD",
        "description": "HA-ViD: 3,222 videos of humans assembling products (1.5 million frames). Fine-grained labels for subject, action, object, target, and tool usage. Often used for human-robot collaboration research.",
        "metadata": {
            "size": "226.63 GB",
            "data_type": "RGB + depth video with skeleton data",
            "license": "Creative Commons Attribution-NonCommercial 4.0 International License",
            "knowledge_type": "Fine-grained action sequences, tool usage, object interactions, human collaboration (sometimes two people).",
            "modalities": ["multi_view_rgb_video", "action_labels", "object_labels", "tool_labels", "skeleton_data"],
            "total_frames": "1.5M",
            "videos": 3222
        },
        "download_link": "https://www.dropbox.com/scl/fo/xm5la37s1apjw93vrrpnh/h?rlkey=dhk3k2fs53zmpa9b7ngg2ja69&e=1&st=06nxvqgo&dl=0",
        "note": "This is a very large dataset (226 GB). Download via the Dropbox link (may require access request)."
    }