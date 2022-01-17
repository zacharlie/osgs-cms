from setuptools import setup, find_packages

setup(
    name="osgs-sl",
    version="0.0.1",
    packages=find_packages(include=[".*"]),
    install_requires=["Flask-AppBuilder==3.4.3", "Pillow==9.0.0"],
    extras_require={
        "dev": ["black", "python-dotenv", "pytest"],
    },
    python_requires="~=3.10",
)
