"""
Example:
Input:
["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
All inputs will be in lowercase.
The order of your output does not matter. """

# Çözüm - 1

liste = ["eat", "tea", "tan", "ate", "nat", "bat"]
sorted_list = []
result = []
for i in liste:
  if sorted(i) not in sorted_list:
    sorted_list.append(sorted(i))
print(sorted_list)
for a in range(len(sorted_list)):
  result.append([i for i in liste if sorted(i) == sorted_list[a]])
print(result)


# Çözüm - 2

l = ["eat", "tea", "tan", "ate", "nat", "bat"]
d = {}
for w in l:
    w_sort = "" .join(sorted(w))  # sort the word in the given list
    if w_sort in d:  # to check whether sorted word in the dictionary
        d[w_sort].append(w) # add the word as a value, not the sorted word
    else:
        d[w_sort] = [w_sort] # if is not true, add sorted word as key and its values as a list
print(list(d.values())) # get the all the values of the dictionary as a list

# Çözüm - 3 

liste=["eat", "tea", "tan", "ate", "nat", "bat"]
sorted_list=[]
sonuç2=[]
for i in liste:
    if sorted(i) not in sorted_list:
        sorted_list.append(sorted(i))
print(sorted_list)
for a in range(3):
    sonuc=[]
    for i in liste:
        if sorted(i)==sorted_list[a]:
            sonuc.append(i)
    print(sonuc)
    sonuç2.append(sonuc)
print(sonuç2)

# Çözüm - 4 

mylist = ["eat", "tea", "tan", "ate", "nat", "bat"]
emptylist = []
for i in mylist:
    tempSet = set(i)
    # print(tempSet)
    templist = []
    for j in range(len(mylist)):
        if tempSet == tempSet.intersection(set(mylist[j])):
            templist.append(mylist[j])
    if templist not in emptylist:
            emptylist.append(templist)
           
print(emptylist)

# Çözüm - 5

given_l = ["eat", "tea", "tan", "ate", "nat", "bat"]
char = {}
len_l = {}
value_l = []
word_str = ""
word_l = []
value_uniq = set() 
for i in given_l:
  char[i] = set(i)
  if set(i) not in value_l:
    value_l.append(set(i))
for j in value_l:
  word_str = ""
  for i in given_l:
    if j == char[i]:
      word_str += i +" "
  word_str = word_str.strip()
  word_str = word_str.split(" ")
  word_l.append(word_str)      
print(word_l)

# Çözüm - 6

liste = ["eat", "tea", "tan", "ate", "nat", "bat"]
sette = []
result = []
for i in liste:
    if set(i) not in sette:
        sette.append(set(i))
for j in range(len(sette)):
    first_result = []
    for i in liste:
        if set(i) == sette[j]:
            first_result.append(i)
    result.append(first_result)
print(result)