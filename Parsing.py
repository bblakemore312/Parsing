import re
from urllib.request import urlretrieve
from os import path
def main():
    # URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    # LOCAL_FILE = 'local.log'
    FILE_NAME = 'local.log'

    # local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)
    #if file is in the directory do no run the commented out 
    # count = 0
    # with open(FILE_NAME, 'r') as f:
    #     for line in f:
    #         count += 1
    # print ("Total Requests:", count)
    ####################################
    days = {}
    parts = {}
    
    for log_line in open(FILE_NAME):
      ERRORS = []
      regex = re.compile("([A-Za-z]{5,6}) - - \[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) ([0-9]{0,6})")
      parts = regex.split(log_line)
      print(parts)
      if len(parts) == 10:
        x = parts[2]
        if days.get(x, -1) == -1:
          days[x] = 1
        else:
          days[x] += 1  
    # for i, j in days.items():
    #   print(i, j)
    ####################################
    counter = 0
    week = {}
    currentw = ''
    weeknum = 1
    for day,value in days.items():
      if counter == 0:
        currentw = "week" +str(weeknum)
        week[currentw] = value
        counter += 1
      else:
        week[currentw] = value + week[currentw]
        counter += 1
      if counter == 7:
        counter = 0 
        weeknum += 1
    # print ("requests per week")
    for day, value in week.items():
      print (day, value)
    months = {}
    counter = 0
    currentm = ''
    spl = ''
    for a, b in days.items():
      spl = a.split('/')
      spl = spl[1]
      if months.get(spl, -1) == -1:
        months[spl] = b
      else:
        months[spl] += b
    for a,b in months.items():
      print(a,b)
    error = {}
    counter = 0
    

    
       


        
      
if __name__ == "__main__":
  main()
      
