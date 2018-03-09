# In this script I create a test directory, and inside it is a file.
# In the test file, I record some data.
# Next, I rename the test directory and the file.
# After I copy the file.
# Finally I delete the created directory and all the files inside.

import os
from os import path

current_directory = path.realpath(path.curdir)

os.mkdir(current_directory + os.sep + "test_directory")
os.rmdir(current_directory + os.sep + "test_directory")