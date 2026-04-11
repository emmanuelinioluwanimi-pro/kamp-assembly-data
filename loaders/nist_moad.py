"""
Minimal Loader for NIST MOAD
Returns only the requested metadata + download link
"""

from typing import Dict, Any


def load_nist_moad(data_root: str = "./data") -> Dict[str, Any]:
    return {
        "dataset_name": "NIST MOAD",
        "description": "NIST Manufacturing Objects and Assemblies Dataset (MOAD) - RGB images, colored point clouds, 3D meshes, and CAD models for NIST Assembly Task Boards 1-4.",
        "metadata": {
            "size": "Not specified",
            "data_type": "RGB images, point clouds, CAD models, fused 3D meshes (no time-series robot/task data)",
            "license": "Not specified (no LICENSE file or terms in repository)",
            "knowledge_type": "Geometric constraints, part mating, 3D spatial relationships",
            "modalities": ["rgb_images", "point_clouds", "cad_models", "3d_meshes"],
            "num_objects": 76
        },
        "download_link": "No direct link; downloaded via scripts/download_moad.py using downloader_config.json.",
        "note": "Download using the official Python script from the repository."
    }