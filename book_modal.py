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
        description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam sit amet urna eu erat aliquam gravida vitae eu ligula. Nulla sed congue lectus. Mauris sit amet lacinia est, ac imperdiet magna. Maecenas vel eros suscipit orci bibendum egestas. Vivamus lacinia dui vel lacus finibus placerat. Integer aliquet ligula quis est condimentum pellentesque. Pellentesque ante metus, pulvinar vel ultricies sit amet, suscipit vitae ligula. Fusce vestibulum at velit et lacinia. Donec maximus orci eget nibh sagittis pharetra. Interdum et malesuada fames ac ante ipsum primis in faucibus. Cras libero justo, ultrices vel ipsum ac, laoreet luctus lorem. Quisque placerat molestie est, a venenatis neque fringilla nec.Sed rutrum convallis dui, ac semper turpis ullamcorper a. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Etiam porta luctus mi sit amet faucibus. Donec pellentesque magna nulla, dictum aliquet mauris scelerisque nec. Praesent pellentesque lacinia nulla in bibendum. Proin pulvinar nunc vitae sapien elementum, id vehicula est sodales. Nullam ac elementum nunc. Integer quam dolor, pulvinar a ipsum non, dapibus maximus erat. Morbi in lorem sed urna lobortis iaculis. Morbi lobortis turpis ut tellus convallis gravida. Nunc id ligula luctus, laoreet odio eget, ullamcorper elit. In rhoncus dapibus sem, at rhoncus dolor blandit malesuada. Duis eget enim ex. Donec consectetur, risus sit amet scelerisque suscipit, ipsum mi sagittis felis, ac scelerisque turpis est a ex. In accumsan risus vitae justo maximus pretium. Sed id lectus cursus ante tempus ornare sed sed erat.Aliquam ut sapien non nisl iaculis hendrerit id eu nulla. Sed convallis varius orci, quis aliquam nibh laoreet aliquam. Nullam sodales dui pharetra, auctor lorem a, volutpat odio. Cras nunc elit, sollicitudin vestibulum urna eu, ultricies egestas arcu. Sed tortor orci, convallis vel auctor vel, faucibus sit amet leo. Nullam consectetur aliquet purus, at porta justo rutrum id. Donec turpis mi, interdum non nulla pulvinar, bibendum condimentum dui. Curabitur eu dictum arcu, sed mattis ex. Pellentesque euismod, erat nec convallis lobortis, elit ligula pellentesque quam, vitae tempor lorem ligula vitae risus. Donec nec neque ac mi condimentum ornare eu sit amet ipsum. Etiam in tristique erat. Duis ornare blandit quam quis finibus.Aliquam ut sapien non nisl iaculis hendrerit id eu nulla. Sed convallis varius orci, quis aliquam nibh laoreet aliquam. Nullam sodales dui pharetra, auctor lorem a, volutpat odio. Cras nunc elit, sollicitudin vestibulum urna eu, ultricies egestas arcu. Sed tortor orci, convallis vel auctor vel, faucibus sit amet leo. Nullam consectetur aliquet purus, at porta justo rutrum id. Donec turpis mi, interdum non nulla pulvinar, bibendum condimentum dui. Curabitur eu dictum arcu, sed mattis ex. Pellentesque euismod, erat nec convallis lobortis, elit ligula pellentesque quam, vitae tempor lorem ligula vitae risus. Donec nec neque ac mi condimentum ornare eu sit amet ipsum. Etiam in tristique erat. Duis ornare blandit quam quis'
        content = ft.Column([
                ft.Row([
                    ft.Text(description, width=600, theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                    ft.Image(
                        src='https://www.designforwriters.com/wp-content/uploads/2017/10/design-for-writers-book-cover-tf-2-a-million-to-one.jpg',
                        width=300,
                        fit=ft.ImageFit.CONTAIN
                    )
                ], vertical_alignment=ft.CrossAxisAlignment.START),
                ft.Text(description, width=600, theme_style=ft.TextThemeStyle.BODY_MEDIUM),
            ], height=700, scroll=ft.ScrollMode.ADAPTIVE,)

        return content
