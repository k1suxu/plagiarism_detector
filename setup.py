from setuptools import setup, find_packages

setup(
    name="plagiarism_detection_system",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "strawberryfields==0.23.0",
        "tensorflow==2.9.1",
        "numpy==1.23.5",
        "scikit-learn==1.2.2",
        "aif360==0.5.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="Advanced plagiarism detection system using quantum computing, ethical AI, and blockchain",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/plagiarism-detection-system",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)