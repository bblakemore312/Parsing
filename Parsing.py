import re
from urllib.request import urlretrieve
from os import path
def main():
   
    FILE_NAME = 'local.log'
    for log_line in open(FILE_NAME):
        # pattern = re.compile(".([0-9]{2})/([A-Za-z]{3})/([0-9]{4}):([0-9]{2}):([0-9]{2}):([0-9]{2}) -([0-9]{4})]")
        # parts = pattern.spilt(log_line)
        # parts = re.compile(r".([0-9]{2})/([A-Za-z]{3})/([0-9]{4}):([0-9]{2}):([0-9]{2}):([0-9]{2}) -([0-9]{4})]", log_line)
        # print(parts)
        ERRORS = []
        regex = re.compile("([A-Za-z]{5,6}) - - \[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) ([0-9]{0,6})")
        parts = regex.split(log_line)
        print (parts)
        if not parts or len(parts) < 7:
          print ("Error added to log entry")
          ERRORS.append(log_line)

if __name__ == "__main__":
  main()
