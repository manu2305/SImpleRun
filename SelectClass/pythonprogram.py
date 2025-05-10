flag=True
l=[0,0,0,0,1]
i=0
while flag:
    try:
      a=4/l[i]
      break
    except:
      print("exception")
      i+=1
