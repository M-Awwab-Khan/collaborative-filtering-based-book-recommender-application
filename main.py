import flet as ft
import pickle
from book_card import BookCard
from modal_manager import ModalManager
from search_page import SearchPage

popular_df = pickle.load(open('popular.pkl', 'rb'))
modal_manager = ModalManager()

class PopularPage(ft.UserControl):
    def build(self):
        self.cards_grid = ft.Row(wrap=True)
        # self.cards_grid.width = 1700
        main_column = ft.Column(
            spacing=20,
            height=610,
            scroll=ft.ScrollMode.ADAPTIVE,
            controls=[
                ft.Text(
                    "Top 50 Books",
                    size=55,
                    weight=ft.FontWeight.BOLD,
                ),
                self.cards_grid
            ]
        )

        main_container = ft.Container(
            content=main_column,
            padding=50,

        )
        return main_container

    def insert(self):
        for _, row in popular_df.iterrows():
            to_insert = BookCard(row['ISBN'], row['Book-Title'], row['Book-Author'], row['Year-Of-Publication'], row['num_ratings'], row['avg_ratings'], open_modal=modal_manager.open_book_modal)
            self.cards_grid.controls.append(to_insert)
            self.update()


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
    page.window_width = 1100
    page.window_height = 750
    page.window_resizable = False
    
    page.on_route_change = route_changed
    page.go(page.route)

ft.app(target=main)