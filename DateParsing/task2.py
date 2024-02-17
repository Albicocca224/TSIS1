import datetime
current=datetime.datetime.now()
diff=datetime.timedelta(days=1)
yestDate=current-diff
tomDate=current+diff
print(yestDate.strftime("%d.%m.%Y"), current.strftime("%d.%m.%Y"), tomDate.strftime("%d.%m.%Y"))