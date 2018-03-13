# Python ZIP file

import os
import shutil


def main():
    full_current_path = os.path.realpath(os.path.curdir)
    shutil.make_archive("test_archive", "zip", full_current_path)

if __name__ == "__main__":
    main()
