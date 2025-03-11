from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from database import DatabaseManager

KV = '''
MDScreen:
    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            title: "Editable Table"
            anchor_title: "center"

        BoxLayout:
            orientation: 'vertical'
            padding: dp(10)
            spacing: dp(10)

            MDRaisedButton:
                text: "Add Row"
                size_hint_x: None
                width: dp(120)
                pos_hint: {"center_x": 0.5}
                on_release: app.add_row()

            Widget:
'''


from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField

from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField


from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField


from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField


class TableScreen(MDScreen):
    data_table = ObjectProperty(None)
    dialog = None
    selected_row_index = None

    def __init__(self, name="Default", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.get_column_name(name=self.name)

        self.row_data = [
            ("Alice", "25", "New York", "New York", "New York"),
            ("Bob", "30", "Los Angeles", "New York", "New York"),
            ("Charlie", "28", "Chicago", "New York", "New York"),
        ]

        self.create_data_table()

    def get_column_name(self, name:str):
        row_dict = {
            "Default": [
                ("Name", dp(20)),
                ("Description", dp(20)),
                ("Cost", dp(20)),
                ("Image", dp(20)),
                ("Last modified by", dp(32)),
                ("food_id", dp(10))
            ],
            "food_listing": [
                ("food_name", dp(40)),
                ("description", dp(60)),
                ("cost", dp(20)),
                ("image", dp(20)),
                ("user_id", dp(32)),
                ("food_id", dp(10))
            ],
            "order_list": [
                ("order_id", dp(20)),
                ("receipt_id", dp(20)),
                ("food_id", dp(20)),
                ("order_date", dp(20)),
                ("status", dp(20)),
                ("last_modified_user_id", dp(32)),
                ("order_id", dp(10))
            ],
            "restaurant": [
                ("name", dp(20)),
                ("location", dp(20)),
            ],
        }
        self.column_data = row_dict.get(name, row_dict["Default"])
    def get_row_data(self, name: str):
        db = DatabaseManager('database.db')
        query_dict = {
            "food_listing": '''select  '''
        }
    def create_data_table(self):
        if self.data_table:
            self.remove_widget(self.data_table)

        self.data_table = MDDataTable(
            size_hint=(0.9, 0.8),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            check=True,
            column_data=self.column_data,
            row_data=self.row_data,
        )

        self.data_table.bind(on_row_press=self.on_row_press)
        self.add_widget(self.data_table)

    def on_row_press(self, instance_table, instance_row):
        """Find the clicked row's index manually and show the dialog."""
        row_text = instance_row.text  # Get text from clicked row
        for i, row in enumerate(self.row_data):
            if row_text in row:  # Check if any value in row matches clicked text
                self.selected_row_index = i
                break

        if self.selected_row_index is not None:
            self.show_edit_dialog()

    def show_edit_dialog(self):
        """Display a popup with text fields for editing row data."""
        self.dialog_content = MDBoxLayout(orientation="vertical", spacing=10, size_hint_y=None, height=600)
        self.text_fields = []

        row_values = self.row_data[self.selected_row_index]  # Get selected row values

        for i, column in enumerate(self.column_data):
            text = row_values[i] if i < len(row_values) else ""
            text_field = MDTextField(hint_text=f"{column[0]}", text=text)
            self.text_fields.append(text_field)
            self.dialog_content.add_widget(text_field)

        self.dialog = MDDialog(
            type="custom",
            content_cls=self.dialog_content,
            buttons=[
                MDRaisedButton(text="Save", on_release=self.save_data),
                MDRaisedButton(text="Cancel", on_release=lambda x: self.dialog.dismiss()),
            ],
        )
        self.dialog.open()

    def save_data(self, instance_button):
        """Update the selected row and recreate the table."""
        if self.selected_row_index is not None:
            new_values = tuple(text_field.text for text_field in self.text_fields)
            self.row_data[self.selected_row_index] = new_values

            self.create_data_table()

        self.dialog.dismiss()





class e(MDApp):
    def build(self):
        self.screen = TableScreen()
        return self.screen

    def add_row(self):
        self.screen.add_row()


if __name__ == "__main__":
    e().run()