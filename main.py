import flet as ft
import pickle
# import base64
# import requests
# import numpy as np
# from io import BytesIO
# from PIL import Image
from book_preview import BookPreview

popular_df = pickle.load(open('popular.pkl', 'rb'))
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}

class PopularPage(ft.UserControl):
    def build(self):
        self.cards_grid = ft.Row(wrap=True, alignment = ft.MainAxisAlignment.CENTER)
        self.cards_grid.width = 1280
        main_column = ft.Column(
            spacing=20,
            height=650,
            scroll=ft.ScrollMode.ADAPTIVE,
            controls=[
                ft.Text(
                    "Top 50 Books",
                    size=40,
                    weight=ft.FontWeight.BOLD,
                ),
                self.cards_grid
            ]
        )

        

        main_container = ft.Container(
            content=main_column,
            padding=50,

        )
        return main_container

    def insert(self):
        for _, row in popular_df.iterrows():
            # response = requests.get(row['Image-URL-M'], headers=headers, stream=True)
            # img = Image.open(response.raw)
            # arr = np.asarray(img)
            # pil_img = Image.fromarray(arr)
            # buff = BytesIO()
            # pil_img.save(buff, format="JPEG")
            # newstring = base64.b64encode(buff.getvalue()).decode("utf-8")
            to_insert = BookPreview(row['ISBN'], row['Book-Title'], row['Book-Author'], row['Year-Of-Publication'], row['num_ratings'], row['avg_ratings'])
            self.cards_grid.controls.append(to_insert)
            self.update()


def main(page: ft.Page):
    page.title = "Collaborative Filtering Based Book Recommender"

    popular_page = PopularPage()

    page.add(
        popular_page
    )
    popular_page.insert()

ft.app(target=main)