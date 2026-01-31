"""
KickLang Parser
Parses KickLang messages into structured Directives and Payloads.
"""
from typing import Optional, Dict, Any
from src.shared.models import KickLangDirective, KickLangPayload, MessageType

class KickLangParser:
    """Parses raw text strings into KickLang objects."""

    @staticmethod
    def parse_line(line: str) -> Optional[Dict[str, Any]]:
        """
        Parses a single line of KickLang.
        Format: ⫻[type]/[subtype]: [content]
        Example: ⫻cmd/exec: Start task
        """
        line = line.strip()
        if not line.startswith('⫻'):
            return None

        # Split into (header, content) at the first colon
        if ': ' in line:
            header_part, content = line.split(': ', 1)
        elif line.endswith(':'):
            header_part = line.rstrip(':')
            content = ""
        else:
            # Malformed or simplified format? Assume header only
            header_part = line
            content = ""

        # Remove the leading ⫻
        header_part = header_part[1:]

        # Split header into type/subtype
        if '/' in header_part:
            msg_type_str, subtype = header_part.split('/', 1)
        else:
            msg_type_str = header_part
            subtype = "unknown"

        # Map string type to Enum
        try:
            msg_type = MessageType(msg_type_str)
        except ValueError:
            # Handle unknown types gracefully, or map to 'data' by default?
            # For now, let's treat unknown as data if it's not strictly recognized
            # Or return raw info. Let's return a dict for further processing.
            msg_type = msg_type_str

        return {
            "type": msg_type,
            "subtype": subtype,
            "content": content
        }

    @staticmethod
    def parse_directive(line: str) -> Optional[KickLangDirective]:
        data = KickLangParser.parse_line(line)
        if not data:
            return None
        
        # We expect a directive
        if data['type'] == MessageType.CMD or (isinstance(data['type'], str) and data['type'] == 'cmd'):
             return KickLangDirective(
                command=data['subtype'],
                parameters={"raw": data['content']} 
            )
        return None

    @staticmethod
    def parse_payload(line: str) -> Optional[KickLangPayload]:
        data = KickLangParser.parse_line(line)
        if not data:
            return None
        
        if data['type'] == MessageType.DATA or (isinstance(data['type'], str) and data['type'] == 'data'):
            return KickLangPayload(
                key=data['subtype'],
                value=data['content']
            )
        return None
