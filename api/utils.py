import os
import json
from typing import Dict, List

def load_config(file_path: str) -> Dict:
    with open(file_path, 'r') as f:
        return json.load(f)

def load_env_variables() -> Dict:
    env_variables = {}
    for var in os.environ:
        env_variables[var] = os.environ[var]
    return env_variables

def validate_env_variables(env_variables: Dict, required_variables: List[str]) -> None:
    for var in required_variables:
        if var not in env_variables:
            raise ValueError(f"Environment variable '{var}' is not set")

def get_terraform_version() -> str:
    try:
        with open('terraform_version.txt', 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return "Unknown"