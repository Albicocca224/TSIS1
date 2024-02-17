import datetime
current=datetime.datetime.now()
diff=datetime.timedelta(days=5)
past=current-diff
print(past)