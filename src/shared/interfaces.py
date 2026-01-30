from abc import ABC, abstractmethod
from typing import Any

class FlowNotifier(ABC):
    """
    Abstract interface for notifying about flow progress.
    Allows SwarmEngine to be used with different outputs (WebSocket, CLI, etc.)
    """

    @abstractmethod
    async def step_started(self, step_id: int) -> None:
        """Called when a step starts executing"""
        pass

    @abstractmethod
    async def step_completed(self, step_id: int, result: Any) -> None:
        """Called when a step completes successfully"""
        pass

    @abstractmethod
    async def flow_completed(self, flow_id: str) -> None:
        """Called when the entire flow completes"""
        pass
