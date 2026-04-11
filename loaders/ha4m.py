"""
Minimal Loader for HA4M
Returns only the requested metadata + download link
"""

from typing import Dict, Any


def load_ha4m(data_root: str = "./data") -> Dict[str, Any]:
    return {
        "dataset_name": "HA4M",
        "description": "HA4M: First multi-modal manufacturing assembly dataset with 41 subjects building an epicyclic gear train. Includes RGB, depth, IR, point clouds, and skeleton data for 12 assembly actions.",
        "metadata": {
            "size": "2.92 TB",
            "data_type": "RGB + depth video with skeleton data",
            "license": "Creative Commons Attribution 4.0 International license (CC BY 4.0)",
            "knowledge_type": "Tool usage in industrial setting, complex multi-step mechanical procedures",
            "modalities": ["rgb", "depth", "ir", "point_clouds", "skeleton_data"],
            "subjects": 41,
            "actions": 12
        },
        "download_link": "https://www.scidb.cn/en/detail?dataSetId=c8d743ad2ea549dfa938cea320a38c46",
        "note": "This is a massive 2.92 TB dataset. Download from SciDB."
    }