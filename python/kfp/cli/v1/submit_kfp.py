import argparse

import kfp


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("package_path")
    args = parser.parse_args()

    client = kfp.Client(host="http://localhost:8080")
    client.create_run_from_pipeline_package(
        pipeline_file=args.package_path, arguments={"no_default_param": 5}
    )


if __name__ == "__main__":
    main()
