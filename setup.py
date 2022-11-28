from setuptools import setup, find_packages

setup(
    name='campuscomjsonparser',
    version='0.0.1',
    packages=find_packages(include=['campuscomjsonparser', 'campuscomjsonparser.*']),
    install_requires=[
        'asttokens==2.1.0',
        'backcall==0.2.0',
        'click==8.1.3',
        'commonmark==0.9.1',
        'decorator==5.1.1',
        'executing==1.2.0',
        'ipdb==0.13.9',
        'ipython==8.6.0',
        'jedi==0.18.2',
        'matplotlib-inline==0.1.6',
        'mysql-connector-python==8.0.31',
        'parso==0.8.3',
        'pexpect==4.8.0',
        'pickleshare==0.7.5',
        'prompt-toolkit==3.0.33',
        'protobuf==3.20.1',
        'ptyprocess==0.7.0',
        'pure-eval==0.2.2',
        'Pygments==2.13.0',
        'rich==12.6.0',
        'six==1.16.0',
        'stack-data==0.6.1',
        'toml==0.10.2',
        'traitlets==5.5.0',
        'wcwidth==0.2.5',
    ],

    entry_points={
        'console_scripts': ['parse=campuscomjsonparser.parser:main']
    }
)
