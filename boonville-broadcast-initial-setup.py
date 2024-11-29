# Boonville Broadcast Project
# Initial Project Structure and Core Components

import uuid
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime

@dataclass
class Business:
    """Represents a local business in the Boonville Broadcast system"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    description: str = ""
    contact_email: str = ""
    partnership_tier: str = "Basic"
    historical_narrative: Optional[str] = None
    location_coordinates: tuple = (0.0, 0.0)
    
    def upgrade_partnership(self, new_tier: str):
        """Upgrade business partnership tier"""
        valid_tiers = ["Basic", "Standard", "Premium", "Platinum"]
        if new_tier in valid_tiers:
            self.partnership_tier = new_tier
        else:
            raise ValueError(f"Invalid partnership tier: {new_tier}")

@dataclass
class UserInteraction:
    """Tracks user interactions with business profiles and tour information"""
    business_id: str
    interaction_type: str
    timestamp: datetime = field(default_factory=datetime.now)
    duration: int = 0  # seconds
    user_demographics: Dict[str, str] = field(default_factory=dict)

class BoonvilleBroadcastSystem:
    def __init__(self):
        self.businesses: Dict[str, Business] = {}
        self.interactions: List[UserInteraction] = []
    
    def register_business(self, business: Business):
        """Register a new business in the system"""
        self.businesses[business.id] = business
    
    def log_interaction(self, interaction: UserInteraction):
        """Log user interaction with a business profile"""
        self.interactions.append(interaction)
    
    def generate_analytics_report(self, business_id: str):
        """Generate analytics report for a specific business"""
        business_interactions = [
            interaction for interaction in self.interactions 
            if interaction.business_id == business_id
        ]
        
        return {
            "total_interactions": len(business_interactions),
            "average_interaction_duration": sum(
                interaction.duration for interaction in business_interactions
            ) / len(business_interactions) if business_interactions else 0,
            "interaction_types": {
                interaction_type: len([
                    i for i in business_interactions 
                    if i.interaction_type == interaction_type
                ]) for interaction_type in set(
                    interaction.interaction_type for interaction in business_interactions
                )
            }
        }

# Example Usage
def main():
    # Initialize the Boonville Broadcast system
    boonville_system = BoonvilleBroadcastSystem()
    
    # Create a sample business
    historic_cafe = Business(
        name="River's Edge Historic Cafe",
        description="A century-old cafe in the heart of Boonville",
        contact_email="contact@riversedgecafe.com",
        historical_narrative="Founded in 1923, this cafe has been a cornerstone of Boonville's community..."
    )
    
    # Register the business
    boonville_system.register_business(historic_cafe)
    
    # Log a sample interaction
    interaction = UserInteraction(
        business_id=historic_cafe.id,
        interaction_type="terminal_view",
        duration=45,
        user_demographics={
            "age_group": "25-34",
            "interests": "local_history"
        }
    )
    boonville_system.log_interaction(interaction)
    
    # Generate analytics
    analytics = boonville_system.generate_analytics_report(historic_cafe.id)
    print(analytics)

if __name__ == "__main__":
    main()