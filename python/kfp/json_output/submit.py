from google.cloud import aiplatform
from kfp.components import load_component_from_file
from kfp.v2 import compiler, dsl


@dsl.component
def echo(msg: str) -> str:
    return msg


@dsl.pipeline(name="generate-array-pipeline")
def pipeline(n: int):
    generate_json_array = load_component_from_file(
        "./components/generate_json_array.yaml"
    )
    generate_json_array_task = generate_json_array(n_sequences=n)
    with dsl.ParallelFor(generate_json_array_task.output) as item:
        echo(item)


compiler.Compiler().compile(
    pipeline_func=pipeline, package_path="./generate_array_pipeline.json"
)

aiplatform.PipelineJob(
    display_name="generate-array-pipeline",
    template_path="./generate_array_pipeline.json",
    pipeline_root="gs://speg03-bucket/pipeline_root/",
    parameter_values={"n": 5},
).submit()
