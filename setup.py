#!/usr/bin/env python3

try:
    from setuptools import setup, find_packages
    get_packages = find_packages
except ImportError:
    from distutils.core import setup
    get_packages = lambda: ['lolchamp']

setup(
    name='lolchamp',
    version=version,
    description='A CLI tool that provides optimal champion and matchup info for the game League of Legends.',
    author='Akhilesh Yarabarla',
    author_email='akhileshyarabarla@gmail.com',
    license='MIT',
    keywords=['lol', 'league', 'league of legends', 'champion', 'matchup', 'level', 'item', 'ability'],
    url='https://github.com/yarabarla/lolchamp',
    packages=get_packages(),
    package_data={},
    install_requires=[
        'requests-futures >= 0.9.5',
    ],
    entry_points={
        'console_scripts': [
            'lolchamp = lolchamp.__main__:main',
        ]
    },
)
