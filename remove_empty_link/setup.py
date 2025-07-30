from setuptools import setup, find_packages

setup(
    name="remove-empty-link-plugin",
    version="1.0",
    description="Entfernt leere 'link'-Felder vor dem Speichern eines Parts in InvenTree.",
    author="Meister",
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
)
