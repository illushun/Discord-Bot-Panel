import dearpygui.dearpygui as dpg

import render.util as render_util
import render.screens.start as screen_start

WIDTH = 800
HEIGHT = 600

getTag = {
    "window": "mainApp_Window"
}

def welcome_screen():
    dpg.push_container_stack(dpg.add_window(label="First Window", tag=getTag["window"]))

    render_util.Texture(400, 400).create_image("assets/images/display-image.png", "display_img")

    dpg.push_container_stack(dpg.add_child_window(label="body", border=False, autosize_x=True, height=HEIGHT - 100))

    dpg.add_image("display_img", pos=((WIDTH / 2) - 200, 10))

    with dpg.group(horizontal=False, pos=((WIDTH / 2) - 200, 420)):
        dpg.add_button(label="Get Started", callback=screen_start.start, width=400)
        dpg.add_button(label="Fonts", callback=render_util.Font().show_manager, width=400)

    # pop child_window container
    dpg.pop_container_stack()
    
    dpg.push_container_stack(dpg.add_child_window(label="footer", no_scrollbar=True, autosize_x=True, autosize_y=True))
    with dpg.group(horizontal=False):
        dpg.add_text("Created by illusion#5641")
    
    # pop child_window container
    dpg.pop_container_stack()

    # pop window container
    dpg.pop_container_stack()

def show_app():
    app=render_util.Viewport("Bot Panel", WIDTH, HEIGHT).create("assets/images/icon.ico")

    first_font = render_util.Font().register("assets/fonts/RobotoMono-Regular.ttf", 20)

    welcome_screen()

    render_util.Font().show(first_font)

    app.show(getTag["window"])
    app.destroy()