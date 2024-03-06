import tkinter as tk
from tkinter import messagebox

# Variable global para almacenar el texto cifrado original
texto_original_cifrado = ""

def cifrar():
    global texto_original_cifrado
    texto = entrada_texto.get("1.0", "end-1c")
    criptograma = cifrar_texto(texto)
    salida_criptograma.config(state="normal")
    salida_criptograma.delete("1.0", "end")
    salida_criptograma.insert("1.0", criptograma)
    salida_criptograma.config(state="disabled")
    # Guardar el texto cifrado original
    texto_original_cifrado = criptograma

def descifrar():
    criptograma = entrada_criptograma.get("1.0", "end-1c")
    texto_plano = descifrar_texto(criptograma)
    salida_texto.config(state="normal")
    salida_texto.delete("1.0", "end")
    salida_texto.insert("1.0", texto_plano)
    salida_texto.config(state="disabled")

#comentario de prueba
    #segundo comentario de prueba
        #tercer comentario
    #hola
def cifrar_texto(texto, columnas=5):
    texto = texto.upper()
    texto_sin_espacios = texto.replace(" ", "")
    if len(texto_sin_espacios) < columnas * columnas:
        texto_sin_espacios += 'X' * (columnas * columnas - len(texto_sin_espacios))
    criptograma = ''
    for columna in range(columnas):
        for i in range(columna, len(texto_sin_espacios), columnas):
            criptograma += texto_sin_espacios[i]
    return criptograma

def descifrar_texto(criptograma, columnas=5):
    filas = int(len(criptograma) / columnas)
    texto_plano = [''] * filas
    for columna in range(columnas):
        for fila in range(filas):
            texto_plano[fila] += criptograma[columna*filas + fila]
    texto_plano = ' '.join(texto_plano)
    texto_plano = texto_plano.replace('X', '')
    return texto_plano


# Crear ventana
ventana = tk.Tk()
ventana.title("Cifrado por Columnas")
ventana.geometry("650x300")

# Etiquetas
tk.Label(ventana, text="Texto a Cifrar:").grid(row=0, column=0, padx=10, pady=5)
tk.Label(ventana, text="Criptograma:").grid(row=0, column=2, padx=10, pady=5)
tk.Label(ventana, text="Criptograma a Descifrar:").grid(row=2, column=0, padx=10, pady=5)
tk.Label(ventana, text="Texto Descifrado:").grid(row=2, column=2, padx=10, pady=5)

# Entradas de texto
entrada_texto = tk.Text(ventana, height=5, width=30)
entrada_texto.grid(row=1, column=0, padx=10, pady=5)
entrada_criptograma = tk.Text(ventana, height=5, width=30)
entrada_criptograma.grid(row=3, column=0, padx=10, pady=5)

# Salidas de texto
salida_criptograma = tk.Text(ventana, height=5, width=30, state="disabled")
salida_criptograma.grid(row=1, column=2, padx=10, pady=5)
salida_texto = tk.Text(ventana, height=5, width=30, state="disabled")
salida_texto.grid(row=3, column=2, padx=10, pady=5)

# Botones
tk.Button(ventana, text="Cifrar", command=cifrar).grid(row=1, column=1, padx=5, pady=5)
tk.Button(ventana, text="Descifrar", command=descifrar).grid(row=3, column=1, padx=5, pady=5)

ventana.mainloop()
