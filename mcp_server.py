"""MCP Server for CAN Routing Skill."""
import json
import sys
from client import CANNode

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "check_can_zone",
                            "description": "Check if coordinate falls within CAN zone",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "node_id": {"type": "string"},
                                    "x_range": {"type": "array", "items": {"type": "number"}},
                                    "y_range": {"type": "array", "items": {"type": "number"}},
                                    "point": {"type": "array", "items": {"type": "number"}}
                                },
                                "required": ["node_id", "x_range", "y_range", "point"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                node = CANNode(args["node_id"], tuple(args["x_range"]), tuple(args["y_range"]))
                px, py = args["point"]
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps({"inside_zone": node.contains(px, py)})}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
