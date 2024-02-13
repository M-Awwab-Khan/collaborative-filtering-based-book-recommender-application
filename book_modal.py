import flet as ft

class BookModal(ft.UserControl):
    def __init__(self, isbn, title, author):
        super().__init__()
        self.modal_data = {
            'isbn': isbn,
            'title': title,
            'author': author
        }

    def build(self):
        description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam sit amet urna eu erat aliquam gravida vitae eu ligula. Nulla sed congue lectus. Mauris sit amet lacinia est, ac imperdiet magna. Maecenas vel eros suscipit orci bibendum egestas. Vivamus lacinia dui vel lacus finibus placerat. Integer aliquet ligula quis est condimentum pellentesque. Pellentesque ante metus, pulvinar vel ultricies sit amet, suscipit vitae ligula. Fusce vestibulum at velit et lacinia. Donec maximus orci eget nibh sagittis pharetra. Interdum et malesuada fames ac ante ipsum primis in faucibus. Cras libero justo, ultrices vel ipsum ac, laoreet luctus lorem. Quisque placerat molestie est, a venenatis neque fringilla nec.'
        content = ft.Row([
                    ft.Text(description, width=500, height=500),
                    ft.Image(
                        src='https://www.designforwriters.com/wp-content/uploads/2017/10/design-for-writers-book-cover-tf-2-a-million-to-one.jpg',
                        width=300,
                        fit=ft.ImageFit.CONTAIN
                    )
                ])

        return content
