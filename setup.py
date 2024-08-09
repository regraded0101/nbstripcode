from setuptools import setup, find_packages

setup(
    name="nbstripcode",
    version="0.1.0",
    description="Remove all that pesky code, but keep those valuable outputs!",
    packages=find_packages(),
    entry_points={
        "console_scripts":[
            "nbstripcode=nbstripcode.main:main",
        ]
    },
    python_requires=">=3.11",
    author="regraded0101"
)

