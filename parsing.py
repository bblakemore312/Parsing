import re
from urllib.request import urlretrieve
from os import path
def main():
   
    FILE_NAME = 'local_copy.log'
    for log_line in open(FILE_NAME):
        # pattern = re.compile(".([0-9]{2})/([A-Za-z]{3})/([0-9]{4}):([0-9]{2}):([0-9]{2}):([0-9]{2}) -([0-9]{4})]")
        # parts = pattern.spilt(log_line)
        parts = re.split(".([0-9]{2})/([A-Za-z]{3})/([0-9]{4}):([0-9]{2}):([0-9]{2}):([0-9]{2}) -([0-9]{4})]", log_line)
        num_lines = 0
        for line in parts:
             num_lines += 1
        print("number of lines: ")
        print (num_lines)
        
if __name__ == "__main__":
  main()
