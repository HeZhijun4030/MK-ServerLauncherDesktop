from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        "algorithms",
        sources=["algorithms.pyx"],
        extra_compile_args=["-O3"],
    )
]
setup(
    ext_modules=cythonize(extensions),
)