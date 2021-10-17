from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

packages = [
    'menu'
]

setup(
    name="menu.py",
    version="0.1.2",
    author="deadyeti",
    author_email="deadyeti@deadyeti.ca",
    description="A simple in-terminal menu solution for Windows",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/readyyeti/menu.py",
    project_urls={
        "Bug Tracker": "https://github.com/readyyeti/menu.py/issues",
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
