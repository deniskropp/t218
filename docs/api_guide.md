# OCS Node: API Integration Guide

## Base URL
`http://localhost:8000`

## Endpoints

### 1. Check System Health
**GET** `/health`
- **Response**: `{"status": "online", "system": "OCS Node"}`

### 2. Get Workflow Definition
**GET** `/workflow`
- **Response**: JSON object containing the 20-step `TRANSFORMATION_WORKFLOW` array.

### 3. Execute Task
**POST** `/execute`
- **Query Param**: `objective` (string) - The high-level intent.
- **Example**:
  ```bash
  curl -X POST "http://localhost:8000/execute?objective=Build%20Login%20Page"
  ```
- **Response**:
  ```json
  {
    "status": "accepted",
    "objective": "Build Login Page",
    "message": "Task queued for processing [Mock]"
  }
  ```

## Integration with Agents
External agents should interface with the Node primarily via the `/execute` endpoint using strict KickLang strings in the `objective` field if complex directives are required.

Example of KickLang Injection:
```bash
curl -X POST "http://localhost:8000/execute?objective=⫻cmd/mode:Strict%20⫻data/obj:Refactor%20API"
```
