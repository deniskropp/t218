import asyncio
import random
from typing import List, Dict
from src.shared.models import OCSFlow, TransformationStep, KickLangPacket
from src.shared.data import SF20_WORKFLOW_STEPS

class SwarmEngine:
    def __init__(self):
        self.active_flows: Dict[str, OCSFlow] = {}

    def create_flow(self, intent: str) -> OCSFlow:
        # Clone the template steps for this new flow
        steps = [step.model_copy() for step in SF20_WORKFLOW_STEPS]
        flow = OCSFlow(intent=intent, steps=steps)
        self.active_flows[flow.flow_id] = flow
        return flow

    async def run_flow(self, flow_id: str, websocket):
        flow = self.active_flows.get(flow_id)
        if not flow:
            return

        flow.status = "active"
        
        # In the context of "Swarm", we treat ⫻flow:ocs/swarm rules:
        # "Parallelized execution of independent tracks"
        # However, the 20-step transformation is largely sequential in its definition.
        # To respect the "Simulation" aspect while keeping it verified, we will 
        # iterate but simulate "Agent Handoffs" with delays.
        
        for i, step in enumerate(flow.steps):
            flow.current_step_index = i
            step.status = "running"
            
            # Notify Client: Step Started
            await websocket.send_json({
                "type": "step_update",
                "step_id": step.id,
                "status": "running"
            })

            # Simulate "Work" being done by the Agent
            # Random duration between 0.5s and 1.5s
            duration = random.uniform(0.5, 1.5)
            await asyncio.sleep(duration)

            # Check for failure (Optional, keeping it happy path for demo)
            step.status = "completed"
            step.result = f"Generated {step.output_type} block."

            # Notify Client: Step Completed
            await websocket.send_json({
                "type": "step_update",
                "step_id": step.id,
                "status": "completed",
                "result": step.result
            })

        flow.status = "completed"
        await websocket.send_json({
            "type": "flow_complete",
            "flow_id": flow.flow_id
        })
