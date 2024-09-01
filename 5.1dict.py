from multiprocessing import Value
s={"name":"laksh","age":"21","class":"4th year"}
print(s)
print(s["laksh"])
print(s.values["laksh"])
print(s.values())
print(s.items())
print(s.keys())
print(s.update({"address":"Ayanavaram"}))
print(s)

for key,value in s.items():
    print(key,value)
#COMPREHENSIVE WAY TO CREATE DICTIONARY
com={ x: x*x for x in range(5)}
print(com)