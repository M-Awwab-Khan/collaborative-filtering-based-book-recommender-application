import flet as ft

def main(page: ft.Page):
    page.title = "Collaborative Filtering Based Book Recommender"

    heading_text = ft.Text(
        "Top 50 Books",
        size=40,
        color=ft.colors.BLACK,
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

    page.add(
        main_container
    )

ft.app(target=main)