from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

packages = [
    'yetimenu'
]

setup(
    name="yetimenu",
    version="0.0.16",
    author="deadyeti",
    author_email="deadyeti@deadyeti.ca",
    description="A simple in-terminal menu solution for managin user-input",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    packages=packages,
    classifiers=[
        "Natural Language :: English",
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ]
)
