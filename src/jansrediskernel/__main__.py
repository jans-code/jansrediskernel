#!/usr/bin/env python
from ipykernel.kernelapp import IPKernelApp
from .kernel import jansrediskernel
IPKernelApp.launch_instance(kernel_class=jansrediskernel)
