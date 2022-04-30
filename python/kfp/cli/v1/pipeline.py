from kfp.v2 import dsl


@dsl.component
def echo(msg: str) -> str:
    return msg


@dsl.pipeline(name="echo-pipeline")
def pipeline(msg: str):
    echo(msg)
