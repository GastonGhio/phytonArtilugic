import re

"""
#EXPRESIONES REGULARES DE PHYTON

match()
search ()
findall()
finditer()
"""

patron= re.compile("a")


#MATCH busca matchear tmb en el order
print(patron.match("alamo"))
print(patron.match("eva"))

#SEARCH busca q coincida en alguna parte
print(patron.search("perra"))
print(patron.search("perrosalchicha"))
print(patron.search("gordovichicho"))

#FINDALL te dice la cantidad de vceces q encontro el patron
print(patron.findall("salchicha"))
print(patron.findall("porton"))

patroncito = re.compile("[^abc]")

print(patroncito.findall("malaguero"))
