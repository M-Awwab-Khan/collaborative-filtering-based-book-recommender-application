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
                    content=ft.Column(
                        [   
                            ft.Image(
                                src= self.book_info['img_url'],
                                width=200,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            
                            ft.ListTile(
                                title=ft.Text(self.book_info['title']),
                            ),
                            
                            ft.Row(
                                [ft.TextButton("Read More →", on_click=lambda e, x=self.book_info: self.book_info['open_modal'](e, x))],
                                alignment=ft.MainAxisAlignment.END,
                            ),
                        ]
                    ),
                    width=200,
                    padding=5
                ),
            )