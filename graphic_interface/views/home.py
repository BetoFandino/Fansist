import flet as ft
from flet_route import Params, Basket
from graphic_interface.views.utils.appbar import AppBarCustom


class MyHome:
    def __init__(self, brain):
        self.brain = brain

    def view(self, page: ft.Page, params: Params, basket: Basket):
        img = ft.Container(
            ft.Image(
                src="assets/fansist.png",
                width=100,
                height=100,
            ),
            alignment=ft.alignment.center
        )
        input_command = ft.TextField(
            label="Ingresa comando",
            width=200,
            )
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        def disable_enable_voice_listening(e):
            if btn_activate_listening.icon_color == "green":
                self.brain.disable_listen_command()
                btn_activate_listening.icon_color = "red"
            else:
                self.brain.enable_listen_command()
                btn_activate_listening.icon_color = "green"

            # Actualizar la página después del cambio de color
            page.update()

        def manual_execute(e):
            command = input_command.value
            self.brain.input_manual_command(command)

        btn_activate_listening = ft.IconButton(
            icon=ft.icons.MIC, icon_color="green",
            on_click=disable_enable_voice_listening
        )

        # Botón para ejecutar el comando manualmente
        btn_manual_execute = ft.ElevatedButton(text="Manual", on_click=manual_execute)

        row = ft.Row([btn_manual_execute, btn_activate_listening], alignment=ft.MainAxisAlignment.CENTER)
        return ft.View(
            "/",
            controls=[AppBarCustom().appbar_custom(page), img, input_command, row],
            scroll=ft.ScrollMode.ADAPTIVE
        )