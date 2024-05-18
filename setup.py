from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='alice-connector',
    version='0.0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A SQL connector developed by alice',
    long_description=open('README.txt').read(),
    install_requires=requirements,
    url='',
    author='Thinh Do Duc',
    author_email='dothinh.dev@gmail.com'
)