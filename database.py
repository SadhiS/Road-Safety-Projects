import json
import math
from typing import List, Optional
from models import RoadSegment

def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate the great circle distance in kilometers between two points on the earth."""
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371 # Radius of earth in kilometers
    return c * r

class RoadDatabase:
    def __init__(self, data_file: str):
        self.data_file = data_file
        self.roads: List[RoadSegment] = []
        self._load_data()

    def _load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.roads = [RoadSegment.from_dict(item) for item in data]
        except FileNotFoundError:
            print(f"Warning: Data file {self.data_file} not found. Starting with an empty database.")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in {self.data_file}.")

    def find_road_by_id(self, road_id: str) -> Optional[RoadSegment]:
        for road in self.roads:
            if road.road_id.lower() == road_id.lower():
                return road
        return None

    def find_road_by_name(self, name: str) -> Optional[RoadSegment]:
        # Simple exact or partial match
        for road in self.roads:
            if name.lower() in road.road_name.lower():
                return road
        return None

    def find_nearest_road(self, lat: float, lon: float, max_distance_km: float = 5.0) -> Optional[RoadSegment]:
        nearest_road = None
        min_distance = float('inf')

        for road in self.roads:
            dist = haversine(lat, lon, road.location['lat'], road.location['lon'])
            if dist < min_distance and dist <= max_distance_km:
                min_distance = dist
                nearest_road = road

        return nearest_road
