from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements

    happy = simpledialog.askstring(title="", prompt="Are you happy?")
    if happy == "yes":
        messagebox.showinfo(title="", message="Keep doing whatever you're doing!")
    if happy == "no":
         ansno = simpledialog.askstring(title="",prompt="Do you want to be happy?")
    if ansno == "no":
        messagebox.showinfo(title="",message="Keep doing whatever you're doing!")
    if ansno == "yes":
        messagebox.showinfo(title="",message="Change Something")








    pass
