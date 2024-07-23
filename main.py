import flet as ft

with open("README.md", "r") as f:
    table = f.read()


def main(page: ft.Page):
    page.scroll = "auto"

    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
    }

    page.add(
        ft.Markdown(
            table,
            selectable=True,
            extension_set="gitHubWeb",
            code_theme="atom-one-dark",
            code_style=ft.TextStyle(font_family="Roboto Mono"),
            on_tap_link=lambda e: page.launch_url(e.data),
        )
    )


ft.app(target=main, assets_dir="assets")