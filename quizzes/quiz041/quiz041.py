import sqlite3

from kivymd.app import MDApp
from secure_password import encrypt_password

class database_worker:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()


class quiz047(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.components = {"basic":0}

    def build(self):
        return

    def save(self):
        pass

    def update(self):
        #This function updates all the labels in the form using the base salary and the percentage
        # Pseudocode
        # 1- get the base salary from the GUI
        base = self.root.ids.base.text
        if base:
            total = int(base)
            for_hash = ""
            net_salary = total
            for ids in ["inhabitant", "income_tax", "pension", "health"]:
                value = self.root.ids[ids].text
                if value:
                    deduction = int(value)*total//100
                    net_salary -= deduction
                    self.root.ids[ids+'_label'].text = f"{deduction} JPY"

                    for_hash += f"{ids}{deduction}"
                    print(for_hash)
                    for_hash += f"total{deduction}"

            self.root.ids.salary_label.text = f"{net_salary} JPY"

            for_hash += f"total{net_salary}"
            hash = encrypt_password(for_hash)
            self.root.ids.hash.text = hash[-50:]

        # 6- set the label next to the TextField (inhabitant_label, income_tax_label, etc) to the variable new_value
        # 7- concatenate to the hash variable the f"{id}{value}"
        # 8- set the text of the element id=total to the total with the JPY symbol
        # 9- encrypt the hash and change the text of the label with id=hash to the last 50 characters of the hash

        #calculate total


        # update the percentage



    def save(self):
        #repeat the algorithm in update but create variables to save the amount of each item:
        #base = int(base)
        #inhabitant = amount in JPY to remove from base for inhabitant tax
        #income_tax = amount in JPY to remove from base for income tax
        #pension = amount in JPY to remove from base for pension tax
        #health = amount in JPY to remove from base for health tax
        #total = total net salary
        #hahs = hash of the calcualtions in the format
        #inhabitant4,income_tax3,pension2,health1,total1103  (here the numbers next to the category are percentages)

        # query = f"""INSERT into payments
        # --here complete the code
        #
        # """
        # db = database_worker("payments.db")
        # db.run_save(query)
        # db.close()
        self.root.ids.hash.text = f"Payment saved"

    def clear(self):
        for label in ["base", "inhabitant","income_tax","pension","health"]:
            self.root.ids[label].text = ""
            self.root.ids[label+"_label"].text = " JPY"

        self.root.ids["salary_label"].text = " JPY"
        self.root.ids.hash.text = "----"



test = quiz047()
# create = """CREATE TABLE if not exists payments(
#
#
# --- Complete here the table
#
#
#     )"""
# db = database_worker("payments.db")
# db.run_save(create)
# db.close()
test.run()
