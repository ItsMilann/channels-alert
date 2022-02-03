from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.1.1"
DESCRIPTION = "Notification/Alert for django users"
LONG_DESCRIPTION = (
    "A package that allows to build simple async alert system using websocket."
)

# Setting up
setup(
    name="ibalert",
    version=VERSION,
    author="Ideabreed Technology (Milann Malla)",
    author_email="<hello@itsmilann.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["channels", "channels-redis", "coloredlogs"],
    keywords=["python", "websocket", "channels", "python-alerts", "ideabreed"],
    project_urls={
        "channels-alert": "https://github.com/ItsMilann/channels-alert/tree/release",
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
