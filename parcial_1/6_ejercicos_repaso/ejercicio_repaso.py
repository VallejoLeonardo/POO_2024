"""
Crear un prograa que clacule y obtenga el total a pagar por un producto
determinado. Se debera de solicitar el nombre o descripcion del producto, 
codigo del producto, precio unitario, cantidad de productos.
El total a pagar incluye el iva del 16%y ep descuento.
Si se compran de 1 a 5 productos se otorga un descuento del 10%, si se compran de
6 a 10 productos se otorga un descuento del 15% y si se compran mas de 10 productos el descuento es del 20%
"""

nombre_producto = input("Ingrese el nombre del producto: ")
codigo_producto = input("Ingrese el código del producto: ")
precio_unitario = float(input("Ingrese el precio unitario: "))
cantidad_productos = int(input("Ingrese la cantidad de productos: "))
total = precio_unitario * cantidad_productos

if cantidad_productos >= 1 and cantidad_productos <= 5:
    descuento = total * 0.10
elif cantidad_productos >= 6 and cantidad_productos <= 10:
    descuento = total * 0.15
else:
    descuento = total * 0.20
    
t_descuento = total - descuento
iva = t_descuento * 0.16
total_pagar = t_descuento + iva

print(f"Nombre del producto: {nombre_producto}")
print(f"Código del producto: {codigo_producto}")
print(f"Precio unitario: {precio_unitario}")
print(f"Cantidad de productos: {cantidad_productos}")
print(f"Total: {total}")
print(f"Descuento: {descuento}")
print(f"Total con descuento: {t_descuento}")
print(f"IVA: {iva}")
print(f"Total a pagar: {total_pagar}")


