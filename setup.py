from setuptools import setup, Extension, find_packages

setup(
    name="hugetsu",
    packages=find_packages(where="hugetsu"),
    package_dir={"":"hugetsu"}
)