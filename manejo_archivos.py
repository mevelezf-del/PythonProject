# --- 1. Escritura de Archivo de Texto usando write() ---

# Nombre del archivo que vamos a crear y manipular.
nombre_archivo = 'mi_tarea_de_python_Maria_Velez.txt'

print(f"Paso 1: Creando y escribiendo en el archivo '{nombre_archivo}'...")

# El bloque 'with open' se usa para abrir el archivo en modo escritura ('w').
# Este método garantiza que el archivo se cierre automáticamente al finalizar.
try:
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        # Usamos el método .write() para añadir contenido al archivo.
        # El carácter '\n' es importante para crear un salto de línea.
        archivo.write("Nombre del Script: manejo_archivos.py\n")
        archivo.write("Autor:Maria Esthefania Velez Freire\n")
        archivo.write("Descripción: Script para la tarea de manejo de archivos.\n")
        archivo.write("Primero: Guardamos el nombre del archivo en una variable.\n")
        archivo.write("Segundo: Usamos un bloque 'try/except' para manejar posibles errores.\n")
        archivo.write("Tercero: La sentencia 'with open' abre el archivo y garantiza que se cierre solo.\n")
        archivo.write("Cuarto: 'w' significa modo escritura (write). Si el archivo existe, lo sobrescribe.\n")
        archivo.write("Quinto: 'encoding='utf-8'' permite usar caracteres especiales como tildes y ñ.\n")
        archivo.write("Sexto: El método .write() escribe una cadena de texto en el archivo.\n")
        
        # --- LÍNEAS CORREGIDAS ---
        # Se añade una barra invertida (\) antes de las comillas internas para "escaparlas".
        archivo.write("Septimo: El carácter '\\n' al final es un \"salto de línea\".\n")
        archivo.write("Iniciamos un bucle infinito que solo se detendrá cuando se lo indiquemos.\n")
        archivo.write("El método .readline() lee una sola línea del archivo y avanza el \"cursor\".\n")
        # --- FIN DE CORRECCIONES ---

        archivo.write("Condición de salida: .readline() devuelve una cadena vacía ('') cuando esta instrucción rompe el bucle 'while'..\n")
        archivo.write("Usamos .strip() para eliminar el carácter de salto de línea ('\\n') invisible.\n")
    
    print("✅ ¡Archivo escrito con éxito!")

except IOError as e:
    print(f"❌ Error al escribir el archivo: {e}")


# --- 2. Lectura de Archivo de Texto usando readline() ---

print(f"\nPaso 2: Leyendo el contenido de '{nombre_archivo}' con readline()...")

try:
    # Abrimos el mismo archivo, pero ahora en modo lectura ('r').
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        print("\n--- Contenido del archivo ---")
        
        # Creamos un bucle infinito que se romperá cuando lleguemos al final del archivo.
        while True:
            # El método .readline() lee una sola línea del archivo en cada llamada.
            linea = archivo.readline()
            
            # Si readline() devuelve una cadena vacía (''), significa que no hay más
            # líneas por leer y hemos llegado al final del archivo.
            if not linea:
                break # Rompemos el bucle while.
            
            # Imprimimos la línea que acabamos de leer.
            # Usamos .strip() para eliminar los saltos de línea invisibles ('\n')
            # y que la salida en la consola se vea limpia.
            print(linea.strip())

except FileNotFoundError:
    print(f"❌ Error: El archivo '{nombre_archivo}' no existe y no se puede leer.")
except IOError as e:
    print(f"❌ Error al leer el archivo: {e}")


# --- 3. Cierre de Archivos ---

# No se necesita una línea 'archivo.close()' porque la estructura 'with'
# ya se encargó de cerrar el archivo de forma segura y automática
# tanto en el bloque de escritura como en el de lectura.
print("\n-----------------------------")
print("✅ Proceso completado. Los archivos se cerraron de forma segura.")

