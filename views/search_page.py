import flet as ft
from utilities.search import search
from models.book_card import BookCard
from models.modal_manager import ModalManager

modal_manager = ModalManager()

class SearchPage(ft.UserControl):
    def build(self):
        self.cards_grid = ft.Row(wrap=True, width=1366)
        self.search_field = ft.TextField(label="Search Book", hint_text="Enter book name, author name, publisher or isbn", width=1200, border_width=0.7, border_radius=10)
        self.error_msg = ft.Text("", size=25, theme_style=ft.TextTheme.title_large)
        return ft.Container(
            content=ft.Column([
                ft.Text('Search Books', size=55, weight=ft.FontWeight.BOLD),
                ft.Row([
                    self.search_field,
                    ft.FloatingActionButton(
                        icon=ft.icons.SEARCH_ROUNDED,
                        tooltip="Search",
                        shape=ft.CircleBorder(),
                        on_click=self.show_suggestions
                    )
                ]),
                self.cards_grid,
                self.error_msg,
            ], spacing=30, height=610, scroll=ft.ScrollMode.ADAPTIVE,),
            padding=ft.padding.Padding(30, 30, 30, 50)
        )
    def show_suggestions(self, e):
        self.cards_grid.controls.clear()
        search_term = self.search_field.value
        suggestions = search(search_term)
        if search_term.strip():
            if suggestions.shape[0] > 0:
                self.error_msg.value = ''
                for _, row in suggestions.iterrows():
                    to_insert = BookCard(row['ISBN'], row['Book-Title'], row['Book-Author'], row['Year-Of-Publication'], row['num_ratings'], row['avg_rating'], open_modal=modal_manager.open_book_modal)
                    self.cards_grid.controls.append(to_insert)
                    self.update()
                self.cards_grid.controls.append(ft.Divider(height=30, thickness=0))
            else:
                self.error_msg.value = "Sorry! Your search yielded no results."
                self.update()
        else:
            self.error_msg.value = "Please fill in the search field to continue."
            self.update()

    