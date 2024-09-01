lak=("Lakshman is the greatest of all")
laksh= "Lakshman is the goat "
#print(lak)
#lak.replace("Lakshman","Praveen")
laksh.replace("goat","GOAT")
#print(laksh)
fruits=['banana','apple','grapes','mango','watermelon']
fruits.pop()
fruits.remove('banana')
print(fruits)
fruits.extend(fruits)
fruits.append('paya')
fruits.insert(1,'kiwi')
fruits.remove('mango')
fruits.reverse()
fruits.sort(reverse=False)
fruits
fruits.index('kiwi')
print('grapes'in fruits)

asd=' - '.join(fruits)
asd


cs_courses = {"S/w", "H/w", "Project" }
print(cs_courses)

art_courses = {"S/w", "H/w", "Design","Art"}
print(art_courses)
print(cs_courses.intersection(art_courses)) # it prints the values which are present in both the sets
print(cs_courses.difference(art_courses))   # it prints the values which are not present in the art_courses but present in the cs_courses
print(cs_courses.union(art_courses))      