"""
Loader for Assemble Them All dataset - matching Aero Fastener pattern.
Handles the real structure: numbered folders containing only .obj mesh files.
"""

from pathlib import Path
from typing import Dict, Any, List

import sys
from pathlib import Path as PathLib
sys.path.insert(0, str(PathLib(__file__).parent))

from utils import get_dataset_dir, check_data_exists, print_download_instructions


def load_assemble_them_all(data_root: str = "./data") -> Dict[str, Any]:
    dataset_name = "Assemble Them All"
    dataset_dir = get_dataset_dir(data_root, dataset_name)

    print(f"Looking for data at: {dataset_dir}")

    sub_dirs = ["joint_assembly", "joint_assembly_rotation", "multi_assembly"]
    found_subfolders = [sub for sub in sub_dirs if (dataset_dir / sub).exists()]

    if not found_subfolders:
        print_download_instructions(
            dataset_name=dataset_name,
            download_link="https://people.csail.mit.edu/yunsheng/Assemble-Them-All/dataset_2403/joint_assembly.zip\n"
                         "https://people.csail.mit.edu/yunsheng/Assemble-Them-All/dataset_2403/joint_assembly_rotation.zip\n"
                         "https://people.csail.mit.edu/yunsheng/Assemble-Them-All/dataset_2403/multi_assembly.zip",
            expected_location=str(dataset_dir),
            expected_structure="""
    assemble_them_all/
    ├── joint_assembly/              ← extract joint_assembly.zip contents here
    ├── joint_assembly_rotation/     ← extract joint_assembly_rotation.zip here
    └── multi_assembly/              ← extract multi_assembly.zip here
            """
        )
        raise FileNotFoundError(f"Assemble Them All data not found at {dataset_dir}")

    samples: List[Dict] = []
    total_folders_scanned = 0

    for sub_dir_name in found_subfolders:
        sub_dir = dataset_dir / sub_dir_name
        print(f"\nScanning: {sub_dir_name}")

        for item in sorted(sub_dir.iterdir()):
            if not item.is_dir():
                continue

            total_folders_scanned += 1
            assembly_id = f"{sub_dir_name}_{item.name}"

            # Get all .obj files in this assembly folder (and subfolders if any)
            obj_files = list(item.rglob("*.obj"))

            if obj_files:
                sample = {
                    "sample_id": assembly_id,
                    "paths": {
                        "meshes": [str(p.relative_to(dataset_dir.parent)) for p in obj_files]
                    },
                    "labels": {
                        "assembly_type": sub_dir_name,
                        "num_parts": len(obj_files),
                    },
                    "metadata": {
                        "num_meshes": len(obj_files),
                        "mesh_names": [p.name for p in obj_files]
                    }
                }
                samples.append(sample)
            else:
                # Show example for first few empty folders
                if total_folders_scanned <= 3:
                    print(f"   No .obj files in {item.name}")

    print(f"\nSummary for Assemble Them All:")
    print(f"   Scanned {total_folders_scanned} assembly folders")
    print(f"   Successfully processed {len(samples)} assemblies with meshes")

    if not samples:
        raise ValueError(f"No .obj mesh files found in the assembly folders.")

    return {
        "description": "Thousands of physically valid industrial assemblies with 3D CAD meshes (.obj) representing assembled states.",
        "metadata": {
            "total_samples": len(samples),
            "modalities": ["3d_meshes"],
            "categories": found_subfolders
        },
        "samples": samples
    }