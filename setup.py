from setuptools import setup, find_packages

setup(
    name="HerSignal",
    version="1.0.0",
    author="Your Name",
    description="AI-Powered Women's Safety Agent",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "pyyaml>=6.0",
        "requests>=2.31.0",
        "google-generativeai>=0.3.0",
        "numpy>=1.24.3",
        "cryptography>=41.0.0",
    ],
)
