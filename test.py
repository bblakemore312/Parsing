import re
from urllib.request import urlretrieve
from os import path
from collections import Counter
from datetime import datetime
def main():
   
    FILE_NAME = 'local.log'
    count = 0
    things = {}
    with open(FILE_NAME, 'r') as f:
        for line in f:
            count += 1
    print ("Total Requests:", count)
    for log_line in open(FILE_NAME):
        ERRORS = []
        parts = re.split("([A-Za-z]{5,6}) - - \[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) ([0-9]{0,6})", log_line)
        if not parts or len(parts) < 7:
          ERRORS.append(log_line)
    count1 = 0
    if parts[2] == parts[2]:
        count1 += 1
    print (count1)
if __name__ == "__main__":
  main()
