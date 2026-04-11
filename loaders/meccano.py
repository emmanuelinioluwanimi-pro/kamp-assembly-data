"""
Minimal Loader for MECCANO
Returns only the requested metadata + download link
"""

from typing import Dict, Any


def load_meccano(data_root: str = "./data") -> Dict[str, Any]:
    return {
        "dataset_name": "MECCANO",
        "description": "MECCANO dataset: Egocentric video recordings of 20 participants building a toy motorbike. Includes RGB + depth video, gaze signals, and annotations for object recognition, detection, and action anticipation.",
        "metadata": {
            "size": "90.619 GB",
            "data_type": "RGB + depth video with gaze data (multimodal egocentric)",
            "license": "Not specified",
            "knowledge_type": "Action anticipation, object recognition from first-person view, gaze-guided attention",
            "modalities": ["egocentric_rgb", "depth", "gaze_signals", "action_annotations", "object_labels"],
            "participants": 20,
            "tasks": "recognition, detection, anticipation"
        },
        "download_link": "https://iplab.dmi.unict.it/legacy/MECCANO/#dat",
        "note": "Download the dataset from the official website link above."
    }