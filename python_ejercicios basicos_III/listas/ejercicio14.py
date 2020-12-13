# Crear un programa que lea los precios de 5 artículos y
# las cantidades vendidas por una empresa en sus 4 sucursales. Informar:
# Las cantidades totales de cada articulo.
# La cantidad de artículos en la sucursal 2.
# La cantidad del articulo 3 en la sucursal 1.
# La recaudación total de cada sucursal.
# La recaudación total de la empresa.
# La sucursal de mayor recaudación.

sucursales=[1,2,3,4]
articulos=[1,2,3,4,5]
precios=[]

for sucursal in sucursales:
    for articulo in articulos:
        precios.append(int(input("Introduzca precio para el articulo %d de la sucursal %d " % (articulo,sucursal))))
        if sucursal[0][0] > articulos[0][4]:
            sumasucursal1+=precios
        elif sucursal[1] and articulos[articulo]:
            sumasucursal2+=precios
        elif sucursal[2] and articulos[articulo]: 
            sumasucursal3+=precios
        elif sucursal[3] and articulos[articulo]:
            sumasucursal4+=precios
        else:
            print("Datos introducidos erróneos, introduzca números enteros")
            

print("La cantidad total vendida del articulo %d es %d " % (articulo,sum(articulo)))
print("La cantidad total de articulos sucursal 2 %d " % (sumasucursal2))
print("La recaudacion de cada sucursal es %d sucursal 1, %d sucursal 2, %d sucursal 3 y %d sucursal 4" % (sumasucursal1,sumasucursal2,sumasucursal3,sumasucursal4))
print("La recaudacion total de la empresa es",sum(sumasucursal1,sumasucursal2,sumasucursal3,sumasucursal4))
print("La sucursal de mayor recaudacion es %d" % (max(sucursales)))
    