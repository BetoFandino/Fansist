import flet as ft
from flet_route import Routing, path

import views.home




def routes(brain):

    app_routes = [
        path(
            url="/",
            clear=True,
            view=views.home.MyHome(brain).view
        ),
        # path(
        #     url="/config/",
        #     clear=True,
        #     view=SettingsAI().view
        # )
    ]

    return app_routes
