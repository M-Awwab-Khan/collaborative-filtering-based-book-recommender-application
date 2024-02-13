import flet as ft
import requests

class BookModal(ft.UserControl):
    def __init__(self, book_info):
        super().__init__()
        self.modal_data = book_info

    def build(self):
        response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q=isbn:{self.modal_data['isbn']}')
        data = response.json()['items'][0]['volumeInfo']
        content = ft.Column([
                    ft.Row([
                        ft.Column([
                            ft.Text(f"Author: {self.modal_data['author']}"),
                            ft.Text(f"Year of Publication {self.modal_data['yop']}"),
                            ft.Text(f"Genre: {data['categories'][0]}"),
                            ft.Text(data['description'], width=500, theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                            ft.Text(f"Ratings: {self.modal_data['num_ratings']} ({self.modal_data['avg_rating']})")
                            
                        ]),

                        ft.Column([
                            ft.Image(
                                src=self.modal_data['img_url'],
                                width=230,
                                fit=ft.ImageFit.CONTAIN
                            ),
                            ft.Text(f"Pages: {data['pageCount']}"),
                            ft.Text(f"ISBN 10: {data['industryIdentifiers'][0]['identifier']}"),
                            ft.Text(f"ISBN 13: {data['industryIdentifiers'][1]['identifier']}")
                        ])
                        
                    ], vertical_alignment=ft.CrossAxisAlignment.START, alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ], height=700, scroll=ft.ScrollMode.ADAPTIVE)

        return ft.Container(content=content, padding=20)
