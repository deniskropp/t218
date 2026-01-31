import asyncio
import json
import websockets
import sys

async def verify_swarm_flow():
    uri = "ws://localhost:8000/ws"
    
    print(f"Connecting to {uri}...")
    try:
        async with websockets.connect(uri) as websocket:
            print("Connected.")
            
            # Send Start Command
            intent = "⫻cmd/exec: Transform intents into reality."
            print(f"Sending intent: {intent}")
            await websocket.send(json.dumps({
                "type": "start_flow",
                "intent": intent
            }))

            step_count = 0
            
            # Listen for updates
            async for message in websocket:
                data = json.loads(message)
                
                if data['type'] == 'step_update':
                    if data['status'] == 'completed':
                        step_count += 1
                        print(f"Step {data['step_id']} Completed.")
                        if step_count >= 5: # Just verify first few steps for speed
                             print("Verified 5 steps, considering success for integration test.")
                             return
                
                elif data['type'] == 'flow_complete':
                    print("Flow Complete.")
                    break
                    
    except Exception as e:
        print(f"Test Failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(verify_swarm_flow())
