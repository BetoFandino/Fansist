import flet as ft



class AppBarCustom:
    def __init__(self):
        pass
        # self.authenticate = authenticate

    def appbar_custom(self, page: ft.Page):

        app_bar = ft.AppBar(
            leading_width=180,
            bgcolor=ft.colors.BLACK45,
            actions=[
                ft.IconButton(ft.icons.HOME, tooltip='Inicio', on_click=lambda _: page.go('/')),
                ft.IconButton(
                    icon=ft.icons.SETTINGS_OUTLINED,
                    tooltip='Configuraciones',
                    on_click=lambda _: page.go('/config/'), disabled=False
                ),


            ],
        )

        # if self.authenticate:
        #     app_bar.actions[1].disabled = False

        return app_bar