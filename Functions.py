# create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency by using dictionaries.


def most_frequent(string):
  d = {}
  for i in string:
    if i in d:
      d[i] +=1
    else:
      d[i] = 1
   return d
print(most_frequent('Mississippi'))
for i in sorted(most_frequent("mississippi").values(),reverse=True):
    print(i)
