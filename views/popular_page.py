import flet as ft
import pickle
import os
from models.book_card import BookCard
from models.modal_manager import ModalManager

popular_df = pickle.load(open(os.path.join(os.getcwd(), 'data', 'popular.pkl'), 'rb'))
modal_manager = ModalManager()

class PopularPage(ft.UserControl):
    def build(self):
        self.cards_grid = ft.Row(wrap=True, width=1366)
        main_column = ft.Column(
            spacing=20,
            height=610,
            scroll=ft.ScrollMode.ADAPTIVE,
            controls=[
                ft.Text(
                    "Top 50 Books",
                    size=55,
                    weight=ft.FontWeight.BOLD,
                ),
                self.cards_grid,
                ft.Divider(height=70)
            ]
        )

        main_container = ft.Container(
            content=main_column,
            margin=ft.margin.Margin(30, 0, 30, 0),
        )
        return main_container

    def insert(self):
        for _, row in popular_df.iterrows():
            to_insert = BookCard(row['ISBN'], row['Book-Title'], row['Book-Author'], row['Year-Of-Publication'], row['num_ratings'], row['avg_ratings'], open_modal=modal_manager.open_book_modal)
            self.cards_grid.controls.append(to_insert)
            self.update()

