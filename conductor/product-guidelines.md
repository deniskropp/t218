# Product Guidelines: OCS Node

## General Principles
- **Transform by two generations**: Every transformation should significantly elevate the fidelity and utility of the input.
- **Protocol First**: All internal and external communications must adhere to KickLang.
- **Persona Integrity**: Agents must remain in character and fulfill their specific workflow responsibilities.

## Quality Standards
- **High Fidelity**: Execution artifacts must be production-ready and technically sound.
- **Clarity**: Purified TAS (`⫻data/ptas:`) must be unambiguous and actionable.
- **Traceability**: Every output must be traceable back to its original objective (`⫻data/obj:`).

## Development Practices
- **Modern Python**: Use FastAPI, Pydantic v2, and async/await.
- **Modern Style**: Follow TypeScript-like structure (Services, DTOs, DI).
- **Documentation**: Use `.kl` files for Knowledge Items.
