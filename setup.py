from setuptools import setup, find_packages

setup(
    name="wtc",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["pandas", "openpyxl"],
    entry_points={
        "console_scripts": [
            "wtc=wtc.main:main"
        ]
    },
    author="Anjan",
    description="JIRA to Worktop Excel Converter",
    python_requires=">=3.8",
)