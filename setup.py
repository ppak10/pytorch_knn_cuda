# https://gist.github.com/tonyseek/7821993
import glob
import torch
from os import path as osp
#from torch.utils.ffi import create_extension

from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension

abs_path = osp.dirname(osp.realpath(__file__))
extra_objects = [osp.join(abs_path, 'build/knn_cuda_kernel.so')]
extra_objects += glob.glob('/usr/local/cuda/lib64/*.a')

#ffi = create_extension(
#    'knn_pytorch',
#    headers=['src/knn_pytorch.h'],
#    sources=['src/knn_pytorch.c'],
#    define_macros=[('WITH_CUDA', None)],
#    relative_to=__file__,
#    with_cuda=True,
#    extra_objects=extra_objects,
#    include_dirs=[osp.join(abs_path, 'include')]
#)

setup(
    name="knn_pytorch",
    ext_modules=[
        CppExtension(
            name="knn_pytorch",
            sources=["src/knn_pytorch.c"],
            define_macros=[("WITH_CUDA", None)],
            with_cuda=True,
            extra_objects=extra_objects,
        )
    ],
    cmdclass={
        "build_ext": BuildExtension
    })
    


if __name__ == '__main__':
    assert torch.cuda.is_available(), 'Please install CUDA for GPU support.'
    # ffi.build()
