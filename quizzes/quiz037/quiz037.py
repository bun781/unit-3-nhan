from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class mystery(MDApp):
    def build(self):
        return

class MysteryPageA(MDScreen):
    def message1(self):
        self.ids.hello.text = "This is mystery Page A you pressed the button"
    def next(self):
        self.parent.current = "MysteryPageB"

class MysteryPageB(MDScreen):
    def message2(self):
        self.ids.helloe.text = "This is mystery page B you pressed the button"
    def back(self):
        self.parent.current = "MysteryPageA"
t = mystery()
t.run()

