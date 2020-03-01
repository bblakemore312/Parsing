import re
from urllib.request import urlretrieve
from os import path
def main():
    URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    LOCAL_FILE = 'local_copy.log'
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
        print(parts)
        if not parts or len(parts) < 7:
          ERRORS.append(log_line)
if __name__ == "__main__":
  main()
      
