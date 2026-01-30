import asyncio
import random
from typing import List, Dict
from src.shared.models import OCSFlow, TransformationStep, KickLangPacket
from src.shared.workflow import SF20_WORKFLOW_STEPS
from src.shared.protocol import KickHeader
from src.shared.llm_provider import MistralProvider

class SwarmEngine:
    def __init__(self):
        self.active_flows: Dict[str, OCSFlow] = {}
        self.provider = MistralProvider()

    def create_flow(self, intent: str) -> OCSFlow:
        # Detect KickLang Header if present
        try:
            if intent.startswith("⫻"):
                header = KickHeader.from_string(intent.split("\n")[0])
                print(f"Detected KickLang Header: {header.to_string()}")
        except Exception as e:
            print(f"Failed to parse KickLang header: {e}")

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

            # Generate Prompt for LLM
            prompt = f"Step: {step.title}\nAgent: {step.agent}\nContext: {flow.intent}\nOutput Type: {step.output_type}\n\nPerform this step and provide the result."

            # Execute Step via Provider
            result = await self.provider.generate_response(prompt)
            
            step.status = "completed"
            step.result = result

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
