# KAMP Assembly Data Catalog

A public collection of manufacturing assembly datasets with easy-to-use Python loaders.

**Goal**: Make real manufacturing assembly data accessible so researchers and engineers can build better AI systems for assembly tasks.

## Overview

AI models are typically trained on internet data, not factory-style assembly data. This repository collects scattered assembly datasets into one place with:
- A central catalog
- One-line Python loaders that return standardized data
- Clear documentation and download instructions

## Available Datasets

| Dataset          | Size       | Key Modalities                          | Focus Area                              | Status          |
|------------------|------------|-----------------------------------------|-----------------------------------------|-----------------|
| Aero Fastener    | 85.6 MB    | Force-torque, kinematics                | Robotic screwing, success/failure       | Full loader     |
| Assemble Them All| ~1 GB      | 3D CAD meshes, assembly sequences       | Physics-based assembly planning         | Full loader     |
| HA-ViD           | 226.63 GB  | Multi-view RGB video, skeleton          | Human industrial assembly               | Skeleton        |
| IKEA ASM         | 420.97 GB  | RGB+depth, pose, segmentation           | Furniture assembly                      | Skeleton        |
| REASSEMBLE       | 54.8 GB    | RGB, event camera, force-torque, audio  | Contact-rich robotic assembly           | Skeleton        |
| HA4M             | 2.92 TB    | RGB, depth, IR, point clouds, skeleton  | Multi-modal mechanical assembly         | Skeleton        |
| IndustReal       | 71.78 GB   | Egocentric RGB, error annotations       | Procedural & execution errors           | Skeleton        |
| MECCANO          | 90.619 GB  | Egocentric RGB+depth, gaze              | Toy motorbike assembly, action anticipation | Skeleton    |
| NIST MOAD        | -          | RGB images, point clouds, CAD models    | Part geometry & mating                  | Skeleton        |

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/kamp-assembly-data.git
cd kamp-assembly-data

# 2. Install dependencies
pip install -r requirements.txt

# 3. List available datasets
python -c "from loaders import list_available_datasets; list_available_datasets()"

# 4. Load a dataset (example)
from loaders import load_dataset
data = load_dataset("Aero Fastener")
print(f"Loaded {len(data['samples'])} samples")
```
# Usage Examples
```python
from loaders import load_dataset

# Load any dataset with one line
data = load_dataset("Aero Fastener")
# or
data = load_dataset("Assemble Them All")

# All loaders return the same structure:
print(data.keys())                    # ['dataset_name', 'description', 'metadata', 'samples']
print(len(data["samples"]))           # number of items
print(data["samples"][0].keys())      # sample fields
```
Note: Large datasets (HA-ViD, IKEA ASM, etc.) will show clear download instructions if the data is not found locally.

# Repository Structure 
```bash
kamp-assembly-data/
├── README.md
├── catalog.csv
├── requirements.txt
├── loaders/
│   ├── __init__.py
│   ├── utils.py
│   ├── aero_fastener.py
│   ├── assemble_them_all.py
│   ├── nist_moad.py
│   ├── reassemble.py
│   ├── meccano.py
│   ├── industreal.py
│   ├── ha_vid.py
│   ├── ikea_asm.py
│   └── ha4m.py
├── data/                     # ← put downloaded datasets here
└── test_loaders.py
```

# How to Add Your Own Data
1. Add an entry to catalog.csv
2. Create a loader in loaders/ following the existing pattern
3. Update __init__.py to include it

# Future Work
- Full loaders for large video datasets
- Knowledge gap analysis (showing where general LLMs fail on assembly tasks)
- Example Jupyter notebooks
- Benchmark scripts

# Citation
If you use this repository, please cite the original dataset papers (links available in catalog.csv).

Built as part of the KAMP Assembly Data project.
Questions or contributions? Open an issue or pull request.
