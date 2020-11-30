email = "ceng113@example.com"
semail = input("Enter your email: ")
semail = semail.lower()
ssemail = str()
list = []
list2 = []
for i in semail:
  if("." in i):
    continue
  else:
    ssemail.join(i)
for i in email:
  list2.append(i)
if(lis1 == list2):
  print(True)
else:
  print(False)
