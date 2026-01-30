import typer
from rich.console import Console
from rich.table import Table
from src.shared.workflow import SF20_WORKFLOW_STEPS

app = typer.Typer(help="OCS Node: SF20 Transformation Engine CLI")
console = Console()

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
    Start a transformation task (Mock).
    """
    console.print(f"[bold blue]Starting Transformation:[/bold blue] {objective}")
    console.print("[yellow]Not implemented in this bootstrap version.[/yellow]")

if __name__ == "__main__":
    app()
