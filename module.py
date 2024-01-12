import datetime
import time

now = datetime.datetime.now().isoformat()[20:]
login = 'Login' + now
print(login)
time.sleep(2)
print(login)