# Write a Python program to get height and the width of console window.

import os
size = os.get_terminal_size(0)
print(size)
