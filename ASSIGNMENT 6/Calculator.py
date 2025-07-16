from tkinter import Tk, Entry, mainloop, Button, END

total_input = ""

window = Tk()
window.geometry("501x240")
e = Entry(window, width=33, font="Arial 20", justify="right")
e.place(x=1, y=0)


def click(user_input):
    global total_input
    curr_input = e.get()

    if curr_input in ["Division by Zero not Allowed", "Expression evaluation Error"]:
        curr_input = ""
        e.delete(0, END)
    if user_input == "Clear":
        total_input = ""
        e.delete(0, END)
        return
    if user_input == "=":
        try:
            result = str(eval(total_input + curr_input))
            print(total_input + curr_input + " = " + result)
            e.delete(0, END)
            e.insert(END, result)
        except ZeroDivisionError:
            e.delete(0, END)
            e.insert(END, "Division by Zero not Allowed")
        except Exception:
            e.delete(0, END)
            print(total_input + curr_input)
            e.insert(END, "Expression evaluation Error")
        total_input = ""
        return
    if user_input in "+-*/":
        if curr_input == "" and user_input == "-":
            e.insert(END, "-")
            return
        total_input += curr_input + " " + user_input + " "
        e.delete(0, END)
        return
    e.insert(END, user_input)


if __name__ == "__main__":
    text_x = ["+", "-", "*", "/"]
    text_y = ["Clear", "0", "="]
    for i in range(4):
        for j in range(4):
            op_colour = {}
            if i != 3:
                text = str(3 * j + i + 1)
            else:
                text = text_x[j]
                op_colour = {"bg": "sky blue", "fg": "black"}
            if j == 3:
                if i != 3:
                    text = text_y[i]
                if i == 2:
                    op_colour = {"bg": "grey", "fg": "white"}
            if i == 0 and j == 3:
                op_colour = {"bg": "grey", "fg": "white"}
            b = Button(window, text=text, width=8, font="Times_New_Roman 18", border=3, **op_colour, command=lambda x=text: click(x))
            b.place(x=(125 * i) + 1, y=50 * (1 + (j % 4)) - 10)

    mainloop()
