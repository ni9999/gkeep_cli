
from setuptools import setup, find_packages

setup(
    name="gkeep",
    description="python cli for google keep notes with added functionality",
    version="0.1",
    author="Nazmul Islam <nazmulislamzrn@yahoo.com>",
    packages=find_packages(),
    install_requires=[
        "click",
        "gpsoauth",
        "gkeepapi",
    ],
    entry_points={
        "console_scripts": [
            "gkeep = gkeep.main:main",
        ]
    },
)