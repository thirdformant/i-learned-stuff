import click
import datetime

from .i_learned_stuff import LearnObject

@click.command()
@click.argument("message")
@click.option("--tags", "-t", multiple=True, help="Optional tags")

def main(message, tags):
    click.echo("Message: {0}\nTags: {1}".format(message, tags))
    # Create learn object from cli parameters
    logtime = datetime.datetime.now()
    learn_object = LearnObject(logtime, message, tags)
    learn_object.write_learnobject(logtime)


if __name__ == "__main__":
    main()
