import sqlite3
import pytz
import pickle


db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

#for row in db.execute ("SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime," "             # noqa: E501
#                       history.account, history.amount FROM history ORDER BY history.time"):  # noqa: E501
for row in db.execute("SELECT * FROM history"):
    utc_time = row[0]
    # picked_zone = row[3]
    # zone = pickle.loads(picked_zone)
    zone = pytz.timezone("Australia/Adelaide")
    local_time = pytz.utc.localize(utc_time).astimezone(zone)
    print("{}\t{}\t{}".format(utc_time, local_time, local_time.tzinfo))

db.close()
