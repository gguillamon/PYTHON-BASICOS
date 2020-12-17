# 6.- Escribir un programa que muestre la tabla ASCII. Extracto:
# Tabla ASCII (caracteres de 32 a 126):
# …
# 60 => <
# 61 => =
# 62 => >
# 63 => ?
# 64 => @
# 65 => A
# 66 => B
# ..
# Gabriel Guillamon
for i in range(32,126):
    print(f"{i} => {chr(i)}")