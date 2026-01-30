import asyncio
import random
from typing import List, Dict
from src.shared.models import OCSFlow, TransformationStep, KickLangPacket
from src.shared.workflow import SF20_WORKFLOW_STEPS
from src.shared.protocol import KickHeader
from src.shared.llm_provider import MistralProvider
from src.shared.interfaces import FlowNotifier

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

    async def run_flow(self, flow_id: str, notifier):
        """
        Executes a flow using the provided notifier for updates.
        :param flow_id: The ID of the flow to execute
        :param notifier: An instance implementing FlowNotifier (e.g. WebSocket or CLI console)
        """
        flow = self.active_flows.get(flow_id)
        if not flow:
            return

        flow.status = "active"
        
        # Accumulate context from all previous steps
        # In a real system, this might be selective or summarized.
        execution_context = []

        for i, step in enumerate(flow.steps):
            flow.current_step_index = i
            step.status = "running"
            
            # Notify: Step Started
            await notifier.step_started(step.id)

            # Construct the Context Block
            context_block = "\n".join(execution_context) if execution_context else "No prior context."

            # Generate Prompt for LLM with rigid KickLang constraints
            # We strictly enforce the Agent Persona and the required Output Type.
            prompt = (
                f"--- SYSTEM ---\n"
                f"You are {step.agent}.\n"
                f"Your task is {step.title}.\n"
                f"You MUST strictly output your response starting with the KickLang header: {step.output_type}\n"
                f"Do not include any conversational filler before or after the KickLang packet.\n\n"
                f"--- CONTEXT ---\n"
                f"User Intent: {flow.intent}\n"
                f"Prior Execution History:\n{context_block}\n\n"
                f"--- INSTRUCTION ---\n"
                f"Perform the task '{step.title}' and provide the result using the header {step.output_type}."
            )

            # Flatten delay simulation (random 0.5s - 1.5s) to mimic "thinking" / agent handoff
            await asyncio.sleep(random.uniform(0.5, 1.5))

            # Execute Step via Provider
            result = await self.provider.generate_response(prompt)
            
            step.status = "completed"
            step.result = result
            
            # Accumulate this result into the execution context for future steps
            execution_context.append(f"[Step {step.id} - {step.agent}]:\n{result}\n")

            # Check for HALT condition (simulation)
            if "⫻cmd/halt:" in result or step.output_type == "⫻cmd/halt:":
                # In a real system, we would pause execution here and wait for user input.
                # For now, we log it and proceed, effectively "auto-approving" in simulation mode.
                pass 

            # Notify: Step Completed
            await notifier.step_completed(step.id, result)

        flow.status = "completed"
        await notifier.flow_completed(flow.flow_id)
