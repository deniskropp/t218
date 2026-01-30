import asyncio
import sys
import json
from websockets.sync.client import connect

def test_websocket():
    uri = "ws://0.0.0.0:8000/ws"
    try:
        with connect(uri) as websocket:
            print("Connected to WebSocket")
            
            # Send Start Flow
            payload = {
                "type": "start_flow",
                "intent": "Test Intent"
            }
            websocket.send(json.dumps(payload))
            print("Sent start_flow")
            
            # Expect at least one step_update
            for _ in range(3):
                message = websocket.recv()
                data = json.loads(message)
                print(f"Received: {data.get('type')} - {data.get('status')}")
                if data.get('type') == 'step_update':
                    print("SUCCESS: Received step update")
                    return
                    
    except Exception as e:
        print(f"FAILED: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_websocket()
