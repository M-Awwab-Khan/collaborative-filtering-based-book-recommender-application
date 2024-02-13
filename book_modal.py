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
                            ft.Image(
                                src=self.modal_data['img_url'],
                                width=230,
                                fit=ft.ImageFit.CONTAIN
                            )
                        ]),
                        ft.Column([
                            ft.Text(f"Author: ", spans=[ft.TextSpan(f"{self.modal_data['author']}", ft.TextStyle(weight=ft.FontWeight.NORMAL))], weight=ft.FontWeight.BOLD, size=17),
                            ft.Text(f"Year of Publication: ", spans=[ft.TextSpan(f"{self.modal_data['yop']}", ft.TextStyle(weight=ft.FontWeight.NORMAL))], weight=ft.FontWeight.BOLD, size=17),
                            ft.Text(f"Genre: ", spans=[ft.TextSpan(f"{data['categories'][0]}", ft.TextStyle(weight=ft.FontWeight.NORMAL))], weight=ft.FontWeight.BOLD, size=17),
                            ft.Text(f"Description:\n", spans=[ft.TextSpan(f"{data['description']}", ft.TextStyle(weight=ft.FontWeight.NORMAL))], weight=ft.FontWeight.BOLD, size=17, width=500),
                            ft.Text(f"Pages: ", spans=[ft.TextSpan(f"{data['pageCount']}", ft.TextStyle(weight=ft.FontWeight.NORMAL))], weight=ft.FontWeight.BOLD, size=17),
                            ft.Text(f"ISBN 10: ", spans=[ft.TextSpan(f"{data['industryIdentifiers'][0]['identifier']}", ft.TextStyle(weight=ft.FontWeight.NORMAL))], weight=ft.FontWeight.BOLD, size=17),
                            ft.Text(f"ISBN 13: ", spans=[ft.TextSpan(f"{data['industryIdentifiers'][1]['identifier']}", ft.TextStyle(weight=ft.FontWeight.NORMAL))], weight=ft.FontWeight.BOLD, size=17),
                            ft.Text(f"Ratings: ", spans=[ft.TextSpan(f"{self.modal_data['num_ratings']} ({self.modal_data['avg_rating']})", ft.TextStyle(weight=ft.FontWeight.NORMAL))], weight=ft.FontWeight.BOLD, size=17),
                        ], spacing=17),
                        
                    ], vertical_alignment=ft.CrossAxisAlignment.START, alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ], height=700, scroll=ft.ScrollMode.ADAPTIVE)

        return ft.Container(content=content, padding=20)
