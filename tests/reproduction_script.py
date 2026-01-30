import asyncio
from typing import Optional
from src.api.engine import SwarmEngine
from src.shared.interfaces import FlowNotifier
from src.shared.llm_provider import MistralProvider

# Mock Provider
class MockProvider(MistralProvider):
    async def generate_response(self, prompt: str) -> str:
        # Extract output type from prompt to return a valid fake response
        output_type = "⫻data/logic:"
        if "Output Type: ⫻" in prompt:
           output_type = prompt.split("Output Type: ")[1].split("\n")[0].strip()
        
        # Also handle the new strict prompting style
        if "KickLang header: ⫻" in prompt:
             output_type = prompt.split("KickLang header: ")[1].split("\n")[0].strip()

        print(f"[MockProvider] Received prompt length: {len(prompt)}")
        return f"{output_type} [MOCK RESPONSE]"

# Mock Notifier
class MockNotifier(FlowNotifier):
    async def step_started(self, step_id: int):
        print(f"[Notifier] Step {step_id} started.")

    async def step_completed(self, step_id: int, result: str):
        print(f"[Notifier] Step {step_id} completed. Result: {result.strip()}")

    async def flow_completed(self, flow_id: str):
        print(f"[Notifier] Flow {flow_id} completed.")

async def main():
    engine = SwarmEngine()
    # Inject mock provider
    engine.provider = MockProvider()
    
    flow = engine.create_flow("⫻data/obj: Test Flow")
    notifier = MockNotifier()
    
    print(f"Starting flow {flow.flow_id} with {len(flow.steps)} steps...")
    await engine.run_flow(flow.flow_id, notifier)
    print("Test finished.")

if __name__ == "__main__":
    asyncio.run(main())
