#!/usr/bin/env python3
# Count the number of times each DNA nucleotide (A, C, G, T) appears in a string.
# See the click decorator on main() for usage instructions.

import click
import warnings


def nucleotide_counter(s: str) -> list:
    """Counts the number of times each DNA nucleotide (A, C, G, T) appears in a string."""
    if not isinstance(s, str):
        raise TypeError('Input must be a string.')

    # Convert string to uppercase. Just in case. (pun)
    # Note, that, maybe, we wouldn't want to do this but instead catch such cases and warn the user.
    # For now, though, let's make sure we are using all caps.
    s = s.upper()

    # Catch instances where a non-expected character is present.
    for i in s:
        if i not in 'ACGT':
            warnings.warn('WARNING: There is an unexpected character present in the input string.')

    return [s.count('A'), s.count('C'), s.count('G'), s.count('T')]

@click.command()
@click.option("-input", "-i", help="Input DNA string")
def main(input: str) -> None:
    """Call functions in this program."""
    print(nucleotide_counter(input)) #print to STDOUT


if __name__ == "__main__":
    main()
