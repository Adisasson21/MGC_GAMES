import os
import time
import platform


SCORES_FILE_NAME = open("score.txt", "w+")
BAD_RETURN_CODE = True


def Screen_cleaner():
    if (platform.system().lower() == "windows"):
        cmdtorun = 'cls'
    else:
        cmdtorun = 'clear'
    print("Screen Cleared, starting a new game . . .")
    time.sleep(2)



