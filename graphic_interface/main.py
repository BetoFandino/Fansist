import flet as ft
import math
from backend.brain import brain

def main(page: ft.Page):
    # Establecer el título de la ventana
    page.title = "Ventana Simple"

    # Ajustar el tamaño de la ventana
    page.window_width = 300  # Ancho de la ventana
    page.window_height = 200  # Altura de la ventana

    # Establecer el diseño a tamaño completo
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Función para cerrar la ventana
    def cerrar_ventana(e):
        page.window_close()  # Cerrar la ventana

    # Función para simular la apertura de algo
    def abrir_algo(e):
        brain()

    # Crear un texto de saludo
    saludo = ft.Text("Hola", size=30, color="white")

    # Crear los botones de cerrar y abrir
    btn_cerrar = ft.ElevatedButton(text="Cerrar", on_click=cerrar_ventana)
    btn_abrir = ft.ElevatedButton(text="Abrir", on_click=abrir_algo)

    fansist_imagen = ft.Image(
        src="assets/fansist.png",  # Ruta de la imagen local
        width=100,  # Ajustar el ancho de la imagen
        height=100,  # Ajustar la altura de la imagen
    )

    # Crear el contenedor de fondo con el gradiente que ocupe toda la ventana
    background = ft.Container(
        content=ft.Column(
            [
                fansist_imagen,
                btn_abrir,
                btn_cerrar
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand=True,  # Esto hace que el fondo ocupe todo el espacio de la ventana
        alignment=ft.alignment.center,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.Alignment(0.8, 1),
            colors=[
                "0xff1f005c",
                "0xff5b0060",
                "0xff870160",
                "0xffac255e",
                "0xffca485c",
                "0xffe16b5c",
                "0xfff39060",
                "0xffffb56b",
            ],
            tile_mode=ft.GradientTileMode.MIRROR,
            rotation=math.pi / 3,
        ),
    )

    # Añadir el contenedor de fondo a la página
    page.add(background)

# Ejecutar la aplicación
ft.app(target=main)
