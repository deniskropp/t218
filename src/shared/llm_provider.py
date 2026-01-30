import os
import logging
from typing import Optional
from mistralai import Mistral
from dotenv import load_dotenv

# Load environment variables (e.g., from .env file)
load_dotenv()

logger = logging.getLogger(__name__)

class MistralProvider:
    def __init__(self):
        self.api_key = os.getenv("MISTRAL_API_KEY")
        self.client: Optional[Mistral] = None

        if self.api_key:
            try:
                self.client = Mistral(api_key=self.api_key)
                logger.info("MistralProvider initialized successfully.")
            except Exception as e:
                logger.error(f"Failed to initialize Mistral client: {e}")
        else:
            logger.warning("MISTRAL_API_KEY not found in environment. Falling back to simulation mode.")

    async def generate_response(self, prompt: str) -> str:
        """
        Generates a response using Mistral AI. 
        Falls back to a simulated response if the client is not initialized.
        """
        if not self.client:
            return f"[SIMULATION] Mistral key missing. Mock response for: {prompt[:30]}..."

        try:
            # Using mistral-tiny or similar fast model for efficiency
            response = await self.client.chat.complete_async(
                model="mistral-tiny",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            if response and response.choices:
                return response.choices[0].message.content
            return "[ERROR] Empty response from Mistral."
        except Exception as e:
            logger.error(f"Mistral generation error: {e}")
            return f"[ERROR] Failed to generate response: {e}"
