import flet as ft

class SearchPage(ft.UserControl):
    def build(self):
        self.cards_grid = ft.Row(wrap=True)
        search_field = ft.TextField(label="Search Book", hint_text="Enter book name, author name, publisher or isbn", width=900, border_width=0.7, border_radius=10)
        return ft.Container(
            content=ft.Column([
                ft.Text('Search Books', theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM, weight=ft.FontWeight.BOLD),
                ft.Row([
                    search_field,
                    ft.FloatingActionButton(
                        icon=ft.icons.SEARCH_ROUNDED,
                        tooltip="Search",
                        shape=ft.CircleBorder()
                    )
                ]),
                self.cards_grid
            ], spacing=30),
            padding=50
        )
    