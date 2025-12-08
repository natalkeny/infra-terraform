import os
import logging
import json
from typing import Dict, List, Optional

class TerraformConfig:
    def __init__(self, path: str):
        self.path = path
        self.config = self.load_config()

    def load_config(self) -> Dict:
        with open(self.path, 'r') as f:
            return json.load(f)

    def get_variable(self, name: str) -> Optional[str]:
        for section in self.config:
            if name in self.config[section]:
                return self.config[section][name]
        return None

    def get_variables(self) -> Dict:
        variables = {}
        for section in self.config:
            variables.update(self.config[section])
        return variables

    def get_output(self, name: str) -> Optional[str]:
        for section in self.config:
            if 'output' in section and name in self.config[section]['output']:
                return self.config[section]['output'][name]
        return None

def get_terraform_config(path: str) -> TerraformConfig:
    return TerraformConfig(path)

def get_root_dir() -> str:
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_env_variable(name: str) -> str:
    return os.environ.get(name)

def get_log_level() -> int:
    return logging.getLevelName(os.environ.get('LOG_LEVEL', 'INFO')).upper()