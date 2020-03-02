import re
from urllib.request import urlretrieve
from os import path
import operator 
def main():
    URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    LOCAL_FILE = 'local.log'
    FILE_NAME = 'local.log'

    local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)
    #if file is in the directory do no run the commented out 
    count = 0
    with open(FILE_NAME, 'r') as f:
        for line in f:
            count += 1
    print ("Total Requests:", count)
    ####################################
    days = {}
    parts = {}
    requests = {}
    mal = {}
    
    for log_line in open(FILE_NAME):
      ERRORS = []
      regex = re.compile("([A-Za-z]{5,6}) - - \[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) ([0-9]{0,6})")
      parts = regex.split(log_line)
      # print(parts)
      if len(parts) == 10:
        x = parts[2]
        if days.get(x, -1) == -1:
          days[x] = 1
        else:
          days[x] += 1  
        y = parts[7]
        if requests.get(y, -1) == -1:
          requests[y] = 1
        else:
          requests[y] += 1
        z = parts[5]
        if mal.get(z, -1) == -1:
          mal[z] = 1
        else:
          mal[z] += 1
    for i, j in days.items():
      print("Requests per Day: ", i, j)
    ####################################
    counter = 0
    week = {}
    currentw = ''
    weeknum = 1
    for day,value in days.items():
      if counter == 0:
        currentw = "Week " + str(weeknum)
        week[currentw] = value
        counter += 1
      else:
        week[currentw] = value + week[currentw]
        counter += 1
      if counter == 7:
        counter = 0 
        weeknum += 1
    for day, value in week.items():
      print ("Requests per week: ", day, value)
    months = {}
    counter = 0
    spl = ''
    for a, b in days.items():
      spl = a.split('/')
      spl = spl[1]
      if months.get(spl, -1) == -1:
        months[spl] = b
      else:
        months[spl] += b
    for a,b in months.items():
      print("Requests per Month: ", a,b)
    l2 = max(mal.items(), key=operator.itemgetter(1))[0]
    l3 = min(mal.items(), key=operator.itemgetter(1))[0]
    #   if e in ["400","401","402","403","404"]:
    #       # print (e, k)
    #   if e in ["300", "301", "302", "303", "304", "305", "306"]:
        # print (e, k)
    print ("400 errors are ", count/(23583 + 4743 + 15 + 43), "Percent")
    print ("Request redirection was: ", count/(30295 + 97792), "Percent")
    print (l2)
    print (l3)
    
          
if __name__ == "__main__":
  main()
