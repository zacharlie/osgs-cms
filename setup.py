from setuptools import setup, find_packages

setup (
    name='osgs-sl',
    version='0.0.1',
    packages=find_packages(include=['osgs-sl', 'osgs-sl.*']),
    install_requires=[
        'Flask-AppBuilder==3.4.3',
        'Pillow==9.0.0'
    ],
    extras_require={
        'development': ['black'],
    },
    python_requires="~=3.10"
)
