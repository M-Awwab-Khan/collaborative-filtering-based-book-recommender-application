import flet as ft
import pickle
import base64
import requests
import numpy as np
from io import BytesIO
from PIL import Image

popular_df = pickle.load(open('popular.pkl', 'rb'))
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}

response = requests.get('http://images.amazon.com/images/P/0439136350.01.MZZZZZZZ.jpg', headers=headers, stream=True)
img = Image.open(response.raw)
arr = np.asarray(img)
pil_img = Image.fromarray(arr)
buff = BytesIO()
pil_img.save(buff, format="JPEG")

newstring = base64.b64encode(buff.getvalue()).decode("utf-8")
class PopularPage(ft.UserControl):
    def build(self):
        cards_grid = ft.ResponsiveRow()
        for index, row in popular_df.iterrows():

            cards_grid.controls.append(
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column(
                                    [   
                                        ft.Image(
                                            src_base64=newstring,
                                            width=180,
                                            fit=ft.ImageFit.CONTAIN,
                                        ),
                                        
                                        ft.ListTile(
                                            title=ft.Text(row['Book-Title']),
                                            subtitle=ft.Text(
                                                f"{row['Book-Author']}({row['Year-Of-Publication']})"
                                            ),
                                        ),
                                        
                                        ft.Row(
                                            [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
                                            alignment=ft.MainAxisAlignment.END,
                                        ),
                                    ]
                                ),
                                width=200,
                                padding=10,
                            ),
                            col={"md": 3}
                        )
                    )
        main_column = ft.Column(
            spacing=20,
            controls=[
                ft.Text(
                    "Top 50 Books",
                    size=40,
                    weight=ft.FontWeight.BOLD,
                ),
                cards_grid
            ]
        )

        

        main_container = ft.Container(
            content=main_column,
            padding=50,
        )
        return main_container

def main(page: ft.Page):
    page.title = "Collaborative Filtering Based Book Recommender"

    popular_page = PopularPage()

    page.add(
        popular_page
    )

ft.app(target=main)