import flet as ft
import pickle

popular_df = pickle.load(open('popular.pkl', 'rb'))

class PopularPage(ft.UserControl):
    def build(self):
        heading_text = ft.Text(
            "Top 50 Books",
            size=40,
            weight=ft.FontWeight.BOLD,
        )
        main_column = ft.Column(
            spacing=10,
            controls=[heading_text]
        )

        main_container = ft.Container(
            content=main_column,
            padding=50,
        )
        return main_container

def main(page: ft.Page):
    page.title = "Collaborative Filtering Based Book Recommender"

    popular_page = PopularPage()

    page.add(
        popular_page
    )

ft.app(target=main)