import flet as ft
import math
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.brain import Brain

def main(page: ft.Page):
    brain = Brain()
    brain.enable_listen_command()
    page.title = "Fansist"

    page.window_width = 350
    page.window_height = 250

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    input_command = ft.TextField(
        label="Ingresa comando",
        width=200,
    )

    def disable_enable_voice_listening(e):
        if btn_activate_listening.icon_color == "green":
            brain.disable_listen_command()
            btn_activate_listening.icon_color = "red"
        else:
            brain.enable_listen_command()
            btn_activate_listening.icon_color = "green"

        # Actualizar la página después del cambio de color
        page.update()

    def manual_execute(e):
        command = input_command.value
        brain.input_manual_command(command)

    # Botón para activar/desactivar escucha por voz
    btn_activate_listening = ft.IconButton(
        icon=ft.icons.MIC, icon_color="green",
        on_click=disable_enable_voice_listening
    )

    # Botón para ejecutar el comando manualmente
    btn_manual_execute = ft.ElevatedButton(text="Manual", on_click=manual_execute)

    # Imagen del logo o ilustración
    fansist_imagen = ft.Image(
        src="assets/fansist.png",
        width=100,
        height=100,
    )

    # Fondo con gradiente
    background = ft.Container(
        content=ft.Column(
            [
                fansist_imagen,
                input_command,
                ft.Row(  # Usar Row para que los botones estén en una fila
                    [btn_manual_execute, btn_activate_listening],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand=True,
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

    page.add(background)


ft.app(target=main)
