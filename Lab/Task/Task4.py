from datetime import datetime

now = datetime.now()
print(now)

formatted_date = now.strftime("%a %b %d %H:%M:%S IST %Y")
print(formatted_date)
