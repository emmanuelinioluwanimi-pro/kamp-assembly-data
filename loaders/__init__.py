"""
KAMP Assembly Data Loaders
Central entry point for all assembly datasets.
"""

import pandas as pd
from pathlib import Path
from typing import Dict, Any

# Lazy loader to avoid import issues
def _get_loader(name: str):
    if name == "Aero Fastener":
        from .aero_fastener import load_aero_fastener
        return load_aero_fastener
    elif name == "Assemble Them All":
        from .assemble_them_all import load_assemble_them_all
        return load_assemble_them_all
    elif name == "NIST MOAD":
        from .nist_moad import load_nist_moad
        return load_nist_moad
    elif name == "REASSEMBLE":
        from .reassemble import load_reassemble
        return load_reassemble
    elif name == "MECCANO":
        from .meccano import load_meccano
        return load_meccano
    elif name == "IndustReal":
        from .industreal import load_industreal
        return load_industreal
    elif name == "HA-ViD":
        from .ha_vid import load_ha_vid
        return load_ha_vid
    elif name == "IKEA ASM":
        from .ikea_asm import load_ikea_asm
        return load_ikea_asm
    elif name == "HA4M":
        from .ha4m import load_ha4m
        return load_ha4m
    else:
        raise NotImplementedError(f"Loader for '{name}' is not implemented yet.")


def load_dataset(name: str, data_root: str = "./data") -> Dict[str, Any]:
    """Main function to load any dataset."""
    catalog_path = Path("catalog.csv")
    if not catalog_path.exists():
        raise FileNotFoundError("catalog.csv not found in project root.")

    catalog = pd.read_csv(catalog_path)
    row = catalog[catalog["name"] == name]
    if row.empty:
        raise ValueError(f"Dataset '{name}' not found in catalog.csv.")

    row = row.iloc[0]

    try:
        loader_func = _get_loader(name)
    except Exception as e:
        raise NotImplementedError(f"Loader for '{name}' failed to load: {e}")

    from .utils import get_dataset_dir
    dataset_dir = get_dataset_dir(data_root, name)

    try:
        data = loader_func(data_root=str(dataset_dir))

        # Add catalog metadata
        data["dataset_name"] = name
        data.setdefault("description", row.get("assembly_task", ""))

        if "metadata" not in data:
            data["metadata"] = {}

        data["metadata"].update({
            "source": row.get("source"),
            "data_type": row.get("data_type"),
            "size": row.get("size"),
            "license": row.get("license"),
            "download_link": row.get("download_link"),
            "knowledge_type": row.get("knowledge_type"),
        })

        print(f"✅ Successfully loaded '{name}' with {len(data.get('samples', []))} samples.")
        return data

    except Exception as e:
        print(f"\n⚠️  Error loading '{name}': {e}")
        print(f"📥 Download link: {row.get('download_link', 'N/A')}")
        print(f"   Expected folder: {dataset_dir}\n")
        raise


def list_available_datasets() -> None:
    """Print summary of all datasets."""
    catalog = pd.read_csv("catalog.csv")
    print("📋 Available Assembly Datasets:\n")
    for _, row in catalog.iterrows():
        print(f"• {row['name']}")
        print(f"  Task : {row['assembly_task'][:85]}...")
        print(f"  Size : {row['size']}")
        print(f"  Type : {row['data_type'][:70]}...")
        print("-" * 70)


__all__ = ["load_dataset", "list_available_datasets"]