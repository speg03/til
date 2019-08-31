#!/usr/bin/env python3

import os

from sagemaker import Session
from sagemaker.tensorflow import TensorFlow
from sagemaker.tuner import CategoricalParameter, HyperparameterTuner
from sagemaker.utils import name_from_base


def main():
    job_name = name_from_base("tf-training", short=True)

    session = Session()
    estimator = TensorFlow(
        sagemaker_session=session,
        role="AmazonSageMaker-ExecutionRole",
        source_dir="src",
        entry_point="train.py",
        framework_version="1.13",
        py_version="py3",
        hyperparameters=dict(epochs=100, checkpoint_dir="/opt/ml/checkpoints"),
        train_instance_count=1,
        train_instance_type="ml.m5.large",
        train_use_spot_instances=True,
        train_max_wait=int(24 * 60 * 60 * 1.2),
        checkpoint_s3_uri=os.path.join(
            "s3://", session.default_bucket(), job_name, "checkpoints"
        ),
    )

    tuner = HyperparameterTuner(
        estimator=estimator,
        metric_definitions=[
            dict(Name="loss", Regex=r"- loss: (\S+)"),
            dict(Name="acc", Regex=r"- acc: (\S+)"),
        ],
        objective_metric_name="loss",
        objective_type="Minimize",
        hyperparameter_ranges=dict(
            batch_size=CategoricalParameter([32, 64]),
            learning_rate=CategoricalParameter([1e-4, 1e-3, 1e-2, 1e-1]),
        ),
        max_jobs=3,
        max_parallel_jobs=1,
    )

    tuner.fit(job_name=job_name)


if __name__ == "__main__":
    main()
