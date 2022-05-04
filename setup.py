from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='TobiiClient',
    version='0.0.1',
    description='Stream Tobii tracker data',
    long_description=readme,
    author='Noah Jennings',
    author_email='njenn001@odu.edu',
    url='https://github.com/njenn001/tobiiClient',
    license=license,
    packages=['app',], 
    install_requires = [
        'kafka-python',
    ]
)