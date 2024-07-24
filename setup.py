from setuptools import setup, find_packages

setup(
    name='snakebox',
    version='0.1.0',
    author='Tristan Mahr',
    author_email='tristan.mahr@wisc.edu',
    description='A sandbox for Python experiments',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tjmahr/snakebox',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # Add your package dependencies here
    ],
)
