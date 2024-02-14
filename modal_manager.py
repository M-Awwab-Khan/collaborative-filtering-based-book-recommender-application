import flet as ft
from book_modal import BookModal

class ModalManager:
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
        e.page.update()

    def close_book_modal(self, e):
        e.page.close_dialog()
        e.page.update()
