from setuptools import setup, find_packages

setup(
    name='konfiDict',
    version='0.1.2',
    packages=find_packages(),
    description='Eine dict mit besonderen Fähigkeiten',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Falk',
    url='https://github.com/quojus/konfiDict',
    python_requires='>=3.6',

)