from setuptools import setup, find_packages

setup(
    name='DataProcessor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    author='Hinx Vietti',
    author_email='hinxvietti@gmail.com',
    description='A package for processing data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/HinxVietti/DataProcessor',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
