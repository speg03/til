import os
from sagemaker.local.local_session import LocalSession
from sagemaker.estimator import Estimator

role = 'AmazonSageMaker-ExecutionRole'

session = LocalSession()
session.config = {'local': {'local_code': True}}

estimator = Estimator(image_name='test:latest', role=role,
                       train_instance_count=1,
                       train_instance_type='local',
                       hyperparameters={
                         'a': {
                           'b': 1,
                           'c': 'hello'
                         }
                       },
                       sagemaker_session=session)

estimator.fit()
