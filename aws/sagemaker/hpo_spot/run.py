#!/usr/bin/env python3

from sagemaker import Session
from sagemaker.tensorflow import TensorFlow
from sagemaker.tuner import CategoricalParameter, HyperparameterTuner


def main():
    session = Session()
    estimator = TensorFlow(
        sagemaker_session=session,
        role="AmazonSageMaker-ExecutionRole",
        source_dir="src",
        entry_point="train.py",
        framework_version="1.13",
        py_version="py3",
        hyperparameters=dict(epochs=100),
        train_instance_count=1,
        train_instance_type="ml.m5.large",
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

    tuner.fit()


if __name__ == "__main__":
    main()
