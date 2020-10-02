import click

from werkzeug.serving import run_simple

from look import application


@click.command()
@click.option("--host", default="localhost", help="Host name or ip.")
@click.option("--port", default=8000, help="Port number.")
def run(host, port):
    run_simple(host, port, application, use_reloader=True)


if __name__ == "__main__":
    run()
