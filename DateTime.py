from datetime import datetime


date_time_str = "09/18/22 15:50"

date_time = datetime.strptime(date_time_str, "%m/%d/%y %H:%M")

print(date_time)