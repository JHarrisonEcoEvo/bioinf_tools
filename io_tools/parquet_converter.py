# Convert a parquet file into a csv file
import click
import pandas as pd

def parquet_converter(input: str) -> None:
    """Convert a parquet file into a csv file."""
    df = pd.read_parquet(input)

    # Remove parquet extension from input if it exists.
    if input.endswith('.parquet'):
        input = input[:-8]

    df.to_csv(f'{input}.csv')

@click.command()
@click.option("-input", "-i", help="Input parquet")
def main(input: str) -> None:
    """Call functions in this program."""
    parquet_converter(input)


if __name__ == "__main__":
    main()
