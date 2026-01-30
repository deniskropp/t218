import typer
from rich.console import Console
from rich.table import Table
from src.shared.workflow import SF20_WORKFLOW_STEPS

from src.shared.interfaces import FlowNotifier
from src.api.engine import SwarmEngine
import asyncio
from typing import Any

app = typer.Typer(help="OCS Node: SF20 Transformation Engine CLI")
console = Console()

class ConsoleNotifier(FlowNotifier):
    def __init__(self, console: Console):
        self.console = console

    async def step_started(self, step_id: int) -> None:
        step = next((s for s in SF20_WORKFLOW_STEPS if s.id == step_id), None)
        title = step.title if step else f"Step {step_id}"
        agent = step.agent if step else "System"
        self.console.print(f"[bold cyan]Running Step {step_id}:[/bold cyan] {title} [dim]({agent})[/dim]")

    async def step_completed(self, step_id: int, result: Any) -> None:
        self.console.print(f"   [green]✓ Completed[/green]")
        self.console.print(f"   [dim]{result}\n[/dim]\n") 

    async def flow_completed(self, flow_id: str) -> None:
        self.console.print(f"\n[bold green]Transformation Flow {flow_id} Completed successfully![/bold green]")

@app.command()
def status():
    """
    Check system status and list available workflow steps.
    """
    console.print("[bold green]OCS Node Online[/bold green]")
    
    table = Table(title="Transformation Workflow")
    table.add_column("Step", style="cyan")
    table.add_column("Agent", style="magenta")
    table.add_column("Output Type")
    
    for step in SF20_WORKFLOW_STEPS:
        table.add_row(
            str(step.id),
            step.agent,
            step.output_type
        )
        
    console.print(table)

@app.command()
def execute(objective: str):
    """
    Start a transformation task.
    """
    console.print(f"[bold blue]Starting Transformation:[/bold blue] {objective}")
    
    engine = SwarmEngine()
    
    # Create the flow
    flow = engine.create_flow(objective)
    console.print(f"Flow Created: [bold]{flow.flow_id}[/bold]\n")
    
    notifier = ConsoleNotifier(console)
    
    # Run the flow (async)
    asyncio.run(engine.run_flow(flow.flow_id, notifier))

if __name__ == "__main__":
    app()
