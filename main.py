import flet as ft
from selenium import webdriver
import time
from extracting_members import extract_member
from add_member_to_group import add_member
from datetime import datetime


def main(page: ft.Page):
    page.title = "WhatsApp Bot"

    pr = ft.ProgressRing(width=16, height=16, stroke_width=2)
    page.add(pr)
    driver = webdriver.Firefox()
    page.remove(pr)

    def close_app(e):
        driver.quit()
        time.sleep(1)
        page.window_close()

    def dialog_true(e):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        dlg_modal.open = False
        page.update()
        lv.clean()
        lv.controls.append(ft.Text("Extracting Members..."))
        page.update(lv)
        target_group = target_group_input.value
        my_group = my_group_input.value
        members = extract_member(driver, page, lv, target_group)  # Extracting Members
        my_file = open(f"{str(timestamp)}.txt", "w")
        for member in members:
            my_file.write(member + "\n")
        my_file.close()
        lv.controls.append(ft.Text(members))
        page.update(lv)
        time.sleep(2)
        lv.controls.append(ft.Text(f"Adding Members to {my_group}"))
        page.update(lv)
        add_member(driver, page, lv, my_group, members)  # Adding member to group

        lv.controls.append(ft.Text("Adding Completed."))
        btn.disabled = False
        page.update()

    def dialog_false(e):
        dlg_modal.open = False
        page.update()
        lv.clean()
        lv.controls.append(ft.Text("Canceled"))
        btn.disabled = False
        page.update()

    def start(e):
        if target_group_input.value != "" and my_group_input.value != "":
            btn.disabled = True
            page.update(btn)
            try:
                driver.get("https://web.whatsapp.com/")
            except:
                btn.disabled = False
            dlg_modal.open = True
            page.update()

    my_group_input = ft.CupertinoTextField(placeholder_text="My Group Name")
    target_group_input = ft.CupertinoTextField(placeholder_text="Target Group Name")
    btn = ft.CupertinoButton(
        content=ft.Text("Submit", color=ft.colors.BLACK),
        bgcolor=ft.colors.GREEN,
        alignment=ft.alignment.top_left,
        border_radius=ft.border_radius.all(15),
        opacity_on_click=0.5,
        on_click=start,
    )
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Are you Logged in?"),
        actions=[
            ft.TextButton("Yes", on_click=dialog_true),
            ft.TextButton("No", on_click=dialog_false),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.add(my_group_input, target_group_input, btn)
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.CLOSE, text="Exit App", on_click=close_app, bgcolor=ft.colors.RED
    )
    page.add(lv)
    page.add(dlg_modal)


ft.app(target=main)
