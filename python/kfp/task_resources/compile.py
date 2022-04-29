from kfp.v2 import compiler, dsl
from kfp.v2.dsl import ContainerOp


@dsl.component(
    base_image="python:3.9-slim", output_component_file="./echo_component.yaml"
)
def echo(msg: str) -> str:
    return f"hello, {msg}"


@dsl.pipeline(name="echo-pipeline")
def echo_pipeline(msg: str = "world"):
    task: ContainerOp = echo(msg)
    task.container.set_cpu_limit("2")
    task.container.set_memory_limit("16G")
    task.container.set_gpu_limit("1")
    task.add_node_selector_constraint(
        "cloud.google.com/gke-accelerator", "NVIDIA_TESLA_T4"
    )
    task.container.set_env_variable("ECHO", "hello")
    task.set_display_name("Echo HELLO")
    task.set_caching_options(True)


def main():
    compiler.Compiler().compile(
        pipeline_func=echo_pipeline, package_path="./echo_pipeline.json"
    )


if __name__ == "__main__":
    main()
