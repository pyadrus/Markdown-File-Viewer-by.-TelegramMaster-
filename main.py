import flet as ft


def main(page: ft.Page):
    page.scroll = "auto"
    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",  # Шрифт
    }

    # Устанавливаем размер окна
    page.window_width = 800
    page.window_height = 600

    def open_file_dialog(e):
        file_picker.pick_files(allowed_extensions=['md'])

    def on_file_chosen(e):
        selected_file = e.files[0].path if e.files else None
        if selected_file and selected_file.endswith('.md'):
            with open(selected_file, "r", encoding='utf-8') as f:
                table = f.read()
            page.clean()  # Очищаем страницу с данными
            page.add(
                ft.Markdown(
                    table,
                    selectable=True,
                    code_theme="atom-one-dark",  # Стиль кода для выделения текста
                    code_style=ft.TextStyle(font_family="Roboto Mono"),
                    on_tap_link=lambda e: page.launch_url(e.data),
                )
            )
        else:
            page.add(ft.Text("Пожалуйста, выберите действительный файл Markdown (.md)", color="red"))

    file_picker = ft.FilePicker(on_result=on_file_chosen)  # Создаем объект FilePicker для выбора файла
    page.overlay.append(file_picker)  # Добавляем объект FilePicker в окно overlay для открытия файла в окне overlay

    # Добавляем заголовок и кнопку для выбора файла
    page.add(
        ft.Column(
            [
                ft.Text("Программа для открытия Markdown файлов",
                        size=14,
                        ),
                ft.Text("Программа создана с помощью фреймворка Flet",
                        size=14,
                        ),
                ft.Text("https://t.me/master_tg_d",
                        size=14,
                        ),
                ft.ElevatedButton("Выберите файл Markdown", on_click=open_file_dialog)  # Кнопка для выбора файла
            ],
        )
    )


ft.app(target=main, assets_dir="assets")
