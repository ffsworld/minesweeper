from cell import Cell
import settings


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


def initialize_counts(frame):
    Cell.create_cell_count_label(frame)  # left_frame
    Cell.cell_count_label_object.place(x=0, y=0)


def start_game(cell_frame, count_label_frame):
    initialize_cells(cell_frame)
    initialize_counts(count_label_frame)
