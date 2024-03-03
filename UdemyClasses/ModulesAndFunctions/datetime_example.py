import datetime as dt
from datetime import datetime

# today = dt.datetime.today() # It is preffered that you don't use the today method but instead use now.  # nqa
now = datetime.now()
utc_now = datetime.utcnow()

# print(today) # It is preffered that you don't use the today method but instead use now.  # nqa
print(now)
print(utc_now)
