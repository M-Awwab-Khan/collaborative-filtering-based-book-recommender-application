import flet as ft
from search_page import SearchPage
from popular_page import PopularPage

def main(page: ft.Page):
    def route_changed(e):
        page.views.clear()
        if e.route == '/':
            p = PopularPage()
            page.views.append(
                ft.View(
                    e.route,
                    [
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