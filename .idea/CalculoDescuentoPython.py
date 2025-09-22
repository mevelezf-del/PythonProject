# Definición de la función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# --- Programa Principal ---

# **Primera llamada:** Usando el descuento por defecto (10%)
print("--- Caso 1: Aplicando el descuento por defecto ---")
compra_1 = 150.00
descuento_1 = calcular_descuento(compra_1)
final_1 = compra_1 - descuento_1

print(f"Monto de la compra: ${compra_1:.2f}")
print(f"Descuento aplicado: ${descuento_1:.2f}")
print(f"Monto final a pagar: ${final_1:.2f}\n")

# **Segunda llamada:** Proporcionando un porcentaje de descuento específico (ej. 15%)
print("--- Caso 2: Aplicando un descuento específico ---")
compra_2 = 220.50
porcentaje_2 = 15
descuento_2 = calcular_descuento(compra_2, porcentaje_2)
final_2 = compra_2 - descuento_2

print(f"Monto de la compra: ${compra_2:.2f}")
print(f"Porcentaje de descuento: {porcentaje_2}%")
print(f"Descuento aplicado: ${descuento_2:.2f}")
print(f"Monto final a pagar: ${final_2:.2f}")