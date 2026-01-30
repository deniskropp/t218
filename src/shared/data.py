# SF20 Transformation Workflow Data
from src.shared.models import TransformationStep

SF20_WORKFLOW_STEPS = [
    TransformationStep(id=1, title='TAS Extraction', agent='GPTASe', output_type='⫻data/tas:'),
    TransformationStep(id=2, title='TAS Purification', agent='puTASe', output_type='⫻data/ptas:'),
    TransformationStep(id=3, title='Workflow Structuring', agent='Lyra', output_type='⫻data/spec:'),
    TransformationStep(id=4, title='Cognitive Coordination', agent='Fizz La Metta', output_type='⫻cmd/exec:'),
    TransformationStep(id=5, title='Knowledge Transfer', agent='AI Tutor', output_type='⫻data/logic:'),
    TransformationStep(id=6, title='Code Context', agent='Codein', output_type='⫻data/logic:'),
    TransformationStep(id=7, title='Prompt Refinement', agent='Lyra', output_type='⫻data/spec:'),
    TransformationStep(id=8, title='Protocol Establishment', agent='Fizz La Metta', output_type='⫻cmd/mode:'),
    TransformationStep(id=9, title='System Monitoring', agent='Fizz La Metta', output_type='⫻data/obj:'),
    TransformationStep(id=10, title='Ethical Compliance', agent='Dima', output_type='⫻cmd/halt:'),
    TransformationStep(id=11, title='Visual Assets', agent='AR-00L', output_type='⫻data/logic:'),
    TransformationStep(id=12, title='Operational Rules', agent='QllickBuzz & QllickFizz', output_type='⫻cmd/mode:'),
    TransformationStep(id=13, title='Strategic Plans', agent='WePlan', output_type='⫻data/spec:'),
    TransformationStep(id=14, title='NL Translation', agent='Kick La Metta', output_type='⫻data/ptas:'),
    TransformationStep(id=15, title='Dynamic Role Adaptation', agent='Orchestrator', output_type='⫻flow:'),
    TransformationStep(id=16, title='Joint Decisions', agent='Dima', output_type='⫻cmd/halt:'),
    TransformationStep(id=17, title='Integrity Monitoring', agent='SystemMonitor', output_type='⫻cmd/halt:'),
    TransformationStep(id=18, title='Tailored Plans', agent='WePlan', output_type='⫻data/spec:'),
    TransformationStep(id=19, title='Holistic Task Approach', agent='Orchestrator', output_type='⫻flow:'),
    TransformationStep(id=20, title='Review & Refinement', agent='All', output_type='⫻data/ptas:')
]
