"""
Minimal Loader for Assemble Them All
Returns only the requested metadata + download link
"""

from typing import Dict, Any


def load_assemble_them_all(data_root: str = "./data") -> Dict[str, Any]:
    return {
        "dataset_name": "Assemble Them All",
        "description": "Thousands of physically valid industrial assemblies with diverse assembly motions. Includes 3D CAD meshes, assembly sequences, and simulation-based data.",
        "metadata": {
            "size": "1.0049 GB",
            "data_type": "3D CAD meshes + assembly metadata (no video, no force, no pose)",
            "license": "MIT License",
            "knowledge_type": "Assembly planning, physics-based reasoning, disassembly strategies",
            "modalities": ["3d_meshes", "assembly_sequences"],
            "total_samples": "Thousands"
        },
        "download_link": "https://people.csail.mit.edu/yunsheng/Assemble-Them-All/dataset_2403/joint_assembly.zip\n"
                         "https://people.csail.mit.edu/yunsheng/Assemble-Them-All/dataset_2403/joint_assembly_rotation.zip\n"
                         "https://people.csail.mit.edu/yunsheng/Assemble-Them-All/dataset_2403/multi_assembly.zip",
        "note": "Download the dataset from the links above to use real samples."
    }