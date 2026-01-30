from enum import Enum
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field, field_validator

class KickAction(str, Enum):
    """
    Standard KickLang actions/verbs.
    """
    # Directives
    EXEC = "exec"
    HALT = "halt"
    MODE = "mode"
    
    # Payload Types
    OBJ = "obj"      # Objective
    TAS = "tas"      # Task Agnostic Steps
    PTAS = "ptas"    # Purified TAS
    SPEC = "spec"    # Specification/Workflow
    LOGIC = "logic"  # Logic/Content
    
    # Query Types
    CLARIFY = "clarify"

class KickHeader(BaseModel):
    """
    Represents the ⫻header/ portion of a KickLang message.
    e.g., ⫻cmd/exec:
    """
    type: str  # cmd, data, query
    action: KickAction
    target: Optional[str] = None # e.g., Agent Name in ⫻cmd/exec:AgentName

    @classmethod
    def from_string(cls, header_str: str) -> "KickHeader":
        """
        Parses a string like '⫻cmd/exec:Target' into a KickHeader object.
        """
        clean = header_str.strip().lstrip("⫻").rstrip(":")
        parts = clean.split("/")
        
        if len(parts) != 2:
            raise ValueError(f"Invalid KickLang header format: {header_str}")
            
        h_type, rest = parts
        
        if ":" in rest:
            action_str, target = rest.split(":", 1)
        else:
            action_str = rest
            target = None
            
        return cls(
            type=h_type,
            action=KickAction(action_str),
            target=target
        )

    def to_string(self) -> str:
        base = f"⫻{self.type}/{self.action.value}"
        if self.target:
            base += f":{self.target}"
        else:
            base += ":"
        return base

class KickMessage(BaseModel):
    """
    A full KickLang message/block.
    """
    header: KickHeader
    content: Any 

    @field_validator('content')
    @classmethod
    def validate_content(cls, v: Any) -> Any:
        # Placeholder for stricter content validation based on header type
        return v

class Directive(KickMessage):
    """
    Operational commands (⫻cmd/).
    """
    pass

class Payload(KickMessage):
    """
    Information containers (⫻data/).
    """
    pass

class Query(KickMessage):
    """
    Requests for information (⫻query/).
    """
    pass
