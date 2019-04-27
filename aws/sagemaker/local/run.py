import os
from sagemaker.local.local_session import LocalSession
from sagemaker.tensorflow import TensorFlow

role = 'AmazonSageMaker-ExecutionRole'

session = LocalSession()
session.config = {'local': {'local_code': True}}

current_dir = os.path.abspath(os.path.curdir)
estimator = TensorFlow(role=role,
                       source_dir=f'{current_dir}/src',
                       entry_point='entrypoint.py',
                       train_instance_count=1,
                       train_instance_type='local',
                       framework_version='1.12',
                       py_version='py3',
                       sagemaker_session=session)

estimator.fit()
