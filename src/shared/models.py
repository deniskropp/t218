from datetime import datetime
from typing import List, Optional, Literal, Dict, Any, Union
from pydantic import BaseModel, Field
from enum import Enum
import uuid

# -- KickLang Protocol Models --

class MessageType(str, Enum):
    CMD = "cmd"
    DATA = "data"
    QUERY = "query"
    FLOW = "flow"
    PROTOCOL = "protocol"
    PLAN = "plan"
    LOGIC = "logic"

class KickLangDirective(BaseModel):
    command: str
    parameters: Dict[str, Any] = Field(default_factory=dict)

class KickLangPayload(BaseModel):
    key: str
    value: Any

class KickLangPacket(BaseModel):
    """Represents a standard data packet in the KickLang protocol."""
    header: str = Field(..., description="e.g. ⫻cmd/exec:")
    payload: Any = Field(..., description="The content of the packet.")
    timestamp: datetime = Field(default_factory=datetime.now)

class TransformationStep(BaseModel):
    """Represents a single step in the SF20 Transformation workflow."""
    id: int
    title: str
    agent: str
    output_type: str = Field(..., description="The expected KickLang output type, e.g. ⫻data/tas:")
    status: Literal["pending", "running", "completed", "failed"] = "pending"
    duration_ms: Optional[int] = None
    result: Optional[str] = None

class OCSFlow(BaseModel):
    """Represents an active flow execution."""
    flow_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    intent: str
    steps: List[TransformationStep]
    status: Literal["active", "completed", "halted"] = "active"
    current_step_index: int = 0
    artifacts: Dict[str, Any] = Field(default_factory=dict)
