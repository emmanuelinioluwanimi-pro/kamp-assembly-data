"""
Shared utilities for all dataset loaders (simplified version).
"""

from pathlib import Path
from typing import Optional


def get_dataset_dir(data_root: str, dataset_name: str) -> Path:
    """Convert dataset name to a safe folder name."""
    slug = (dataset_name.lower()
            .replace(" ", "_")
            .replace("-", "_")
            .replace("'", "")
            .replace("(", "")
            .replace(")", ""))
    return Path(data_root) / slug


def print_download_instructions(dataset_name: str, download_link: str, 
                               expected_location: str = "", 
                               expected_structure: str = "") -> None:
    """Print clear download instructions when data is missing."""
    print(f"\n⚠️  Dataset '{dataset_name}' not found or not downloaded yet.")
    if expected_location:
        print(f"   Expected location: {expected_location}")
    print(f"\n📥 Download from:")
    print(f"   {download_link}")
    if expected_structure:
        print("\nExpected folder structure:")
        print(expected_structure.strip())
    print("\nAfter downloading, run load_dataset() again.\n")