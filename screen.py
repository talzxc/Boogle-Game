import tkinter as tk
from tkinter import messagebox
from typing import *
import boggle

SIZE = 4  # the size of the board
TIME_LIMIT = 180  # the limit of the game in seconds
HARD_LEN = 3  # the length of the shorts word needing in hard difficulty
TIME_LABEL = "time remaining:\n"
SCORE_LABEL = "Score:"
GUESS_LABEL_TEXT = "Words You \nFound:"
# the text that will show on respective labels
BG_COLOR = "lightblue3"  # the color of the background of the game
DICT_FILE = "boggle_dict.txt"  # the word file of the game
GREEN_BUTTON = "./data/GreenButton.png"
GREY_BUTTON = "./data/GreyButton.png"
ORANGE_BUTTON = "./data/OrangeButton.png"
PINK_BUTTON = "./data/PinkButton.png"
# the files for the respective generic buttons
ORANGE_PLAY = "./data/OrangePlay.png"
GREY_PLAY = "./data/GreyPlay.png"
ORANGE_EXIT = "./data/OrangeExit.png"
GREY_EXIT = "./data/GreyExit.png"
GREEN_HOME = "./data/GreenHome.png"
GREY_HOME = "./data/GreyHome.png"
GREY_BACK = "./data/GreyBack.png"
PINK_BACK = "./data/PinkBack.png"
GREEN_RELOAD = "./data/GreenReload.png"
GREY_RELOAD = "./data/GreyReload.png"
GREEN_INFO = "./data/GreenInfo.png"
GREY_INFO = "./data/GreyInfo.png"
GREEN_HELP = "./data/GreenHelp.png"
# the files for the respective special buttons
ORANGE_LABEL = "./data/OrangeLabel.png"
GREEN_LABEL = "./data/GreenLabel.png"
GREY_LABEL = "./data/GreyLabel.png"
PINK_LABEL = "./data/PinkLabel.png"
# the files for the respective labels
TITLE_IMAGE = "./data/GameTitle.png"  # the file of the title image
BIG_TITLE_IMAGE = "./data/MainTitle.png"  # the file of the title image
INFO_TITLE = "./data/InformationTitle.png"  # info page title image
TAL_AVATAR = "./data/TalAvatar.png"  # Tals' avatar image in info page
IDAN_AVATAR = "./data/IdanAvatar.png"  # Idans' avatar image in info page
TAL_QUOTE = '"eh? Whats a Boggle?!"\nTal Koviazin'
IDAN_QUOTE = '"Let epsilon be\ngreater than zero"\nIdan Rachmani'
# the developer quotes in info page
HELP_BOX_TEXT = f"EASY: 'AA' is a word!\nHARD: 'AA' is still a word but it's "\
                f"too short.\n\tOnly {HARD_LEN} letters and up! "
# the text shown when mouse hovers over the help button in difficulty select
TIME_UP_BOX_TITLE = "Bing Bong, Pong Ping"
# the title of the pop-up window when time runs out
TIME_UP_BOX_MESSAGE = "\t\t   Time is UP!\nDuring your last adventure you " \
                      "slayed {0} words for a total of {1} points! Would you "\
                      "like to go for another one? "
# the message on the pop-up window that shows when time runs out
CREDITS = "Tal and Idan HomeworkSubmitters Present... \na Tal and Idan " \
          "production... \n\nExercise 12: Electric Boggle-u\n\n" \
          "Directed by: Tal and Idan\n" \
          "Editors: Tal and Idan\n" \
          "Lead Designers: Tal and Idan\n" \
          "Executive Producer: The Interwebs"
# the credits text that appears on the info page


class Screen:
    def __init__(self):
        self.__root = tk.Tk()  # make the window
        self.__load_assets()  # load all of the images to the window
        self.__root.geometry("500x500")  # set its size
        self.__root.resizable(0, 0)  # make sure the window is not resizable
        self.__root.config(bg=BG_COLOR)  # set background color for the window
        self.__root.title("OH That's a Boggle")  # set the title of the window

        self.__main_menu()
        # create all the elements relating to the main menu screen
        self.__root.mainloop()

    def __main_menu(self, event=None):
        """
        as soon as the window starts load the main menu
        :param event: the None default indicates that the function was called
                    to called to create the main menu.
                    i.e: was not called back from the difficulty select
        :return: None
        """
        if event is not None:
            # check if the function ws called back from difficulty select
            for widget in self.__start_frame.winfo_children():
                # remove all the elements of the previous screen except the
                # return to main menu button
                widget.destroy() if widget != self.__start_frame else None
        else:
            self.__start_frame = tk.Frame(self.__root, width=500, height=500,
                                          bg=BG_COLOR)
            self.__start_frame.grid(columnspan=10, rowspan=10)
            # create a frame to act as the title screen
        self.__main_title = tk.Label(self.__start_frame,
                                     image=self.big_title_image, bg=BG_COLOR)
        self.__main_title.place(x=40, y=0)
        # make and add the title image for the main menu
        self.__play_label = tk.Label(self.__start_frame,
                                     image=self.orange_play, bg=BG_COLOR)
        self.__play_label.place(x=260, y=250)
        self.__play_label.bind("<Button-1>",
                               lambda event: self.__play_label.config(
                                   image=self.grey_play))
        self.__play_label.bind("<ButtonRelease-1>", self.__difficulty_select)
        # make a start button, when pressed delete the title screen and
        # start the game
        self.__exit_label = tk.Label(self.__start_frame,
                                     image=self.orange_exit, bg=BG_COLOR)
        self.__exit_label.bind("<Button-1>",
                               lambda event: self.__exit_label.config(
                                   image=self.grey_exit))
        self.__exit_label.bind("<ButtonRelease-1>",
                               lambda event: self.__root.destroy())
        self.__exit_label.place(x=100, y=250)
        # make an exit button, when pressed exit the window
        self.__info_button = tk.Label(self.__start_frame,
                                      image=self.green_info, bg=BG_COLOR)
        self.__info_button.place(x=5, y=430)
        self.__info_button.bind("<Button-1>",
                                lambda event: self.__info_button.config(
                                    image=self.grey_info))
        self.__info_button.bind("<ButtonRelease-1>", self.__information)
        # create the info button that leads to credit screen
        self.__cancel_label = tk.Label(self.__start_frame,
                                       image=self.pink_back, bg=BG_COLOR)
        self.__cancel_label.bind("<Button-1>",
                                 lambda event: self.__cancel_label.config(
                                     image=self.grey_back))
        self.__cancel_label.bind("<ButtonRelease-1>", self.__main_menu)
        # create but not place the return to main menu button

    def __information(self, event):
        """
        show the credit page of the game
        :param event:
        :return:
        """
        for widget in self.__start_frame.winfo_children():
            # destroy all the widget in start frame so that the info screen
            # will show, all except the return to main menu button
            widget.destroy() if widget != self.__cancel_label else None
        self.__info_label = tk.Label(self.__start_frame, image=self.info_title,
                                     bg=BG_COLOR)
        self.__info_label.place(x=4, y=10)
        # add the title image of the credit page
        self.__credit_text = tk.Label(self.__start_frame, bg=BG_COLOR,
                                      text=CREDITS, font="bold")
        self.__credit_text.place(x=35, y=140)
        # place the credit text themselves
        self.__cancel_label.place(x=5, y=430)
        # place the return to main menu button
        self.tal_label = tk.Label(self.__start_frame, image=self.tal_avatar,
                                  bg=BG_COLOR)
        self.tal_label.place(x=80, y=380)
        self.tal_quote = tk.Label(self.__start_frame, bg=BG_COLOR,
                                  text=TAL_QUOTE)
        self.tal_quote.place(x=162, y=410)
        # create and place Tals' avatar and quote on info page
        self.idan_label = tk.Label(self.__start_frame, image=self.idan_avatar,
                                   bg=BG_COLOR)
        self.idan_label.place(x=290, y=380)
        self.idan_quote = tk.Label(self.__start_frame, bg=BG_COLOR,
                                   text=IDAN_QUOTE)
        self.idan_quote.place(x=380, y=405)
        # create and place Idans' avatar and quote on info page

    def __difficulty_select(self, event):
        """"""
        self.__play_label.destroy()
        self.__exit_label.destroy()
        self.__info_button.destroy()
        # the main menu stays but it's button get destroyed

        self.__easy_label = tk.Label(self.__start_frame,
                                     image=self.orange_label, text="EASY",
                                     compound='center', bg=BG_COLOR,
                                     font='bold')
        self.__easy_label.place(x=200, y=250)
        self.__easy_label.bind("<Button-1>",
                               lambda event: self.__easy_label.config(
                                   image=self.grey_label))
        self.__easy_label.bind("<ButtonRelease-1>", self.__start_game)
        # create a label for the easy difficulty
        self.__hard_label = tk.Label(self.__start_frame,
                                     image=self.orange_label, text="HARD",
                                     compound='center', bg=BG_COLOR,
                                     font='bold')
        self.__hard_label.place(x=200, y=320)
        self.__hard_label.bind("<Button-1>",
                               lambda event: self.__hard_label.config(
                                   image=self.grey_label))
        self.__hard_label.bind("<ButtonRelease-1>", self.__start_game)
        # create a label for the hard difficulty
        self.__cancel_label.place(x=5, y=430)
        # place the cancel label on screen
        self.help_label = tk.Label(self.__start_frame, image=self.green_help,
                                   bg=BG_COLOR)
        self.help_label.place(x=330, y=330)
        # create and place the help icon on screen
        self.help_box = tk.Label(self.__start_frame, bg=BG_COLOR,
                                 borderwidth=2, text=HELP_BOX_TEXT,
                                 relief="ridge", justify="left")
        self.help_label.bind("<Enter>",
                             lambda event: self.help_box.place(x=140, y=430))
        self.help_label.bind("<Leave>",
                             lambda event: self.help_box.place_forget())
        # when mouse hovers over help icon this label appears

    def __start_game(self, event):
        """
        this function acts as the creation of the actual game
        :param event: if the start was called from the main menu it will
                    contain the difficulty button that called it
                    if it was called as a restart it will contain None
        :return: None
        """
        self.__game = boggle.Game(boggle.DICT_FILE)
        # make a new Boggle game with the give dictionary
        if event.widget is self.__easy_label or event.widget is self.__hard_label:
            # if this game creation was called from the main menu
            self.__difficulty = "easy" if event.widget == self.__easy_label else "hard"
            # a variable for the game difficulty
            self.__start_frame.grid_forget()
            # destroy the tile screen to reveal the actual game

        self.title_label = tk.Label(image=self.title_image, bg=BG_COLOR)
        self.title_label.grid(columnspan=3, rowspan=1, sticky="w")
        # add the image of the title as a label
        self.time_label = tk.Label(self.__root, image=self.pink_label,
                                   bg=BG_COLOR, text=TIME_LABEL,
                                   compound="center")
        self.time_label.grid(column=3, row=0, columnspan=2, sticky="se")
        # add the time tracker to the window as a label
        self.__time_left = TIME_LIMIT + 1
        self.__update_clock()
        # start the count down of the clock, update it after one second
        self.score_label = tk.Label(image=self.green_label, bg=BG_COLOR,
                                    text=SCORE_LABEL + f"\n{self.__game.get_score()}",
                                    compound="center")
        self.score_label.grid(column=5, row=0, columnspan=2, sticky="s")
        # add the score tracker to the window as a label
        self.correct_words = []
        # a list holding all the correctly guessed words
        self.guess_title = tk.Label(self.__root, bg=BG_COLOR,
                                    image=self.grey_label,
                                    text=GUESS_LABEL_TEXT, compound="center")
        self.guess_title.place(x=358, y=135)
        # add a label to act as the title of the guessed words
        self.guess_label = tk.Label(self.__root, bg=BG_COLOR,
                                    text="".join(self.correct_words),
                                    wraplength=100, anchor="n", height=18,
                                    width=15, borderwidth=1, relief="sunken")
        self.guess_label.place(x=368, y=200)
        self.guess_label.place_configure()
        # add a label that will display the words the play found
        self.home_button = tk.Label(image=self.green_home, bg=BG_COLOR)
        self.home_button.grid(column=3, row=0, columnspan=1, sticky="ne")
        self.home_button.bind("<Button-1>",
                              lambda event: self.home_button.config(
                                  image=self.grey_home))
        self.home_button.bind("<ButtonRelease-1>",
                              lambda event: self.__go_home())
        # add a label that will act as the return to main menu button
        self.reload_button = tk.Label(image=self.green_reload, bg=BG_COLOR)
        self.reload_button.grid(column=4, row=0, columnspan=1, sticky="ne")
        self.reload_button.bind("<Button-1>",
                                lambda event: self.reload_button.config(
                                    image=self.grey_reload))
        self.reload_button.bind("<ButtonRelease-1>", self.__reload_game)
        # add a label that will act as the reload game button

        self.die_frame = tk.Frame(self.__root, width=300, height=300,
                                  borderwidth=3, relief="raised")
        self.die_frame.grid(column=0, row=3, columnspan=5, rowspan=5, )
        # make a frame that will hold the dice board
        self.__dice: List = []
        self.make_board(self.__game.board)
        # make a list of list each holding a row of buttons
        self.__root.update()
        # to get dimensions of the dice, the root needs to update firt
        self.die_width = self.__dice[0][0].winfo_width() - 8
        self.die_height = self.__dice[0][0].winfo_height() - 8
        # get the dimensions of a die and lower it a bit to create blank space
        # between them

        self.__root.bind("<B1-Motion>", self.__start_action)
        # when the mouse is pressed and dragged
        self.__root.bind("<ButtonRelease-1>", self.__stop_action)
        # when the mouse is released
        self.attempt_list: List[Tuple] = [(-1, -1)]
        #  a list holding all the used dice during selection process
        self.attempt: str = ""
        # a place holder for the string of the letters selected

    def __load_assets(self):
        """
        :function: load and create variables for all of the files of the game
        :return: None
        """
        self.green_button = tk.PhotoImage(file=GREEN_BUTTON)
        self.grey_button = tk.PhotoImage(file=GREY_BUTTON)
        self.pink_button = tk.PhotoImage(file=PINK_BUTTON)
        self.orange_button = tk.PhotoImage(file=ORANGE_BUTTON)
        self.orange_label = tk.PhotoImage(file=ORANGE_LABEL)
        self.pink_label = tk.PhotoImage(file=PINK_LABEL)
        self.green_label = tk.PhotoImage(file=GREEN_LABEL)
        self.grey_label = tk.PhotoImage(file=GREY_LABEL)
        self.title_image = tk.PhotoImage(file=TITLE_IMAGE)
        self.big_title_image = tk.PhotoImage(file=BIG_TITLE_IMAGE)
        self.orange_play = tk.PhotoImage(file=ORANGE_PLAY)
        self.grey_play = tk.PhotoImage(file=GREY_PLAY)
        self.orange_exit = tk.PhotoImage(file=ORANGE_EXIT)
        self.grey_exit = tk.PhotoImage(file=GREY_EXIT)
        self.green_home = tk.PhotoImage(file=GREEN_HOME)
        self.grey_home = tk.PhotoImage(file=GREY_HOME)
        self.pink_back = tk.PhotoImage(file=PINK_BACK)
        self.grey_back = tk.PhotoImage(file=GREY_BACK)
        self.grey_reload = tk.PhotoImage(file=GREY_RELOAD)
        self.green_reload = tk.PhotoImage(file=GREEN_RELOAD)
        self.green_info = tk.PhotoImage(file=GREEN_INFO)
        self.grey_info = tk.PhotoImage(file=GREY_INFO)
        self.info_title = tk.PhotoImage(file=INFO_TITLE)
        self.tal_avatar = tk.PhotoImage(file=TAL_AVATAR)
        self.idan_avatar = tk.PhotoImage(file=IDAN_AVATAR)
        self.green_help = tk.PhotoImage(file=GREEN_HELP)

    def make_board(self, letters: List[List]):
        """
        :function: make labels for the board and load them to the window
        :param letters: a list of the board in letter form
        :return: None
        """
        for row in range(SIZE):
            self.__dice.append([])
            # create a new row on the board
            for col in range(SIZE):
                temp_die = tk.Label(self.die_frame, image=self.orange_button,
                                    text=letters[row][col], compound="center",
                                    font="bold", bg=BG_COLOR)
                # natural image is orange and the letter corresponds to the
                # board given
                temp_die.grid(row=row + 1, column=col)
                # add the newly created die label to the window
                self.__dice[row].append(temp_die)
                # place the die in the corresponding location in the die list

    def __start_action(self, event):
        """
        :function: change the die labels to reflect the even of <B1-Motion>
        :param event: not used
        :return: None
        """
        for row in range(SIZE):
            for col in range(SIZE):
                # go through all the dice if the board
                temp = self.__dice[row][col]  # a place holder for current die
                if temp.winfo_rootx() < self.__root.winfo_pointerx() \
                        < temp.winfo_rootx() + self.die_width and \
                        temp.winfo_rooty() < self.__root.winfo_pointery() < \
                        temp.winfo_rooty() + self.die_height:
                    # check if the location of the cursor ON SCREEN while its
                    # being dragged is on this die
                    if self.attempt_list[-1] != (-1, -1) and (
                            row, col) not in self.possible_moves(
                            self.attempt_list[-1]):
                        # the next selection has to be from the 8 dice
                        # surrounding the last one
                        self.__root.event_generate("<ButtonRelease-1>")
                        # force a release of Button-1
                        return  # stop this selection process
                    if (row, col) in self.attempt_list[:-1]:
                        self.__cut_selection((row, col))
                    temp.config(image=self.grey_button)
                    # the die will turn grey during selection process
                    temp_letter = temp.cget("text")
                    # get the letter on the selected die
                    if row != self.attempt_list[-1][0] or col != \
                            self.attempt_list[-1][1]:
                        # make sure the selection progressed to a different die
                        self.attempt += temp_letter
                        # add the letter to the current attempt to solve
                        # the last used die is this one
                        self.attempt_list.append((row, col))
                        # add the last die to the used

    def __stop_action(self, event):
        """
        :function: change the die to reflect release of B1
        :param event: not used
        :return: None
        """
        check = self.__game.word_check(self.attempt)
        if (len(
                self.attempt) < HARD_LEN and self.__difficulty == "hard") \
                or self.attempt in self.correct_words:
            check = False
        # see if the attempt is correct or not
        for row in range(SIZE):
            for col in range(SIZE):
                # go through all the dice on board
                temp = self.__dice[row][col]
                # a place holder for current die
                if temp.cget("image") == str(self.grey_button):
                    # if the current die is grey, i.e. was one of the selected
                    if check:
                        temp.config(image=self.green_button)
                    else:
                        temp.config(image=self.pink_button)
                    # if the check was True change it to green to reflect
                    # correct guess
                    # if the check was False change it to pink to reflect
                    # incorrect guess
        self.correct_guess() if check else None
        # if check was True update the game accordingly
        self.__root.after(250, self.__reset_die)
        # after a short period change all of the board back to natural state

    def __reset_die(self):
        """
        :function: reset all dice to natural state
        :return: None
        """
        self.attempt = ""
        # turn the attempt variable back to nothing
        self.attempt_list = [(-1, -1)]
        # turn the last used die to nothing
        for row in range(SIZE):
            for col in range(SIZE):
                # go through all of the dice on board
                temp = self.__dice[row][col]
                # a place golder for current die
                temp.config(image=self.orange_button)
                # change it to its natural state, i.e orange

    def __go_home(self):
        """
        during the game process if this function is called it will return the
        window to the main menu
        :return: None
        """
        for widget in self.__root.winfo_children():
            # destroy all the widget in window to allow for new ones to be made
            widget.grid_forget()
        self.__root.after_cancel(self.__clock_id)
        # stop the clocks progression to allow for a new one to be created
        # later and build the main menu
        self.__main_menu(None)

    def correct_guess(self):
        """
        :function: update the game to reflect the success of the player
        :return: None
        """
        if self.attempt in self.correct_words:
            # if the word already was found then there is nothing further to do
            return
        self.correct_words.append(self.attempt)
        # add the correct guess to the correct guesses list
        self.guess_label.config(text=", ".join(self.correct_words))
        # change the label showing the guessed words
        self.__game.update_score(len(self.attempt))
        self.score_label.config(
            text=SCORE_LABEL + f"\n{self.__game.get_score()}")
        # change the score

    def __cut_selection(self, die: Tuple):
        """
        cut all of the selected die from given index to the end
        :param die: a tuple of index (x, y) of the board dice
        :return: None
        """
        die_index = self.attempt_list.index(die)
        # the index from which to delete
        cut_index = len(self.attempt_list) - 1
        # the index of last element in the list
        while cut_index != die_index:
            # while deleting from the end continue backwards until the index
            # of the removal reaches the start
            self.__remove_die(self.attempt_list[cut_index])
            # do all the actions corresponding to removal of given die
            cut_index -= 1  # continue to next die

    def __remove_die(self, die: Tuple):
        """
        given die coordinate, remove it from the correct selection attempt
        :param die:  a tuple of index (x, y) of the board dice
        :return: None
        """
        self.attempt = self.attempt[:-1]
        # shorten the word by one
        temp = self.__dice[die[0]][die[1]]
        # a place holder for the die from dice list corresponding to the give
        # coordinates tuple
        temp.config(image=self.orange_button)
        # change the image to its natural state, i.e. make it orange
        self.attempt_list = self.attempt_list[:-1]
        # shorten the selection attempt list by one

    def __reload_game(self, event):
        """
        during the game itself if this function is called it will reload a new
        game instead
        :param event: the event that called this function
        :return: None
        """
        for widget in self.__root.winfo_children():
            # destroy all the widgets in game so they could be created from
            # scratch
            widget.destroy()
        self.__root.after_cancel(self.__clock_id)
        # stop the clock update process to allow for a new one to be created
        self.__start_game(event)
        # start the game over

    def __update_clock(self):
        """
        update the game clock every 1 second
        :return: None
        """
        now = self.__time_left - 1
        # get time left from the game
        if now % 60 < 10:
            # if there are less then 10 seconds left or exactly 3 minutes
            self.time_label.config(
                text=TIME_LABEL + f"0{now // 60}:0{now % 60}")
            # change the time label text to reflect the remaining time
        else:
            self.time_label.config(
                text=TIME_LABEL + f"0{now // 60}:{now % 60}")
            # change the time label text to reflect the remaining time
        if not now:
            # when time runs out
            msg_box = messagebox.askquestion(TIME_UP_BOX_TITLE,
                                             TIME_UP_BOX_MESSAGE.format(
                                                 len(self.correct_words),
                                                 self.__game.get_score()))
            # pop-up a window showing a message and asks to go again
            if msg_box == 'yes':
                #  if the answer was yes
                self.reload_button.event_generate("<ButtonRelease-1>")
                # reload the game
            else:
                # if the answer was no
                self.__go_home()
                # go to main menu
        else:
            # if the time didn't run out yet
            self.__clock_id = self.__root.after(1000, self.__update_clock)
            # in addition to updating the clock keep the idea of the current
            # after  function in case later it will need to be canceled
            self.__time_left -= 1
            # ask to be updated in another 1 second

    def possible_moves(self, die: Tuple):
        """
        given a die coordinates, make a list containing all of the legal
        coordinates for the next die
        :param die: a tuple of (x, y) coordinates
        :return: list of possible moves
        """
        lst = [(die[0] + 1, die[1]), (die[0] + 1, die[1] + 1),
               (die[0] + 1, die[1] - 1), (die[0] - 1, die[1]),
               (die[0] - 1, die[1] - 1), (die[0] - 1, die[1] + 1),
               (die[0], die[1] + 1), (die[0], die[1] - 1), (die[0], die[1])]
        return lst


game = Screen()
