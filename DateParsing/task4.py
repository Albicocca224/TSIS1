import datetime
date1=datetime.datetime(2024, 2, 15)
date2=datetime.datetime(2024, 1, 1)
diff=date1-date2
print(diff.total_seconds())