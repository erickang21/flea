from setuptools import setup

setup(
    name="flea",
    version="1.1.1",
    py_modules=["flea"],
    install_requires=["Click"],
    entry_points='''
        [console_scripts]
        flea=flea:flea
    ''',
)