from setuptools import setup, find_packages

VERSION = '0.4.0'
DESCRIPTION = 'Assetto Corsa stubs library.'
LONG_DESCRIPTION = 'Assetto Corsa stubs library for "ac" object. Useful for autocompletion in IDE during development.'

# Setting up
setup(
    name='ac-stubs',
    version=VERSION,
    author='Kirby R',
    author_email='<andkirby@gmail.com>',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'AC', 'Assetto Corsa', 'dummy', 'stub'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Games/Entertainment :: Simulation',
    ]
)