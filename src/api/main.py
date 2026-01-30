from fastapi import FastAPI, WebSocket, Request, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.shared.data import SF20_WORKFLOW_STEPS
from src.api.engine import SwarmEngine
from pathlib import Path

app = FastAPI(title="OCS Node")

# Setup Templates
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Initialize Engine
engine = SwarmEngine()

@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "steps": SF20_WORKFLOW_STEPS
    })

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            if data.get("type") == "start_flow":
                intent = data.get("intent")
                flow = engine.create_flow(intent)
                await engine.run_flow(flow.flow_id, websocket)
    except WebSocketDisconnect:
        print("Client disconnected")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=8000, reload=True)
