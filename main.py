import flet as ft
from views.search_page import SearchPage
from views.popular_page import PopularPage

def main(page: ft.Page):
    def route_changed(e):
        page.views.clear()
        if e.route == '/':
            p = PopularPage()
            page.views.append(
                ft.View(
                    e.route,
                    [  
                        page.appbar,
                        p,
                        page.navigation_bar
                    ],
                )
            )
            page.update()
            p.insert()
        else:
            page.views.append(
                ft.View(
                    e.route,
                    [
                        page.appbar,
                        SearchPage(),
                        page.navigation_bar
                    ],
                )
            )
    
    def tab_changed(e):
        if e.control.selected_index == 0:
            page.go('/')
        else:
            page.go('/search')


    def toggle_theme(e):
        e.control.selected = not e.control.selected
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        page.update()

    page.appbar = ft.AppBar(
            title=ft.Text("Collaborative Filtering Based Book Recommender"),
            leading=ft.Icon(ft.icons.PALETTE),
            leading_width=50,
            center_title=True,
            actions=[
                ft.Row([
                    ft.IconButton(
                        ft.icons.DARK_MODE_OUTLINED,
                        selected_icon=ft.icons.WB_SUNNY_OUTLINED,
                        on_click=toggle_theme,
                        tooltip="Toggle brightness"
                    ),
                ])
            ],
    )
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Explore"),
            ft.NavigationDestination(icon=ft.icons.SEARCH, label="Search"),
        ], on_change=tab_changed
    )
    page.title = "Collaborative Filtering Based Book Recommender"
    page.window_maximized = True
    page.window_resizable = False

    page.on_route_change = route_changed
    page.go(page.route)

ft.app(target=main)