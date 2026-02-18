import logging
from typing import Dict, Any
import requests
import json

class DataCollector:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.headers = {
            'Content-Type': 'application/json',
        }
    
    def collect_data(self, endpoint: str, data: Dict[str, Any]) -> None:
        try:
            response = requests.post(endpoint, headers=self.headers, json=data)
            response.raise_for_status()
            self.logger.info(f"Data collected successfully. Response: {response.text}")
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to collect data: {str(e)}")