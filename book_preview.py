import flet as ft

class BookPreview(ft.UserControl):
    def __init__(self, isbn, title, author, yop, num_ratings, avg_rating, open_modal, img_url=None):
        super().__init__()
        self.book_info = {
            'isbn': isbn,
            'title': title,
            'author': author,
            'yop': yop,
            'num_ratings': num_ratings,
            'avg_rating': avg_rating,
            'open_modal': open_modal,
            'img_url': f"https://covers.openlibrary.org/b/isbn/{isbn}-M.jpg",
        }
    def build(self):
        return ft.Card(
                content=ft.Container(
                    content=ft.Row(
                        [   
                            ft.Image(
                                src= self.book_info['img_url'],
                                width=100,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Column([
                                ft.ListTile(
                                    title=ft.Text(self.book_info['title'], max_lines=2, overflow="ellipsis"),
                                    subtitle=ft.Text(
                                        f"Author: {self.book_info['author']}({self.book_info['yop']})\nRatings: {round(self.book_info['avg_rating'], 2)}({self.book_info['num_ratings']})"
                                    )
                                ),
                                
                                ft.Row(
                                    [ft.TextButton("Read More →", on_click=lambda e, x=self.book_info: self.book_info['open_modal'](e, x))],
                                    alignment=ft.MainAxisAlignment.END,
                                ),
                            ], width=180)
                        ]
                    ),
                    width=300,
                    padding=5,
                    ink=True
                ),
            )