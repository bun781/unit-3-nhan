from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.toolbar import Toolbar
from kivymd.uix.list import MDList, OneLineListItem

KV = '''
BoxLayout:
    orientation: 'vertical'

    Toolbar:
        title: "Burger Menu Example"
        background_palette: 'Primary'
        background_hue: '500'
        left_action_items: [['menu', lambda x: nav_drawer.toggle()]]  # Open Drawer

    Widget:

MDNavigationDrawer:
    id: nav_drawer
    BoxLayout:
        orientation: 'vertical'
        spacing: "8dp"
        padding: "8dp"

        MDList:
            OneLineListItem:
                text: "Home"
                on_release: print("Home clicked")
            OneLineListItem:
                text: "Settings"
                on_release: print("Settings clicked")
            OneLineListItem:
                text: "About"
                on_release: print("About clicked")
'''

class BurgerMenuApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

BurgerMenuApp().run()
