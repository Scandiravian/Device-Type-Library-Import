from setuptools import setup

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='netbox-importer',
    packages=['netbox_importer'],
    version='0.1.0',
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'netbox_importer = netbox_importer:main',
        ]
    },
)
