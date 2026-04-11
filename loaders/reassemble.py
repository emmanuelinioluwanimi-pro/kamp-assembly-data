"""
Minimal Loader for REASSEMBLE
Returns only the requested metadata + download link
"""

from typing import Dict, Any


def load_reassemble(data_root: str = "./data") -> Dict[str, Any]:
    return {
        "dataset_name": "REASSEMBLE",
        "description": "REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly on NIST Task Board 1. Includes multi-view RGB, event camera, force-torque, audio, robot proprioception, pose, and action labels.",
        "metadata": {
            "size": "54.8 GB",
            "data_type": "Multimodal (RGB, event camera, audio, force–torque, robot proprioception, pose, action labels)",
            "license": "Creative Commons Attribution 4.0 International",
            "knowledge_type": "Force feedback, success vs failure detection, robot constraints during tight insertions",
            "modalities": ["rgb_video", "event_camera", "force_torque", "audio", "proprioception", "pose", "action_labels"],
            "duration": "781 minutes"
        },
        "download_link": "https://researchdata.tuwien.ac.at/records/0ewrv-8cb44/files/data.zip?download=1\n"
                         "https://researchdata.tuwien.ac.at/records/0ewrv-8cb44/files/poses.zip?download=1\n"
                         "https://researchdata.tuwien.ac.at/records/0ewrv-8cb44/files/splits.zip?download=1",
        "note": "Download the zip files from the links above and extract them."
    }