from kivymd.app import MDApp
from kivy.core.window import Window
Window.size = (400, 600)

class nhan_calculator(MDApp):
    def build(self):
        self.screen_message = "0"
        self.last_input = ""
        self.is_positive = True
        return

    def update_screen(self, message:str):
        if message in '0123456789':
            self.last_input += message
        elif message != "pm":
            self.last_input = ""
            self.is_positive = True
        else:
            pass


        if message == "AC":
            self.screen_message = "0"
            self.root.ids.screen.text = self.screen_message
        elif message == "pm":
            if self.is_positive:
                self.root.ids.screen.text = self.root.ids.screen.text[:-len(self.last_input)] + f"-{self.last_input}"
                self.screen_message = self.screen_message[:-len(self.last_input)] + f"-{self.last_input}"
                self.is_positive = False
            else:
                self.screen_message = self.screen_message[:-len(self.last_input) - 1] + f"{self.last_input}"
                self.root.ids.screen.text = self.root.ids.screen.text[:-len(self.last_input) - 1] + f"{self.last_input}"
                self.is_positive = True
        elif self.screen_message == "0":
            self.screen_message = message
            self.root.ids.screen.text = self.screen_message
        elif message == "%":
            self.screen_message += "*0.01"
            self.root.ids.screen.text += "%"
        else:
            self.screen_message = self.root.ids.screen.text
            self.screen_message += message
            self.root.ids.screen.text = self.screen_message
        return

    def get_result(self):
        safe = False
        try:
            ball = str(eval(self.screen_message))
            safe = True
        except:
            self.screen_message = "0"
            self.root.ids.screen.text = "0"

        if safe:
            self.screen_message = ball
            self.root.ids.screen.text = ball

a = nhan_calculator()
a.run()


