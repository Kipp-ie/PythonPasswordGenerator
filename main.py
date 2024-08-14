import flet as ft

def main(page: ft.Page):
  page.title = "Python Password Generator"
  page.add(
    ft.Row (
      [
        ft.FilledButton(text="Generate Password", on_click=generate_password),
        ft.Divider(),
        ft.TextField(label="Password", read_only=True, value = "Click on generate password")
                    
      ],
      alignment=ft.MainAxisAlignment.CENTER,
    )
  )    
def generate_password(e):
  pass

ft.app(main, view=ft.AppView.WEB_BROWSER)
