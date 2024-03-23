from setuptools import setup, find_packages

setup(
    name='konfiDict',
    version='0.1.2',
    packages=find_packages(),
    description='Eine dict mit besondern Fächkeiten',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Falk',
    url='https://github.com/quojus/konfiDict',
    python_requires='>=3.6',
    nstall_requires=[
        # Liste von erforderlichen Paketen
    ]
)