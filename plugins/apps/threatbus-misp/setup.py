from setuptools import setup

setup(
    name="threatbus-misp",
    install_requires=["threatbus", "pymisp", "pyzmq"],
    entry_points={"threatbus.app": ["misp = threatbus_misp"]},
    py_modules=["threatbus_misp"],
)
