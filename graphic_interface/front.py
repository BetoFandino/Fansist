import flet as ft
from flet_route import Routing, path
from view_routes import routes

from brain import Brain


def main(page: ft.Page):
    brain = Brain()
    brain.enable_listen_command()
    page.title = "Fansist"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50
    page.window_width = 400
    page.window_height = 300
    page.update()
    Routing(page=page, app_routes=routes(brain))
    page.go(page.route)

    # confirm_dialog = ft.AlertDialog(
    #     modal=True,
    #     title=ft.Text("Please confirm"),
    #     content=ft.Text("Do you really want to exit this app?"),
    #     actions_alignment=ft.MainAxisAlignment.END,
    # )


ft.app(
    target=main,
    assets_dir="graphic_interface/assets"
)