import time
from datetime import datetime as dt
host_path = "/etc/hosts"
# host_path = "hosts"
redirect = "127.0.0.1"
website_list = ['facebook.com',
                "www.facebook.com",
                "www.espn.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23):
        with open(host_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' '+ website + '\n')
    else:
        with open(host_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            file.truncate()
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                else:
                    pass
    time.sleep(5)
