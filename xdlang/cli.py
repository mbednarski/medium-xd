from pathlib import Path

import rich
import typer
from lark.tree import pydot__tree_to_png

from xdlang.pipeline.parser import Parser
from xdlang.pipeline.ast_builder import AstBuilder

app = typer.Typer()


@app.command()
def build():
    pass


@app.command(help="Compiles and runs an xd program with a lot of debug info.")
def run(input_file: Path):
    print("XD Compiler")
    print(f"Compiling and running {input_file}")

    parser = Parser()
    with input_file.open("rt") as f:
        tree = parser.parse_text(f.read())
    rich.print(tree)

    pydot__tree_to_png(tree, str(input_file.with_suffix(".png")), rankdir="TB")

    transformed = AstBuilder().transform(tree)
    rich.print(transformed)


def main():
    app()


if __name__ == "__main__":
    app()
