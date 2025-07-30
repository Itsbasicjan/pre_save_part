from setuptools import setup, find_packages

setup(
    name="pre-save-part-plugin",
    version="1.0",
    description="Entfernt leere link-Felder in InvenTree",
    author="Meister",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
