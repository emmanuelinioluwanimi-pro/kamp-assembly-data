"""
KAMP Assembly Data Loaders - Minimal Metadata Version
"""

import pandas as pd
from pathlib import Path
from typing import Dict, Any

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
    """Return only metadata + download link. No data loading or folder checks."""
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
        data = loader_func(data_root)
    except Exception as e:
        print(f"Warning: Loader for '{name}' failed: {e}")
        data = {
            "dataset_name": name,
            "description": row.get("assembly_task", ""),
            "metadata": {},
            "download_link": row.get("download_link"),
            "note": "Error loading loader."
        }

    # Force the exact keys you want
    data["dataset_name"] = name
    data.setdefault("description", row.get("assembly_task", ""))
    data.setdefault("metadata", {})
    data["metadata"].update({
        "size": row.get("size"),
        "data_type": row.get("data_type"),
        "license": row.get("license"),
        "knowledge_type": row.get("knowledge_type"),
    })
    data["download_link"] = row.get("download_link")
    data.setdefault("note", "Download the dataset from the link above to use real samples.")

    return data


def list_available_datasets() -> None:
    """Print simple list of all datasets."""
    catalog = pd.read_csv("catalog.csv")
    print("Available datasets:")
    for _, row in catalog.iterrows():
        print(f"• {row['name']}")
    print()


__all__ = ["load_dataset", "list_available_datasets"]