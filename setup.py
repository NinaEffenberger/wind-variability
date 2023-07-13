from setuptools import setup, find_packages

setup(
    packages=find_packages(
        include=["windspeed-variability", "windspeed-variability.*"]
    ),
)
