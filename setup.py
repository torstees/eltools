from setuptools import setup

setup(name='eltools',
    version='0.1',
    description='Tools built to support needs of Edwards Lab',
    url='https://github.com/torstees/eltools',
    author='Eric Torstenson',
    author_email='eric.s.torstenson@vumc.org',
    packages=['elab'],
    entry_points={
        'console_scripts': [
            'mxcovar = elab.tools.mxcovar:main'
        ]}
)
