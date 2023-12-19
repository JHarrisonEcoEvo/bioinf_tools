# Compare two genomes of equal length. Useful for short genomes.

import click


@click.command()
@click.option("-i_1", help="input path to first genome", required=True)
@click.option("-i_2", help="input path to first genome", required=True)
def compare_genomes(**kwargs):
    # read in the genomes.
    # This assumes no header...  should add a check for that and remove if
    # ever used this for real.
    with open(kwargs["i_1"], "r") as g1:
        string = g1.read()

    with open(kwargs["i_2"], "r") as g2:
        string2 = g2.read()

    string = ''.join(string.splitlines())
    string2 = ''.join(string2.splitlines())

    # compare the genomes like a boss (or caveman?)
    if string == string2:
        print("The genomes are the same")
    else:
        print("The genomes are different")
        # Try to print out the number of letters that differ between the two strings.
        # This will only work if genomes are same length.
        for i in range(len(string)):
            if string[i] != string2[i]:
                print("The genomes differ at position: {}".format(i))

    print(f"The length of genome one is {len(string)}")
    print(f"The length of genome two is {len(string2)}")


if __name__ == "__main__":
    compare_genomes()

