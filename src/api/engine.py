import asyncio
import random
from typing import List, Dict, Optional
from src.shared.models import OCSFlow, TransformationStep, KickLangPacket, MessageType
from src.shared.workflow import SF20_WORKFLOW_STEPS, TransformationStep
from src.shared.protocol import KickHeader
from src.shared.llm_provider import MistralProvider
from src.shared.interfaces import FlowNotifier
from src.shared.parser import KickLangParser

class SwarmEngine:
    def __init__(self):
        self.active_flows: Dict[str, OCSFlow] = {}
        self.provider = MistralProvider()

    def create_flow(self, intent: str) -> OCSFlow:
        # Clone the template steps for this new flow
        steps = [step.model_copy() for step in SF20_WORKFLOW_STEPS]
        flow = OCSFlow(intent=intent, steps=steps)
        self.active_flows[flow.flow_id] = flow
        return flow

    async def run_flow(self, flow_id: str, notifier):
        """
        Executes a flow using the provided notifier for updates.
        """
        flow = self.active_flows.get(flow_id)
        if not flow:
            return

        flow.status = "active"
        execution_context = []

        # Use KickLangParser to parse the intent if it follows the protocol
        intent_directive = KickLangParser.parse_directive(flow.intent)
        if intent_directive:
            print(f"Parsed Intent Directive: {intent_directive}")

        # In a full swarm implementation, we would build a dependency graph here.
        # For SF20, we follow the 20-step linear sequence, but we execute them 
        # as if they were autonomous agents being triggered.
        
        for i, step in enumerate(flow.steps):
            flow.current_step_index = i
            step.status = "running"
            
            # Notify: Step Started
            await notifier.send_json({
                "type": "step_update",
                "step_id": step.id,
                "status": "active"
            })

            # Construct the Context Block
            context_block = "\n".join(execution_context) if execution_context else "No prior context."

            # Generate Prompt
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
                f"Perform the task '{step.title}'."
            )

            # Flatten delay simulation (random 0.5s - 1.5s)
            await asyncio.sleep(random.uniform(0.5, 1.5))

            # Execute Step via Provider
            result = await self.provider.generate_response(prompt)
            
            # Validation via Parser
            parsed_result = KickLangParser.parse_line(result)
            if parsed_result:
                 # If we successfully parsed it, we can use the structured data
                 pass
            
            step.status = "completed"
            step.result = result
            
            execution_context.append(f"[Step {step.id} - {step.agent}]:\n{result}\n")

            # Check for HALT condition (simulation)
            if "⫻cmd/halt:" in result:
                # Placeholder for halt logic
                pass 

            # Notify: Step Completed
            await notifier.send_json({
                "type": "step_update",
                "step_id": step.id,
                "status": "completed",
                "output": result
            })

        flow.status = "completed"
        await notifier.send_json({
            "type": "flow_complete",
            "flow_id": flow.flow_id
        })
