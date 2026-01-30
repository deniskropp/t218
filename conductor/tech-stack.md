# Tech Stack: OCS Node

This document outlines the technologies and protocols that power the OCS Node: SF20 Transformation Engine.

## Core Components

### LLM Architecture
- **Primary Model**: `mistral:devstral-medium-latest`
- **Configuration**:
  - Temperature: 0.0
  - Max Input Tokens: 262,144

### Protocol: KickLang
The OCS Node operates using the **KickLang** protocol for all inter-agent communication and data processing.

- **Headers**:
  - `⫻cmd/`: Directives (Operational commands)
  - `⫻data/`: Payloads (Information transport)
  - `⫻query/`: Queries (Inter-agent clarification)
- **Specialized Payloads**:
  - `⫻data/rv:`: Research Vectors
  - `⫻data/draft:`: Written prose
  - `⫻data/cite:`: Citation data

### Operating Environment
- **Platform**: Linux
- **Development Language**: (Primarily Markdown and KickLang for orchestration)

## System Roles (Personas)
The transformation engine utilizes a specialized team of AI personas, including:
- **GPTASe**: TAS (Task Agnostic Steps) extractor.
- **puTASe**: TAS purifier.
- **Lyra**: Prompt Engineer and Workflow Structurer.
- **Fizz La Metta**: Cognitive Coordinator and System Monitor.
- **Codein**: Code Investigator.
- **AI Tutor**: Knowledge transfer.
- **Dima**: Ethical Compliance and Joint Decisions.
- **SystemMonitor**: Integrity Monitoring.
- **Orchestrator**: Dynamic Role Adaptation.
- **WePlan**: Strategic and Tailored Plans.
- **AR-00L**: Visual Assets.
- **Kick La Metta**: NL to Formal Translation.
- **QllickBuzz & QllickFizz**: Operational Rules.
