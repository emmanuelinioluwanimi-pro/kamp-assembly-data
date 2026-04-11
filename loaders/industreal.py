"""
Minimal Loader for IndustReal
Returns only the requested metadata + download link
"""

from typing import Dict, Any


def load_industreal(data_root: str = "./data") -> Dict[str, Any]:
    return {
        "dataset_name": "IndustReal",
        "description": "IndustReal: Industrial procedural assembly dataset with 27 participants assembling a toy car. Includes egocentric RGB video, action labels, and annotations for procedural errors and execution errors.",
        "metadata": {
            "size": "71.78 GB",
            "data_type": "RGB video frames + hand/pose/gaze tracking + ground‑truth labels",
            "license": "Apache-2.0",
            "knowledge_type": "Error detection, procedural knowledge, distinguishing normal vs wrong execution",
            "modalities": ["egocentric_rgb", "action_labels", "error_annotations", "pose_tracking", "gaze_tracking"],
            "participants": 27
        },
        "download_link": "https://data.4tu.nl/datasets/b008dd74-020d-4ea4-a8ba-7bb60769d224",
        "note": "Download the dataset from the link above."
    }