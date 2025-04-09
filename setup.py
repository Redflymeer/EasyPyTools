from setuptools import setup, find_packages

setup(
    name="easypython",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "beautifulsoup4>=4.9.3",
        "aiogram>=2.23.1",
        "tqdm>=4.60.0",
        "PySide6>=6.4.0"
    ],
    python_requires=">=3.8",
)