from tkinter import *
from tkinter import messagebox
from tkmacosx import Button
import random
import settings
import time
from frames import Frames


class Cell:
    # all = []
    # cell_count = settings.CELL_COUNT
    # cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.is_opened = False
        self.is_mine_candidate = False
        self.x = x
        self.y = y

        # Append the object to Cell.all list
        Cell.all.append(self)

    @staticmethod
    def initialize_cells(frame):
        for x in range(settings.GRID_SIZE):
            for y in range(settings.GRID_SIZE):
                c = Cell(x, y)
                c.create_btn_object(frame)  # center_frame
                c.cell_btn_object.grid(
                    column=x,
                    row=y
                )
        Cell.randomize_mines()
    @staticmethod
    def initialize_root(root):
        Cell.root = root        
    @staticmethod
    def initialize_counts(frame):
        Cell.create_cell_count_label(frame)  # left_frame
        Cell.cell_count_label_object.place(x=0, y=0)

    @staticmethod
    def restart_game():
        Cell.start_game(Frames.center_frame, Frames.left_frame)
    @staticmethod
    def start_game(cell_frame, count_label_frame):
        Cell.initialize_mines()
        Cell.initialize_cells(cell_frame)
        Cell.initialize_counts(count_label_frame)

        
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=60,
            height=40
        )
        # <Button-1> is left click, <Button-3> is right click
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-2>', self.right_click_actions)  # TODO
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells left:{settings.CELL_COUNT}",
            width=12,
            height=4,
            font=("", 30)
        )
        # return lbl
        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_current_cell()
            self.update_cell_count_label()
            if Cell.cell_count == settings.MINES_COUNT:
                print("You won!")
                self.exit_application(isWin=True)
        # Cancel left and right click events if cell is already opened:
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-2>')  # TODO

    def show_current_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.is_opened = True
            if not self.surrounded_cells_mines_length:  # cell = 0
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_current_cell()
            else:
                self.cell_btn_object.configure(
                    text=self.surrounded_cells_mines_length
                )

            # If this was a mine candidate, then for safety, we should configure the bg color to SystemButtonFace
        self.cell_btn_object.configure(
            bg='SystemButtonFace'
        )
        return

    def show_cell(self, is_zero=False):
        if not self.is_opened:
            Cell.cell_count -= 1
            if not is_zero:
                self.cell_btn_object.configure(
                    text=self.surrounded_cells_mines_length
                )
            self.is_opened = True
        # If this was a mine candidate, then for safety, we should configure the bg color to SystemButtonFace
        self.cell_btn_object.configure(
            bg='SystemButtonFace'
        )

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    # Use it as an attribute like these defined in constructor
    # self.surrounded_cells
    def surrounded_cells(self):
        cells = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                if self.get_cell_by_axis(self.x-i, self.y-j):
                    cells.append(self.get_cell_by_axis(self.x-i, self.y-j))
        return cells

    @property
    def surrounded_cells_mines_length(self):
        return sum([i.is_mine for i in self.surrounded_cells])

    def update_cell_count_label(self):
        if Cell.cell_count_label_object:
            Cell.cell_count_label_object.configure(
                text=f"Cells left:{Cell.cell_count}"
            )

    def show_mine(self):
        # A logic to interrupt the game and display a message that player lost

        self.cell_btn_object.configure(
            bg='red'
        )
        # Frames.update_gametitle("You Lost!")
        # time.sleep(10)
        # Frames.update_gametitle("Restart?")
        self.exit_application(isWin=False)
        # Cell.start_game(Frames.center_frame, Frames.left_frame)
        


        # if messagebox.askretrycancel('retry', 'Failed! want to try again?') == True:

    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate = False

    def exit_application(self,isWin):
        if not isWin:
            msg_box = messagebox.askquestion('You Lost', 'You Lost 🥲 Would you like to restart?',
                                                icon='warning')
        else:
            msg_box = messagebox.askquestion('You Won', 'You Won 😎 Would you like to restart?')
        if msg_box == 'yes':
            Cell.start_game(Frames.center_frame, Frames.left_frame)
        
        else:
            messagebox.showinfo('Return', 'The game window will be closed now.')
            Cell.root.destroy()

    @staticmethod
    # a method does not belong to any object instance,
    # but belongs globally to the class
    def initialize_mines():
        Cell.all = []
        Cell.cell_count = settings.CELL_COUNT
        Cell.cell_count_label_object = None
        Frames.game_title.config(text = "Minesweeper Game")
    @staticmethod
    # a method does not belong to any object instance,
    # but belongs globally to the class
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
        

    def __repr__(self):  # override this method, to print things we want
        return f"Cell({self.x},{self.y})"
