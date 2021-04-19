liste=[]
while True:
  a=input("Type 'ok' when you are done: ")
  if a.isdigit():
    liste.append(int(a))
  else: 
    break
minler=[0]
toplam=0
for i in range(1,len(liste)):
  if i==len(liste)-1:
    minler.append(0)
  elif i==1:
    minler.append(min(max(liste[i+1:]), liste[0]))
  elif i==len(liste)-2:
    minler.append(min(liste[len(liste)-1], max(liste[(i-1)::-1])))
  else:
    minler.append(min(max(liste[i+1:]), max(liste[(i-1)::-1])))
for i in range(len(liste)):  
  if liste[i] < minler[i]:
    toplam+=minler[i]-liste[i]
print(toplam)