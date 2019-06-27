import argparse

from jinja2 import Environment, meta

template_str = 'hello, {{ message }}'

env = Environment()
ast = env.parse(template_str)
variables = meta.find_undeclared_variables(ast)
print('variables:', variables)

parser = argparse.ArgumentParser()
for v in variables:
    parser.add_argument('--' + v, required=True)
args = parser.parse_args()
print('args:', args)

template = env.from_string(template_str)
print(template.render(**vars(args)))
