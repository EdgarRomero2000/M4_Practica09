areas = ['cuina', 7.88, 'menjador', 13.0, 'terrassa', 20.34, 'lavabo', 6.55, 'habitació1', 7.98,
         'habitació2', 12, 'rebedor', 4.23]
# imprimeix el numero en l'index 1
print(areas[1])
# imprimeix el ultim valor de la llista
print(areas[-1])
# imprimeix el valor en l'index 5 de la llista
print(areas[5])
# imprimeix des de el primer valor fins al tercer de la llista
print(areas[:3])
# imprimeix des de el quart valor fins l'ultim de la llista
print(areas[3:])
# suma el desè valor amb el dotzè de la llista
print(areas[9] + areas[11])
# canvia el vuite valor per 100
areas[7] = 100
print(areas)
# afegeix al final de la llista els seguents valors
areas.append("pati_interior")
areas.append(2.78)
print(areas)
