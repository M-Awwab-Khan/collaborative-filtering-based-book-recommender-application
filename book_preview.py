import flet as ft

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
                                width=250,
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
                    width=210,
                    padding=10,
                ),
                col={"md": 3},
            )
    def open_book_modal(self, e):
        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Please confirm"),
            content=ft.ElevatedButton(text="Elevated button"),
            actions=[
                ft.TextButton("Close", on_click=self.close_book_modal),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        e.page.show_dialog(self.dlg_modal)
        self.update()

    def close_book_modal(self, e):
        e.page.close_dialog()
        self.update()