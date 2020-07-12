import os
import time
import sys

def main():
    # if sys.argv[1] =="manual":
    #     run_arg = "manual":
    # if sys.argv[1] =="automatic":
    #     run_arg = "manual":
    time.sleep(10)
    os.system("git pull")
    time.sleep(60)
    os.system("python3 run_quetta.py")

if __name__ == "__main__":
    main()
