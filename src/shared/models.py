from datetime import datetime
from typing import List, Optional, Literal, Dict, Any
from pydantic import BaseModel, Field
import uuid

# -- KickLang Protocol Models --

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
