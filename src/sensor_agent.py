"""
Sensor Agent Module
Collects data from device sensors
"""

import logging
import random
from datetime import datetime
from typing import Dict

logger = logging.getLogger(__name__)


class SensorAgent:
    """Handles sensor data collection"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.last_location = None
        self.movement_history = []
    
    def collect_data(self) -> Dict:
        """Collect sensor data"""
        try:
            data = {
                'timestamp': datetime.now().isoformat(),
                'gps': self._get_gps_data() if self.config['sensors']['gps_enabled'] else None,
                'accelerometer': self._get_accelerometer_data() if self.config['sensors']['accelerometer_enabled'] else None,
                'microphone': self._get_microphone_data() if self.config['sensors']['microphone_enabled'] else None,
                'battery': self._get_battery_level(),
                'signal_strength': self._get_signal_strength()
            }
            logger.debug(f"Sensor data collected: {data}")
            return data
        except Exception as e:
            logger.error(f"Error collecting sensor data: {str(e)}")
            return {}
    
    def _get_gps_data(self) -> Dict:
        """Get GPS location (simulated)"""
        # In real implementation, use actual GPS
        lat = 28.6139 + random.uniform(-0.01, 0.01)
        lon = 77.2090 + random.uniform(-0.01, 0.01)
        return {
            'latitude': lat,
            'longitude': lon,
            'accuracy': random.uniform(5, 20),
            'timestamp': datetime.now().isoformat()
        }
    
    def _get_accelerometer_data(self) -> Dict:
        """Get accelerometer data (simulated)"""
        return {
            'x': random.uniform(-10, 10),
            'y': random.uniform(-10, 10),
            'z': random.uniform(-10, 10),
            'magnitude': random.uniform(0, 30)
        }
    
    def _get_microphone_data(self) -> Dict:
        """Analyze audio for distress (simulated)"""
        return {
            'noise_level': random.uniform(40, 90),  # dB
            'distress_detected': random.random() > 0.9,  # 10% chance for demo
            'confidence': random.uniform(0.5, 1.0)
        }
    
    def _get_battery_level(self) -> int:
        """Get device battery level"""
        return random.randint(20, 100)
    
    def _get_signal_strength(self) -> int:
        """Get network signal strength"""
        return random.randint(1, 5)
