books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}
for i in books:
  count = 0
  for j in range(len(i)-1):
    if i[j] != i[j+1]:
      count += 1
  book_dict[i] = "{0},{1}".format(len(i),count)
#print(book_dict)

for i in book_dict.keys():
  i.split(",")
  a = (float(i[0]) + float(i[1]))/2
  tuple = [f"i,{a}"]
  for i in range(len(book_dict)):
    book_dict[i] = a
print(book_dict)
