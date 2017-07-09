"""Create a Python distribution package setup.py."""
from setuptools import setup


extra_packages = {
    'testing': ['pytest-watch', 'pytest-cov']
}


setup(
    name="Data Structs",
    description="Contains Python data structure and algorithm implementations",
    version=0.1,
    author="Kurt Maurer" "James Feore",
    author_email="",
    license="MIT",
    py_modules=[],
    package_dir={'': 'src'},
    install_requires=["ipython", "pytest"],
    extras_require=extra_packages,
    entry_points={
        'console_scripts': [
        ]
    }
)
