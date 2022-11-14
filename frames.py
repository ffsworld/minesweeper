from tkinter import *
import settings
import utils


class Frames:
    top_frame = None
    left_frame = None
    center_frame = None
    game_title = None
    root = None

    @staticmethod
    def getRoot(root):
        Frames.root = root

    @staticmethod
    def initialize_frames():

        Frames.top_frame = Frame(
            Frames.root,
            bg='black',  # Change later to black
            width=settings.WIDTH,
            height=utils.height_prct(25)
        )
        # where the top left corner of the frame will be placed at
        Frames.top_frame.place(x=0, y=0)

        Frames.left_frame = Frame(
            Frames.root,
            bg='black',
            width=utils.width_prct(25),
            height=utils.height_prct(75)
        )
        Frames.left_frame.place(x=0, y=utils.height_prct(25))

        Frames.center_frame = Frame(
            Frames.root,
            bg='black',
            width=utils.width_prct(75),
            height=utils.height_prct(75)
        )
        Frames.center_frame.place(x=utils.width_prct(25),
                                  y=utils.height_prct(25))

    @staticmethod
    def initialize_gametitle(some_frame, title):

        Frames.game_title = Label(
            some_frame,  # top_frame
            bg='black',
            fg='white',
            text=title,
            font=('', 48)
        )
        Frames.game_title.place(x=0, y=0)

    @staticmethod
    def update_gametitle(newTitle):
        Frames.game_title.config(text = newTitle)
