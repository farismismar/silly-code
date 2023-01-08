#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 08:50:18 2023

@author: farismismar
"""

import random
import string
import time

seed = 1

random.seed(seed)

alphabets = string.ascii_letters
punctuation = '.,;!?'

dictionary = alphabets + punctuation

target_string = 'Faris' #' B. Mismar lives in Texas.'
use_cheat_heuristic = True

number_of_monkeys = 0
current_string = ''

start_time = time.time()
while current_string != target_string:
    # Sample from dictionary
    current_char = random.sample(dictionary, 1)[0]
    
    # and append it to the current string
    current_string += current_char
    
    print(number_of_monkeys, current_string)
    
    # Cheat allowed: if the first char is not equal to the first target
    # purge and restart
    if use_cheat_heuristic:
        if len(current_string) == 1 and (current_char != target_string[0]):
            current_string = ''
            continue
    
    # purge the buffer and start afresh
    if len(current_string) > len(target_string):
        current_string = ''
        
    number_of_monkeys += 1   
end_time = time.time()
    
time_duration = (end_time - start_time)

print(f'One of {number_of_monkeys} monkeys was able to write this sentence at the first attempt: {target_string}.')
print('Total CPU time: {:.2f} mins.'.format(time_duration / 60.))


