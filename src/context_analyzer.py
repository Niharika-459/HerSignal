"""
Context Analyzer Module
Analyzes sensor data to determine risk level
"""

import logging
import random
from typing import Dict

logger = logging.getLogger(__name__)


class ContextAnalyzer:
    """Analyzes context and determines risk level"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.location_history = []
    
    def analyze(self, sensor_data: Dict, user_profile: Dict) -> Dict:
        """Analyze sensor data and return risk assessment"""
        risk_score = 0.0
        reasons = []
        
        try:
            # Check GPS data
            if sensor_data.get('gps'):
                gps_risk, gps_reason = self._analyze_location(
                    sensor_data['gps'], 
                    user_profile.get('safe_zones', [])
                )
                risk_score += gps_risk * 0.3
                if gps_reason:
                    reasons.append(gps_reason)
            
            # Check accelerometer for unusual movement
            if sensor_data.get('accelerometer'):
                accel_risk, accel_reason = self._analyze_movement(sensor_data['accelerometer'])
                risk_score += accel_risk * 0.2
                if accel_reason:
                    reasons.append(accel_reason)
            
            # Check audio for distress
            if sensor_data.get('microphone'):
                audio_risk, audio_reason = self._analyze_audio(sensor_data['microphone'])
                risk_score += audio_risk * 0.3
                if audio_reason:
                    reasons.append(audio_reason)
            
            # Check battery and signal
            if sensor_data.get('battery', 100) < 15:
                risk_score += 0.1
                reasons.append("Low battery")
            
            # Normalize risk score to 0-1
            risk_score = min(risk_score, 1.0)
            
            return {
                'risk_level': risk_score,
                'risk_category': self._get_risk_category(risk_score),
                'reasons': reasons,
                'timestamp': sensor_data.get('timestamp')
            }
        
        except Exception as e:
            logger.error(f"Error analyzing context: {str(e)}")
            return {'risk_level': 0.0, 'reasons': ['Analysis error']}
    
    def _analyze_location(self, gps_data: Dict, safe_zones: list) -> tuple:
        """Analyze location risk"""
        # Simulated analysis
        risk = random.uniform(0, 0.3)
        reason = "Location analysis: " + ("In unsafe area" if risk > 0.2 else "Location ok")
        return risk, reason if risk > 0.15 else None
    
    def _analyze_movement(self, accel_data: Dict) -> tuple:
        """Analyze movement patterns"""
        magnitude = accel_data.get('magnitude', 0)
        # High sudden movement might indicate struggle
        risk = min(magnitude / 50, 1.0)
        reason = "Unusual movement detected" if risk > 0.5 else None
        return risk, reason
    
    def _analyze_audio(self, audio_data: Dict) -> tuple:
        """Analyze audio for distress"""
        if audio_data.get('distress_detected'):
            return audio_data.get('confidence', 0.7), "Distress detected in audio"
        return 0.0, None
    
    def _get_risk_category(self, risk_score: float) -> str:
        """Categorize risk level"""
        if risk_score < 0.3:
            return "LOW"
        elif risk_score < 0.6:
            return "MEDIUM"
        elif risk_score < 0.8:
            return "HIGH"
        else:
            return "CRITICAL"
