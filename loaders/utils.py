from pathlib import Path
from typing import Optional

def get_dataset_dir(data_root: str, dataset_name: str) -> Path:
    slug = dataset_name.lower().replace(" ", "_").replace("-", "_").replace("'", "").replace("(", "").replace(")", "")
    return Path(data_root) / slug


def check_data_exists(dataset_dir: Path, required_files: Optional[list] = None) -> bool:
    if not dataset_dir.exists():
        return False
    if required_files:
        for item in required_files:
            if not (dataset_dir / item).exists():
                return False
    return True


def print_download_instructions(dataset_name: str, download_link: str, 
                               expected_location: str = "", 
                               expected_structure: str = "") -> None:
    print(f"\n⚠️  Dataset '{dataset_name}' not found or incomplete.")
    if expected_location:
        print(f"   Expected location: {expected_location}")
    print(f"\n📥 Download from:")
    print(f"   {download_link}")
    if expected_structure:
        print("\nExpected folder structure:")
        print(expected_structure.strip())
    print("\nAfter downloading/extracting, run the test again.\n")