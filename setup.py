from setuptools import setup, find_packages

setup(
    name="wtc-cli",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["pandas", "openpyxl"],
    entry_points={
        "console_scripts": [
            "wtc=wtc.main:main"
        ]
    },
    author="Anjani Kumar Chejarla",
    url="https://github.com/anjancoforge/wtc-cli",
    description="CLI tool to convert JIRA Excel into Worktop format",
)
