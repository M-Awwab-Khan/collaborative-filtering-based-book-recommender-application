import flet as ft
from book_modal import BookModal

class BookPreview(ft.UserControl):
    def __init__(self, isbn, title, author, yop, num_ratings, avg_rating):
        super().__init__()
        self.book_info = {
            'isbn': isbn,
            'title': title,
            'author': author,
            'yop': yop,
            'num_ratings': num_ratings,
            'avg_rating': avg_rating
        }
    def build(self):
        return ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [   
                            ft.Image(
                                src= f"https://covers.openlibrary.org/b/isbn/{self.book_info['isbn']}-M.jpg",
                                width=200,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            
                            ft.ListTile(
                                title=ft.Text(self.book_info['title']),
                                subtitle=ft.Text(
                                    f"Author: {self.book_info['author']}({self.book_info['yop']})\nRatings: {round(self.book_info['avg_rating'], 2)}({self.book_info['num_ratings']})"
                                ),
                            ),
                            
                            ft.Row(
                                [ft.TextButton("Read More →", on_click=self.open_book_modal)],
                                alignment=ft.MainAxisAlignment.END,
                            ),
                        ]
                    ),
                    width=200,
                    padding=ft.padding.only(bottom=10)
                ),
            )

    def open_book_modal(self, e):
        dlg_content = BookModal(self.book_info['isbn'], self.book_info['title'], self.book_info['author'])
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(f"{self.book_info['title']}",size=35, weight=ft.FontWeight.W_700),
            content=dlg_content,
            actions=[
                ft.TextButton("Close", on_click=self.close_book_modal),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        e.page.show_dialog(dialog)
        self.update()

    def close_book_modal(self, e):
        e.page.close_dialog()
        self.update()