# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print("Solución para ir desde B hasta A")
print(" ")

print("Con el algoritmo de búsqueda en anchura se obtiene:")
print(search.breadth_first_graph_search(ab).path())
print("Con el algoritmo de búsqueda en profundidad se obtiene:")
print(search.depth_first_graph_search(ab).path())
print("Con el algoritmo de búsqueda de ramificación y salto se obtiene:")
print(search.bab(ab).path())
print("Con el algoritmo de búsqueda de ramificación y salto con subestimación se obtiene:")
print(search.babh(ab).path())


print(" ")
print(" ")
print(" ")

ac = search.GPSProblem('O', 'A'
                       , search.romania)

print("Solución para ir desde A hasta O")
print(" ")

print("Con el algoritmo de búsqueda en anchura se obtiene:")
print(search.breadth_first_graph_search(ac).path())
print("Con el algoritmo de búsqueda en profundidad se obtiene:")
print(search.depth_first_graph_search(ac).path())
print("Con el algoritmo de búsqueda de ramificación y salto se obtiene:")
print(search.bab(ac).path())
print("Con el algoritmo de búsqueda de ramificación y salto con subestimación se obtiene:")
print(search.babh(ac).path())

print(" ")
print(" ")
print(" ")

ad = search.GPSProblem('N', 'C'
                       , search.romania)

print("Solución para ir desde C hasta N")
print(" ")

print("Con el algoritmo de búsqueda en anchura se obtiene:")
print(search.breadth_first_graph_search(ad).path())
print("Con el algoritmo de búsqueda en profundidad se obtiene:")
print(search.depth_first_graph_search(ad).path())
print("Con el algoritmo de búsqueda de ramificación y salto se obtiene:")
print(search.bab(ad).path())
print("Con el algoritmo de búsqueda de ramificación y salto con subestimación se obtiene:")
print(search.babh(ad).path())

print(" ")
print(" ")
print(" ")

ae = search.GPSProblem('L', 'F'
                       , search.romania)

print("Solución para ir desde F hasta L")
print(" ")

print("Con el algoritmo de búsqueda en anchura se obtiene:")
print(search.breadth_first_graph_search(ae).path())
print("Con el algoritmo de búsqueda en profundidad se obtiene:")
print(search.depth_first_graph_search(ae).path())
print("Con el algoritmo de búsqueda de ramificación y salto se obtiene:")
print(search.bab(ae).path())
print("Con el algoritmo de búsqueda de ramificación y salto con subestimación se obtiene:")
print(search.babh(ae).path())

print(" ")
print(" ")
print(" ")

af = search.GPSProblem('V', 'S'
                       , search.romania)

print("Solución para ir desde S hasta V")
print(" ")

print("Con el algoritmo de búsqueda en anchura se obtiene:")
print(search.breadth_first_graph_search(af).path())
print("Con el algoritmo de búsqueda en profundidad se obtiene:")
print(search.depth_first_graph_search(af).path())
print("Con el algoritmo de búsqueda de ramificación y salto se obtiene:")
print(search.bab(af).path())
print("Con el algoritmo de búsqueda de ramificación y salto con subestimación se obtiene:")
print(search.babh(af).path())

print(" ")
print(" ")
print(" ")

ag = search.GPSProblem('M', 'A'
                       , search.romania)

print("Solución para ir desde A hasta M")
print(" ")

print("Con el algoritmo de búsqueda en anchura se obtiene:")
print(search.breadth_first_graph_search(ag).path())
print("Con el algoritmo de búsqueda en profundidad se obtiene:")
print(search.depth_first_graph_search(ag).path())
print("Con el algoritmo de búsqueda de ramificación y salto se obtiene:")
print(search.bab(ag).path())
print("Con el algoritmo de búsqueda de ramificación y salto con subestimación se obtiene:")
print(search.babh(ag).path())
