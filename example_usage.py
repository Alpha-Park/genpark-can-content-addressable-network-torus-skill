"""Example usage for CAN Routing Skill."""
from client import CANNode

def main():
    print("Executing CAN Torus Routing...")
    node = CANNode("zone_quadrant_1", (0.0, 0.5), (0.0, 0.5))
    print("CAN Zone Info:", node.get_info())
    assert node.contains(0.2, 0.3) == True
    assert node.contains(0.8, 0.3) == False
    print("CAN Torus Routing verified successfully!")

if __name__ == "__main__":
    main()
