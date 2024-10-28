# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:34:37 2024

@author: Faris Mismar
"""

# Runs a benchmark between a GPU and a CPU using a 
# Matrix multiplication and inversion
# Clearly, the moment inversion is in the benchmark, GPUs win.

import os
import numpy as np
import tensorflow as tf
import time


os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"

# For Windows users
if os.name == 'nt':
    os.add_dll_directory("C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.6/bin")

print(tf.config.list_physical_devices('GPU'))

# The GPU ID to use, usually either "0" or "1" based on previous line.
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

seed = 47
np_random = np.random.RandomState(seed)

max_iter = 10000

a_real = tf.constant(np_random.random(1000))
a_imag = tf.constant(np_random.random(1000))

a = tf.complex(a_real, a_imag) 
a = tf.reshape(a, (-1, 10, 10))

a_n = a.numpy()

print('Using TensorFlow: ', end='')
start_time = time.time()
for _ in range(max_iter):
    a@tf.linalg.inv(a)
    
end_time = time.time()

print('{:.3f} mins.'.format((end_time - start_time) / 60.))

print('Using Numpy: ', end='')
start_time = time.time()

for _ in range(max_iter):
    a_n@np.linalg.inv(a_n)
	
end_time = time.time()
print('{:.3f} mins.'.format((end_time - start_time) / 60.))
