y = int(input())
y= y % (1440*60)
hours = (y// 3600)
y = y % 3600
minutes = (y // 60)
y = y % 60
seconds = (y)

print ("{}:{:02d}:{:02d}".format(hours, minutes, seconds))