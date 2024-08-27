import logparser

import ipgeolocation

for logline in open('apache_logs','r'):

    logdetails = logparser.parser(logline)

    host = logdetails['host']
    
    if host not in ipcounter:
        
        ipcounter[host] =1
        
    else:

        ipcounter[host] +=1

for ip in ipcounter:
    
    freq = ipcounter[ip]
    
    if freq > 100:
        r = get_country(ip=ip,api_key='7be76590669b4a18a684bc978d6e4cae')
        print(f'{ip:20} - {freq:6} - [{r}]')
