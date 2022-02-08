import re
import csv
from collections import Counter
def reader(filename):
    with open(filename) as f:
        log=f.read()

        regexp=r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ips_list=re.findall(regexp,log)

        regexp=r'\d{1,2}\/\D{1,3}\/\d{1,4}'
        date_list=re.findall(regexp,log)

        regexp=r'\d[10]\:\d{1,2}\:\d{1,2}\s[+]0000'
        time_list=re.findall(regexp,log)

        regexp=r'GET.*1.1'
        get_list=re.findall(regexp,log)

        regexp=r'\b200'
        status_list=re.findall(regexp,log)

        regexp=r'\s\d{4,6}\s'
        size_list=re.findall(regexp,log)

        regexp=r'ht.*20..'
        http_list=re.findall(regexp,log)

        regexp=r'Mozilla..*\d{1,3}\.\d{1,2}'
        mozilla_list=re.findall(regexp,log)

        dict = {'IP ADDRESS':ips_list , 'DATE':date_list,'TIME':time_list,'REQUEST STATUS':status_list,'FILE SIZE':size_list,'REQUEST':get_list,'REQUEST URL':http_list,'WEB BROWSER URL':mozilla_list}
        print(dict)

    with open("myfile2.csv", 'w') as f:
            for key, value in dict.items():
                writer = csv.writer(f)
                writer.writerow(dict.keys())
                writer.writerows(zip(*dict.values()))
                break   

if __name__=='__main__':
    reader(filename='log.txt')
