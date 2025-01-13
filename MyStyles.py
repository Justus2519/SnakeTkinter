#Styles to use
def initStyles(style):
    #QuitButton
    style.configure("Quit.TButton",
                    background="#d9d0bd",
                    foreground="black")
    style.map("Quit.TButton", font="helvetica 28",
              foreground=[('pressed', '#c70a04'), ('active', '#c70a04')],
          background=[('pressed', '#d9d0bd'), ('active', '#d9d0b0'),
                      ('disabled', "#d9d0bd")],
              relief=[('pressed', '!disabled', 'sunken')])
    #frame
    style.configure("TFrame", background="#d9d0bd")
    style.configure("L1.TLabel", background="#d9d0bd", font="helvetica 28 bold")

