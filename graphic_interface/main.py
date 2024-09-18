import flet as ft
from backend.brain import brain


def main(page: ft.Page):
    # Establecer el título de la ventana
    page.title = "Ventana Simple"

    # Ajustar el tamaño de la ventana
    page.window.width = 300  # Ancho de la ventana
    page.window.height = 200  # Altura de la ventana

    # Función para cerrar la ventana
    def cerrar_ventana(e):
        page.window_close()  # Cerrar la ventana

    # Función para simular la apertura de algo
    def abrir_algo(e):
        brain()

    # Crear un texto de saludo
    saludo = ft.Text("Hola", size=30)

    # Crear los botones de cerrar y abrir
    btn_cerrar = ft.ElevatedButton(text="Cerrar", on_click=cerrar_ventana)
    btn_abrir = ft.ElevatedButton(text="Abrir", on_click=abrir_algo)

    # Añadir todos los elementos a la página
    page.add(
        saludo,
        btn_abrir,
        btn_cerrar
    )

# Ejecutar la aplicación
ft.app(target=main)
