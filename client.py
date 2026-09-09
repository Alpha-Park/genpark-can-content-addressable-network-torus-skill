"""
Autonomous Agent Content-Addressable Network (CAN) Skill
Pure Python Standard Library implementation.
"""
from typing import Tuple, Dict, Any

class CANNode:
    """
    2D CAN node managing a hyper-rectangular zone.
    """
    def __init__(self, node_id: str, x_range: Tuple[float, float], y_range: Tuple[float, float]):
        self.id = node_id
        self.x0, self.x1 = x_range
        self.y0, self.y1 = y_range

    def contains(self, x: float, y: float) -> bool:
        return self.x0 <= x <= self.x1 and self.y0 <= y <= self.y1

    def get_info(self) -> Dict[str, Any]:
        return {
            "node_id": self.id,
            "x_bounds": [self.x0, self.x1],
            "y_bounds": [self.y0, self.y1],
            "area": (self.x1 - self.x0) * (self.y1 - self.y0)
        }
