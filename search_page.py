import flet as ft
from search import search
from book_card import BookCard
from modal_manager import ModalManager

modal_manager = ModalManager()

class SearchPage(ft.UserControl):
    def build(self):
        self.cards_grid = ft.Row(wrap=True, alignment=ft.MainAxisAlignment.CENTER, width=1000)
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
            self.cards_grid.controls.clear()
            for _, row in suggestions.iterrows():
                to_insert = BookCard(row['ISBN'], row['Book-Title'], row['Book-Author'], row['Year-Of-Publication'], row['num_ratings'], row['avg_rating'], open_modal=modal_manager.open_book_modal)
                self.cards_grid.controls.append(to_insert)
                self.update()
        else:
            self.cards_grid.controls.append(ft.Text("Sorry! Your search yielded no results.", size=25, theme_style=ft.TextTheme.title_large))
            self.update()

    