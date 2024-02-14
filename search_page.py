import flet as ft
from search import search

class SearchPage(ft.UserControl):
    def build(self):
        self.cards_grid = ft.Row(wrap=True)
        self.search_field = ft.TextField(label="Search Book", hint_text="Enter book name, author name, publisher or isbn", width=900, border_width=0.7, border_radius=10)
        return ft.Container(
            content=ft.Column([
                ft.Text('Search Books', theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM, weight=ft.FontWeight.BOLD),
                ft.Row([
                    self.search_field,
                    ft.FloatingActionButton(
                        icon=ft.icons.SEARCH_ROUNDED,
                        tooltip="Search",
                        shape=ft.CircleBorder(),
                        on_click=self.show_suggestions
                    )
                ]),
                self.cards_grid
            ], spacing=30),
            padding=50
        )
    def show_suggestions(self, e):
        search_term = self.search_field.value
        suggestions = search(search_term)

        if suggestions.shape[0] > 0:
            for _, row in suggestions.iterrows():
                print(row)