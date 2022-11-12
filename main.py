from tkinter import *
import settings
# import utils
import game
from frames import Frames

root = Tk()
# Override the settings of the window
root.configure(bg="black")
window_width = settings.WIDTH
window_height = settings.HEIGHT
center_x = 10
center_y = 20
# width x height
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.title('Minesweeper Game')
root.resizable(False, False)

# frame = Frames(root)
# frame.initialize_gametitle(frame.top_frame)
# game.start_game(frame.center_frame, frame.left_frame)

Frames.getRoot(root)
Frames.initialize_frames()
Frames.initialize_gametitle(Frames.top_frame)
game.start_game(Frames.center_frame, Frames.left_frame)


# Run the window: tk should run until we close it
root.mainloop()
