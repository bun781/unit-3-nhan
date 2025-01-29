from kivymd.app import MDApp
class quiz037(MDApp):
    def build(self):
        self.turn = 'x'
        self.locked = []
        self.lockedall = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        self.grid = [ # beautiful grid to compare win conditions
            "0", "0", "0",
            "0", "0", "0",
            "0", "0", "0",
        ]
        return

    def update_screen(self, message):
        print(self.locked)
        if message not in self.locked:
            button = self.root.ids.get(message)
            if self.turn == 'x':
                button.text = 'X'
                button.md_bg_color = '#db1a2e'

                self.root.ids.turn.text = "It is O's turn" # update screen

                self.turn = 'o'

                self.grid[int(message)] = "X" # update grid
            elif self.turn == 'o':
                button.text = 'O'
                button.md_bg_color = "#ff9752"


                self.root.ids.turn.text = "It is X's turn" # update screen

                self.turn = 'x'

                self.grid[int(message)] = "O" # update grid

            if (
                    (self.grid[0] == self.grid[1] == self.grid[2] and self.grid[0] != "0") or
                    (self.grid[3] == self.grid[4] == self.grid[5] and self.grid[3] != "0") or
                    (self.grid[6] == self.grid[7] == self.grid[8] and self.grid[6] != "0") or
                    (self.grid[0] == self.grid[4] == self.grid[8] and self.grid[0] != "0") or
                    (self.grid[2] == self.grid[4] == self.grid[6] and self.grid[2] != "0") or
                    (self.grid[0] == self.grid[2] == self.grid[6] and self.grid[0] != "0") or
                    (self.grid[1] == self.grid[4] == self.grid[7] and self.grid[1] != "0") or
                    (self.grid[2] == self.grid[5] == self.grid[8] and self.grid[2] != "0")
            ):
                if self.turn == "o":
                    self.turn = "x"
                elif self.turn == "x":
                    self.turn = "o"

                self.root.ids.turn.text = f'{self.turn} wins!'
                self.locked = self.lockedall
        self.locked.append(message) # simple square lock mechanism :)
        
a = quiz037()
a.run()
