from typing import List, Dict, TypedDict

class WorkflowStep(TypedDict):
    number: int
    title: str
    agent: str
    description: str
    input_type: str
    output_type: str

TRANSFORMATION_WORKFLOW: List[WorkflowStep] = [
    {"number": 1, "title": "TAS Extraction", "agent": "GPTASe", "description": "Extracting raw Task Agnostic Steps from the high-level objective.", "input_type": "⫻data/obj:", "output_type": "⫻data/tas:"},
    {"number": 2, "title": "TAS Purification", "agent": "puTASe", "description": "Refining and removing ambiguity from extracted steps.", "input_type": "⫻data/tas:", "output_type": "⫻data/ptas:"},
    {"number": 3, "title": "Workflow Structuring", "agent": "Lyra", "description": "Creating optimized workflows from purified steps.", "input_type": "⫻data/ptas:", "output_type": "⫻data/spec:"},
    {"number": 4, "title": "Cognitive Coordination", "agent": "Fizz La Metta", "description": "Aligning agent roles and responsibilities.", "input_type": "⫻data/spec:", "output_type": "⫻cmd/exec:"},
    {"number": 5, "title": "Knowledge Transfer", "agent": "AI Tutor", "description": "Providing domain-specific insights and context.", "input_type": "⫻query/clarify:", "output_type": "⫻data/logic:"},
    {"number": 6, "title": "Code Context", "agent": "Codein", "description": "Analyzing implementation needs and providing code references.", "input_type": "⫻data/spec:", "output_type": "⫻data/logic:"},
    {"number": 7, "title": "Prompt Refinement", "agent": "Lyra", "description": "Optimizing prompts based on feedback loops.", "input_type": "⫻query/clarify:", "output_type": "⫻data/spec:"},
    {"number": 8, "title": "Protocol Establishment", "agent": "Fizz La Metta", "description": "Creating operational rules and protocols.", "input_type": "⫻data/spec:", "output_type": "⫻cmd/mode:"},
    {"number": 9, "title": "System Monitoring", "agent": "Fizz La Metta", "description": "Tracking execution and collecting performance metrics.", "input_type": "⫻data/logic:", "output_type": "⫻data/obj:"},
    {"number": 10, "title": "Ethical Compliance", "agent": "Dima", "description": "Validating decisions against ethical guidelines.", "input_type": "⫻query/clarify:", "output_type": "⫻cmd/halt:"},
    {"number": 11, "title": "Visual Assets", "agent": "AR-00L", "description": "Creating visual prototypes and design elements.", "input_type": "⫻data/spec:", "output_type": "⫻data/logic:"},
    {"number": 12, "title": "Operational Rules", "agent": "QllickBuzz", "description": "Refining rules for edge cases and exceptions.", "input_type": "⫻data/ptas:", "output_type": "⫻cmd/mode:"},
    {"number": 13, "title": "Strategic Plans", "agent": "WePlan", "description": "Developing long-term roadmaps and strategies.", "input_type": "⫻data/obj:", "output_type": "⫻data/spec:"},
    {"number": 14, "title": "NL Translation", "agent": "Kick La Metta", "description": "Converting informal requests to formal tasks.", "input_type": "⫻data/obj:", "output_type": "⫻data/ptas:"},
    {"number": 15, "title": "Dynamic Role Adaptation", "agent": "Orchestrator", "description": "Adjusting agent roles based on workload shifts.", "input_type": "⫻cmd/exec:", "output_type": "⫻flow:"},
    {"number": 16, "title": "Joint Decisions", "agent": "Dima", "description": "Resolving conflicts and reaching consensus.", "input_type": "⫻query/clarify:", "output_type": "⫻cmd/halt:"},
    {"number": 17, "title": "Integrity Monitoring", "agent": "SystemMonitor", "description": "Ensuring system security and data integrity.", "input_type": "⫻data/logic:", "output_type": "⫻cmd/halt:"},
    {"number": 18, "title": "Tailored Plans", "agent": "WePlan", "description": "Customizing workflows based on user feedback.", "input_type": "⫻query/clarify:", "output_type": "⫻data/spec:"},
    {"number": 19, "title": "Holistic Task Approach", "agent": "Orchestrator", "description": "Unifying cross-domain tasks and execution.", "input_type": "⫻data/obj:", "output_type": "⫻flow:"},
    {"number": 20, "title": "Review & Refinement", "agent": "All", "description": "Final review and iterative improvements.", "input_type": "⫻data/logic:", "output_type": "⫻data/ptas:"}
]
