import re
from urllib.request import urlretrieve
from os import path
def main():
   
    FILE_NAME = 'local.log'

    count = 0
    with open(FILE_NAME, 'r') as f:
        for line in f:
            count += 1
    print ("Total Requests:", count)
    for log_line in open(FILE_NAME):
        ERRORS = []
        regex = re.compile("([A-Za-z]{5,6}) - - \[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) ([0-9]{0,6})")
        parts = regex.split(log_line)
        # print (parts)
        if not parts or len(parts) < 7:
        #   print ("Error added to log entry")
          ERRORS.append(log_line)
        count1 = 0
        for line in s:
            count1 += 1
        print ("The total requests are: ", count1)
if __name__ == "__main__":
  main()
