from datetime import datetime

date=datetime.now()
s=str(date).replace(":","-")
print(s)