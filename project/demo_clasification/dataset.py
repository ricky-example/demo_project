from pathlib import Path
import pandas as pd
from loguru import logger
import typer

from demo_clasification.config import RAW_DATA_DIR

app = typer.Typer()

@app.command()
def main(
    output_path: Path = RAW_DATA_DIR / "dataset.csv",
):
    logger.info("Creating toy dataset...")

    # Create a small toy dataset
    data = {
        "id": [1, 2, 3, 4, 5],
        "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
        "age": [25, 30, 22, 35, 28],
        "score": [85.5, 90.0, 78.0, 88.5, 92.3],
    }

    df = pd.DataFrame(data)

    # Ensure RAW_DATA_DIR exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Save to CSV
    df.to_csv(output_path, index=False)

    logger.success(f"Dataset saved to {output_path}")

if __name__ == "__main__":
    app()
