import tkinter

#game setup
playerx = "x"
playerO = "O"
curr_player = playerx
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

#window setup
window = tkinter.Tk() #create the game window
window.title("Tic Tac Toe")
window.resizable(False, False)

window.mainloop() # keeps window open until user exits
