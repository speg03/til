import argparse
import os

from google.cloud import aiplatform


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("package_path")
    args = parser.parse_args()

    aiplatform.PipelineJob(
        display_name=os.path.basename(args.package_path),
        template_path=args.package_path,
        pipeline_root="gs://speg03-bucket/pipeline_root/",
        parameter_values={"no_default_param": 5},
    ).submit()


if __name__ == "__main__":
    main()
