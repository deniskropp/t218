from fastapi import FastAPI
from src.shared.workflow import TRANSFORMATION_WORKFLOW

app = FastAPI(
    title="OCS Node API",
    description="SF20 Transformation Engine Interface",
    version="0.1.0"
)

@app.get("/health")
async def health_check():
    """
    Basic system health check.
    """
    return {"status": "online", "system": "OCS Node"}

@app.get("/workflow")
async def get_workflow():
    """
    Returns the defined 20-step transformation workflow.
    """
    return {"steps": TRANSFORMATION_WORKFLOW}

@app.post("/execute")
async def execute_task(objective: str):
    """
    Placeholder for task execution trigger.
    """
    # TODO: Implement actual execution logic
    return {
        "status": "accepted", 
        "objective": objective,
        "message": "Task queued for processing [Mock]"
    }
