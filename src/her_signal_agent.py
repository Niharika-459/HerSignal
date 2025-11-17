"""
HerSignal: Main Agent Orchestrator
Coordinates multi-agent system for women's safety
"""

import logging
import time
from datetime import datetime
from typing import Dict, List

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class HerSignalAgent:
    """Main HerSignal Agent - Orchestrates multi-agent safety system"""
    
    def __init__(self):
        """Initialize HerSignal Agent"""
        self.is_active = False
        self.user_profile = {}
        self.alert_history = []
        self.incident_log = []
        logger.info("✓ HerSignal Agent initialized")
    
    def activate(self, user_profile: Dict) -> bool:
        """Activate agent for user"""
        try:
            self.user_profile = user_profile
            self.is_active = True
            logger.info(f"✓ Agent activated for: {user_profile.get('name', 'Unknown')}")
            return True
        except Exception as e:
            logger.error(f"✗ Activation failed: {str(e)}")
            return False
    
    def deactivate(self) -> bool:
        """Deactivate agent"""
        self.is_active = False
        logger.info("✓ Agent deactivated")
        return True
    
    def monitor(self, duration: int = 300) -> None:
        """Start monitoring loop"""
        if not self.is_active:
            logger.warning("Agent not active")
            return
        
        logger.info(f"🔍 Monitoring started for {duration} seconds")
        start_time = time.time()
        iteration = 0
        
        while time.time() - start_time < duration:
            iteration += 1
            try:
                import random
                risk_level = random.uniform(0.0, 1.0)
                logger.info(f"Iteration {iteration}: Risk Level = {risk_level:.2f}")
                
                if risk_level >= 0.7:
                    logger.warning(f"🚨 ALERT: High risk detected!")
                    self._handle_emergency({'risk_level': risk_level})
                
                time.sleep(2)
            except Exception as e:
                logger.error(f"Error in monitoring: {str(e)}")
        
        logger.info("✓ Monitoring ended")
    
    def _handle_emergency(self, data: Dict) -> None:
        """Handle emergency"""
        alert = {
            'timestamp': datetime.now().isoformat(),
            'user': self.user_profile.get('name', 'Unknown'),
            'risk_level': data.get('risk_level', 0.0),
            'type': 'emergency_alert'
        }
        self.alert_history.append(alert)
        self.incident_log.append(alert)
        logger.critical(f"🚨 EMERGENCY ALERT: {alert}")
    
    def manual_alert(self) -> bool:
        """Manually trigger alert"""
        logger.critical("🚨 MANUAL EMERGENCY ALERT TRIGGERED")
        self._handle_emergency({'risk_level': 1.0})
        return True
    
    def get_status(self) -> Dict:
        """Get agent status"""
        return {
            'is_active': self.is_active,
            'user': self.user_profile.get('name', 'N/A'),
            'total_alerts': len(self.alert_history),
            'incidents_logged': len(self.incident_log)
        }


def main():
    """Demo entry point"""
    print("=" * 60)
    print("       HerSignal - AI Women's Safety Agent v1.0.0")
    print("=" * 60)
    
    # Initialize agent
    agent = HerSignalAgent()
    
    # Demo user
    user_profile = {
        'name': 'Priya Sharma',
        'phone': '+91-9876543210',
        'emergency_contacts': [
            {'name': 'Mom', 'phone': '+91-9123456789'},
            {'name': 'Police', 'phone': '100'},
            {'name': 'Friend', 'phone': '+91-9111111111'}
        ]
    }
    
    # Activate
    if agent.activate(user_profile):
        print(f"✓ Agent activated for {user_profile['name']}")
        print(f"✓ Emergency contacts: {len(user_profile['emergency_contacts'])}")
        
        # Start monitoring (10 seconds for demo)
        print("\n🔍 Starting monitoring...")
        agent.monitor(duration=10)
        
        # Get final status
        status = agent.get_status()
        print(f"\n📊 Final Status: {status}")
    else:
        print("✗ Failed to activate agent")


if __name__ == "__main__":
    main()
