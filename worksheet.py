from modules.open_digraph import *
import inspect 

a = node( 1,'lol',{}, {} ) 

b = open_digraph([1], [2], [])

print(a) 
print(b)

vide = open_digraph.__empty__()

print(vide)

n = a.copy()

print(n)

m = b.copy()

print(m)

k = a.get_id()

print(k) 

a.set_id(5) 

print(a)

print(dir(node))
print(dir(open_digraph))
