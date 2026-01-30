# OCS Node: Technical Architecture

## Overview
The OCS Node uses a **Python Monorepo** structure designed for high-performance AI agent orchestration. It adheres strictly to the **KickLang** protocol.

## Directory Structure
- `src/api`: FastAPI application entry points.
- `src/cli`: Command-line interface tools.
- `src/shared`: Shared libraries, protocols, and workflow definitions.
- `tasks/`: Active Task Agnostic Steps (TAS) and definitions.
- `docs/`: Knowledge base and protocol specifications.

## Core Components

### 1. Protocol Layer (`src/shared/protocol.py`)
Defines the Pydantic models for KickLang:
- **Directives (`⫻cmd/`)**: `KickAction.EXEC`, `HALT`, `MODE`.
- **Payloads (`⫻data/`)**: `KickAction.OBJ`, `TAS`, `PTAS`.
- **Logic**: Conditional flow control (`IF`, `ELSE`, `LOOP`).

### 2. Workflow Engine (`src/shared/workflow.py`)
Implements the **20-step Transformation Cycle**.
- **Steps**: Hardcoded sequence of 20 steps.
- **Agents**: Maps each step to a specific persona (e.g., GPTASe, Lyra).
- **Data Flow**: Defines Strict Input/Output types for each step (e.g., `⫻data/obj:` -> `⫻data/tas:`).

### 3. API Layer (`src/api/main.py`)
Exposes the engine via HTTP.
- `GET /workflow`: Returns the definition.
- `POST /execute`: Triggers a task (Mock implementation).

## Data Flow
1.  **Input**: User sends `⫻data/obj:` via CLI or API.
2.  **Processing**: The Orchestrator (to be implemented) moves the object through the 20-step chain using `src/shared/workflow.py`.
3.  **Output**: Final artifacts are written to `output/` or returned as `⫻data/ptas:`.
