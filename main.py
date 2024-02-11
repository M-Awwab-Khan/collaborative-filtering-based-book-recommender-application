import flet as ft
import pickle

popular_df = pickle.load(open('popular.pkl', 'rb'))

class PopularPage(ft.UserControl):
    def build(self):
        main_column = ft.Column(
            spacing=10,
            controls=[
                ft.Text(
                    "Top 50 Books",
                    size=40,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    leading=ft.Icon(ft.icons.ALBUM),
                                    title=ft.Text("The Enchanted Nightingale"),
                                    subtitle=ft.Text(
                                        "Music by Julie Gable. Lyrics by Sidney Stein."
                                    ),
                                ),
                                ft.Row(
                                    [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
                                    alignment=ft.MainAxisAlignment.END,
                                ),
                            ]
                        ),
                        width=400,
                        padding=10,
                    )
                )
            ]
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