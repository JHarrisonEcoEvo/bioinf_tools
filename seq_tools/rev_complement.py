#!/usr/bin/env python3
# A function that takes an input DNA string and returns its reverse complement.
# See the click decorator on main() for usage instructions.

import click


def rev_complement(s: str) -> str:
    """Reverse complement a DNA string."""
    # This function will break if characters other than A, C, G, or T are within the input string.

    # First, convert to upper case and check for unexpected characters.
    # Again, we may not want to do this case conversion, but instead catch it
    # and warn the user. But, for now, I will leave this here.
    s = s.upper()
    for i in s:
        if i not in 'ACGT':
            raise ValueError('Unexpected character in input string. Is this a DNA string?')

    # Reverse the string.
    # NOTE: If just a reversed string was desired, then this could be passed to the output.
    s_rev = s[::-1]

    # Complement the string.
    s_rev_comp = ''

    # NOTE: if the complement of the non-reversed string was desired then I would probably make this a function
    # (defined elsewhere) and add a conditional statement here that would call the function
    # on either the reversed or non-reversed string depending on the desired output.
    for i in s_rev:
        if i == 'A':
            s_rev_comp += 'T'
        elif i == 'C':
            s_rev_comp += 'G'
        elif i == 'G':
            s_rev_comp += 'C'
        elif i == 'T':
            s_rev_comp += 'A'

    return s_rev_comp


@click.command()
@click.option("-input", "-i", help="Input DNA string")
def main(input: str) -> None:
    """Call functions in this program."""
    print(rev_complement(input))


if __name__ == "__main__":
    main()
