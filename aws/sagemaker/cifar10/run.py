#!/usr/bin/env python

import sagemaker
from sagemaker.tensorflow import TensorFlow

local_estimator = TensorFlow(
    role=sagemaker.get_execution_role(),
    source_dir='src',
    entry_point='train.py',
    train_instance_count=1,
    train_instance_type='local',
    framework_version='1.12.0',
    py_version='py3',
    hyperparameters=dict(limit_data_rate=0.01),
    script_mode=True)

local_estimator.fit('file://cifar10.npz')
