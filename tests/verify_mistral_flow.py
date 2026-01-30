import asyncio
import websockets
import json

async def verify_flow():
    uri = "ws://localhost:8000/ws"
    async with websockets.connect(uri) as websocket:
        print(f"Connected to {uri}")

        # Start Flow
        start_msg = {
            "type": "start_flow",
            "intent": "⫻query/clarify:Verify Mistral Connection"
        }
        await websocket.send(json.dumps(start_msg))
        print("Sent start_flow command")

        while True:
            try:
                message = await websocket.recv()
                data = json.loads(message)
                
                if data["type"] == "step_update":
                    print(f"Step {data.get('step_id')}: {data.get('status')}")
                    if data.get("result"):
                        print(f"  Result: {data['result'][:50]}...")
                
                elif data["type"] == "flow_complete":
                     print(f"Flow {data.get('flow_id')} complete!")
                     break
            except Exception as e:
                print(f"Error: {e}")
                break

if __name__ == "__main__":
    asyncio.run(verify_flow())
