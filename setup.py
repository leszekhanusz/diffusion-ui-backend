import os

from setuptools import find_packages, setup

install_requires = [
    "diffusers==0.3.0",
    "gradio>=3.1.6",
    "transformers>=4.21.3",
]

dev_requires = [
    "black==22.3.0",
    "check-manifest>=0.42,<1",
    "flake8==3.8.1",
    "isort==5.10.1",
]

console_scripts = [
    "diffusionui=diffusionui.cli:diffusionui_cli",
]

# Get version from __version__.py file
current_folder = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(
    os.path.join(current_folder, "src", "diffusionui", "__version__.py"), "r"
) as f:
    exec(f.read(), about)

setup(
    name="diffusionui",
    version=about["__version__"],
    description="Unified Stable Diffusion pipeline for diffusers",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/leszekhanusz/diffusion-ui-backend",
    author="Leszek Hanusz",
    author_email="leszek.hanusz@gmail.com",
    license="Apache",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="diffusers stable-diffusion",
    package_dir={"": "src"},
    packages=find_packages("src"),
    # PEP-561: https://www.python.org/dev/peps/pep-0561/
    package_data={"diffusionui": ["py.typed"]},
    install_requires=install_requires,
    extras_require={
        "dev": dev_requires,
    },
    include_package_data=True,
    python_requires=">=3.6.0",
    zip_safe=False,
    platforms="any",
    entry_points={"console_scripts": console_scripts},
)
