import flet as ft
import pickle
from book_preview import BookPreview
from book_modal import BookModal
from search_page import SearchPage

popular_df = pickle.load(open('popular.pkl', 'rb'))

class PopularPage(ft.UserControl):
    def build(self):
        self.cards_grid = ft.Row(wrap=True)
        # self.cards_grid.width = 1700
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
            to_insert = BookPreview(row['ISBN'], row['Book-Title'], row['Book-Author'], row['Year-Of-Publication'], row['num_ratings'], row['avg_ratings'], open_modal=self.open_book_modal)
            self.cards_grid.controls.append(to_insert)
            self.update()

    def open_book_modal(self, e, book_info):
        dlg_content = BookModal(book_info)
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(f"{book_info['title']}",size=35, weight=ft.FontWeight.W_700),
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


def main(page: ft.Page):
    def route_changed(e):
        page.views.clear()
        if e.route == '/':
            p = PopularPage()
            page.views.append(
                ft.View(
                    e.route,
                    [
                    p,
                    page.navigation_bar
                    ],
                )
            )
            page.update()
            p.insert()
        else:
            page.views.append(
                ft.View(
                    e.route,
                    [
                    SearchPage(),
                    page.navigation_bar
                    ],
                )
            )
    
    def tab_changed(e):
        if e.control.selected_index == 0:
            page.go('/')
        else:
            page.go('/search')
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Explore"),
            ft.NavigationDestination(icon=ft.icons.SEARCH, label="Search"),
        ], on_change=tab_changed
    )
    page.title = "Collaborative Filtering Based Book Recommender"
    page.window_width = 1100
    page.window_height = 750
    page.window_resizable = False
    
    page.on_route_change = route_changed
    page.go(page.route)

ft.app(target=main)