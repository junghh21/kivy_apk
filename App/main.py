from kivy.lang import Builder
from kivymd.app import MDApp

root_kv = """
MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        id: toolbar
        title: "Test MDBottomNavigation"
        md_bg_color: app.theme_cls.primary_color
        left_action_items: [["menu", lambda x: None]]

    MDBottomNavigation:
        id: panel

        MDBottomNavigationItem:
            name: "files1"
            text: "Python"
            icon: "language-python"

            BoxLayout:
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(10)
                pos_hint: {"center_x": .5, "center_y": .5}

                MDLabel:
                    font_style: "Body1"
                    theme_text_color: "Primary"
                    text: "Toggle to set custom panel color"
                    halign: "center"

                MDSwitch:
                    size_hint: None, None
                    size: dp(36), dp(48)
                    pos_hint: {"center_x": .5}
                    on_active:
                        panel.panel_color = \
                        [0.2980392156862745, 0.2823529411764706, 0.32941176470588235, 1] \
                        if self.active else app.theme_cls.bg_dark

        MDBottomNavigationItem:
            name: "files2"
            text: "C++"
            icon: "language-cpp"

            MDLabel:
                font_style: "Body1"
                theme_text_color: "Primary"
                text: "I programming of C++"
                halign: "center"

        MDBottomNavigationItem:
            name: "files3"
            text: "JS"
            icon: "language-javascript"

            MDLabel:
                font_style: "Body1"
                theme_text_color: "Primary"
                text: "Oh god JS again"
                halign: "center"
"""


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "KivyMD Examples - Bottom Navigation"
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_string(root_kv)


if __name__ == "__main__":
    MainApp().run()
