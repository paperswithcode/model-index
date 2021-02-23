from setuptools import setup, find_packages
from modelindex import __version__

name = "model-index"
author = "Robert Stojnic"
author_email = "hello@paperswithcode.com"
url = "https://github.com/paperswithcode/model-index"


setup(
    name=name,
    version=__version__,
    author=author,
    author_email=author_email,
    maintainer=author,
    maintainer_email=author_email,
    description="Create a source of truth for ML model results and browse it on Papers with Code",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url=url,
    platforms=["Windows", "POSIX", "MacOSX"],
    license="MIT",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points="""
        [console_scripts]
        mi=modelindex.__main__:cli
    """,
)
