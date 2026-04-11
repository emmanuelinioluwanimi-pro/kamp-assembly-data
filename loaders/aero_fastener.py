"""
Minimal Loader for Aero Fastener
Returns only the requested metadata + download link
"""

from typing import Dict, Any


def load_aero_fastener(data_root: str = "./data") -> Dict[str, Any]:
    return {
        "dataset_name": "Aero Fastener",
        "description": "Robotic screwing experiments with aeronautical threaded fasteners (alignment, backspin, and fastening). Includes force–torque, position, velocity with assembly outcome labels.",
        "metadata": {
            "size": "85.6 MB",
            "data_type": "Force–torque + robot kinematics (position, orientation, linear & angular velocity) with assembly outcome labels",
            "license": "Creative Commons Attribution 4.0 International licence",
            "knowledge_type": "Force/torque interpretation, tightening heuristics, precision alignment",
            "modalities": ["force_torque", "kinematics", "time_series"],
            "total_samples": 479
        },
        "download_link": "https://data.mendeley.com/public-api/zip/26674p3hvg/download/1",
        "note": "Download the dataset from the link above to use real samples."
    }