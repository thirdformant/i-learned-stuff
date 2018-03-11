import click

@click.command()
@click.argument("message")
@click.option("--tags", "-t", multiple=True, help="Optional tags")

def main(message, tags):
    # click.echo("Message: {0}\nTags: {1}".format(message, tags))

if __name__ == "__main__":
    main()
