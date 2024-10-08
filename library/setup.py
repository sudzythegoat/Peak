from setuptools import setup, find_packages

setup(
    name='Peak',
    version='0.1',
    author='Sudzy',
    description='A Python library for modifying memory values',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sudzythegoat/Peak',
    packages=find_packages(),
    install_requires=[
        'pymem',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
