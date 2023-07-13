from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in cloud_automation/__init__.py
from cloud_automation import __version__ as version

setup(
	name="cloud_automation",
	version=version,
	description="An application that automate cloud processes",
	author="Douglas Ejiroghene Dominic",
	author_email="ejise45@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
