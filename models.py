from dataclasses import dataclass
from typing import Dict

@dataclass
class RoadSegment:
    road_id: str
    road_name: str
    location: Dict[str, float]  # e.g., {"lat": 12.9716, "lon": 77.5946}
    road_type: str              # NH, SH, MDR
    contractor_name: str
    last_relaying_date: str     # YYYY-MM-DD
    budget_sanctioned: float
    budget_spent: float
    executive_engineer_name: str
    executive_engineer_contact: str

    @classmethod
    def from_dict(cls, data: dict) -> "RoadSegment":
        return cls(**data)
