import dearpygui.dearpygui as dpg

class Theme():
    def __init__(self):
        pass

    def default(self):
        with dpg.theme() as global_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_Border, (243, 180, 191), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Separator, (64, 66, 87), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (38, 40, 58), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (38, 40, 58), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (45, 47, 66), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (52, 54, 75), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (52, 54, 75), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (254, 124, 142), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Button, (38, 40, 58), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (54, 56, 77), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (254, 124, 142), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Tab, (38, 40, 58), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TabHovered, (48, 50, 70), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TabActive, (254, 124, 142), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (52, 54, 75), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, (52, 54, 75), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, (38, 40, 58), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, (254, 124, 142), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, (254, 124, 142), category=dpg.mvThemeCat_Core)

                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 2, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 2, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_PopupRounding, 2, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 2, category=dpg.mvThemeCat_Core)
        dpg.bind_theme(global_theme)

class Viewport():
    def __init__(self, vpTitle: str="", vpWidth: int=0, vpHeight: int=0):
        self.vpTitle=vpTitle
        self.vpWidth=vpWidth
        self.vpHeight=vpHeight

    def create(self, vpIcon: str=""):
        dpg.create_context()
        Theme().default()
        dpg.create_viewport(title=self.vpTitle, width=self.vpWidth, height=self.vpHeight, resizable=False, )
        if len(vpIcon)>0:
            dpg.set_viewport_small_icon(vpIcon)
            dpg.set_viewport_large_icon(vpIcon)
        dpg.setup_dearpygui()
        return Viewport()
    
    def show(self, containerTag: str=""):
        dpg.show_viewport()
        if len(containerTag)>0:
            dpg.set_primary_window(containerTag, True)
        while dpg.is_dearpygui_running():
            dpg.render_dearpygui_frame()
        dpg.start_dearpygui()
    
    def destroy(self):
        dpg.destroy_context()

class Font():
    def __init__(self):
        pass
    
    def register(self, path: str, size: int):
        with dpg.font_registry():
            dpg.add_font(path, size)
    
    def show(self, font: object):
        dpg.bind_font(font)
    
    def show_manager(self):
        dpg.show_font_manager()

class Texture():
    def __init__(self, width: int=0, height: int=0):
        self.width=width
        self.height=height
    
    def get_texture_data(self, r: int=255, g: int=0, b: int=0, a: int=255):
        texture_data=[]
        for i in range(self.width * self.height):
            texture_data.append(r)
            texture_data.append(g)
            texture_data.append(b)
            texture_data.append(a)
        return texture_data
    
    def create(self, texture_data: list, tag: str):
        with dpg.texture_registry(show=False):
            dpg.add_static_texture(width=self.width, height=self.height, default_value=texture_data, tag=tag)
    
    def create_image(self, path: str, tag: str):
        width, height, channels, data = dpg.load_image(path)
        if self.width==0 and self.height==0:
            with dpg.texture_registry(show=False):
                Texture(width, height).create(data, tag)
        else:
            with dpg.texture_registry(show=False):
                Texture(self.width, self.height).create(data, tag)
    
    def save_image(self, path: str, texture_data: list, components: int):
        dpg.save_image(file=path, width=self.width, height=self.height, data=texture_data, components=components)