# create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency by using dictionaries.


def most_frequent(string):
  d = {}
  for i in string:
    if i in d:
      d[i] +=1
    else:
      d[i] = 1
  return d
a = {k:v for k,v in sorted(most_frequent('Mississippi').items(), reverse = True, key= lambda item:item[1])}
print(a)
