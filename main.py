import flet as ft
import random

input_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '?']
input_special = ['!', '@', '#', '?']


def main(page: ft.Page):
  a = ft.TextField(label="Password", read_only=True)
  def generate_password(e):
    b = random.randint(0, len(input_special) - 1)
    password = (input_list[b])
    b2 = random.randint(0, len(input_list) - 1)
    password2 = (input_list[b2])
    b3 = random.randint(0, len(input_list) - 1)
    password3 = (input_list[b3])
    b4 = random.randint(0, len(input_list) - 1)
    password4 = (input_list[b4])
    b5 = random.randint(0, len(input_list) - 1)
    password5 = (input_list[b5])
    b6 = random.randint(0, len(input_special) - 1)
    password6 = (input_list[b6])
    b7 = random.randint(0, len(input_list) - 1)
    password7 = (input_list[b7])
    b8 = random.randint(0, len(input_list) - 1)
    password8 = (input_list[b8])
    b9 = random.randint(0, len(input_list) - 1)
    password9 = (input_list[b9])
    b10 = random.randint(0, len(input_list) - 1)
    password10 = (input_list[b10])
    b11 = random.randint(0, len(input_list) - 1)
    password11 = (input_list[b11])
    b12 = random.randint(0, len(input_list) - 1)
    password12 = (input_list[b12])
    b13 = random.randint(0,len(input_special) - 1)
    password13 = (input_special[b13])

    passwordcombo = password+password2+password3+password4+password5+password6+password7+password8+password8+password9+password10+password11+password12+password13
    a.value = passwordcombo
    page.update()
    

  page.title = "Python Password Generator"
  page.add(
    ft.Row (
      [
        ft.FilledButton(text="Generate Password", on_click=generate_password),
        a
        
                    
      ],
      alignment=ft.MainAxisAlignment.CENTER,
    )
  )    

ft.app(main)
