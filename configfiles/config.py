"""
config.py

Loads configuration from config.yaml and provides it as a dictionary `config`.
"""

import os
import yaml

# Path to config.yaml
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.yaml")

# Load the YAML configuration
with open(CONFIG_FILE, "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)
