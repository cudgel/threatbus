from setuptools import setup
import pathlib

plugin_dir = pathlib.Path(__file__).parent.absolute()

with open(f"{plugin_dir}/README.md", "r") as fh:
    long_description = fh.read()

setup(
    author="Tenzir",
    author_email="engineering@tenzir.com",
    classifiers=[
        # https://pypi.org/classifiers/
        "Development Status :: 3 - Alpha",
        "Environment :: Plugins",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
        "Topic :: Security",
        "Topic :: Software Development :: Object Brokering",
        "Topic :: System :: Distributed Computing",
    ],
    description="A plugin to connect apps via ZeroMQ.",
    entry_points={"threatbus.app": ["zmq-app = threatbus_zmq_app.plugin"]},
    install_requires=[
        "threatbus>=2020.09.30",
        "pyzmq>=19",
        "python-dateutil>=2.8.1",
    ],
    keywords=[
        "threatbus",
        "threat intelligence",
        "plugin",
        "zeromq",
        "zmq",
    ],
    license="BSD 3-clause",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="threatbus-zmq-app",
    package_dir={"": "plugins/apps"},
    packages=["threatbus_zmq_app"],
    python_requires=">=3.7",
    url="https://github.com/tenzir/threatbus",
    version="2020.09.30",
)