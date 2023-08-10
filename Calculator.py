from tkinter import *
calwindow = Tk()
calwindow.title("Calculator")
calwindow.geometry("280x295+300+200")
calwindow.config(bg = "gold")

equation = ""
def show(value) :
    global equation
    equation += value
    val.config(text=equation)
    
def clear() :
    global equation
    equation = ""
    val.config(text=equation)

def delete() :
    global equation
    equation = equation[:-1]
    val.config(text=equation)
    
def equal() :
    global equation
    result = ""
    equation = equation.replace("^","**")
    if equation != "" :
        try :
            result = eval(equation)
            equation = str(result)
        except :
            result = "error"
            print("Invalid")
            equation = result
    val.config(text=result)

    
val = Label(calwindow, width = 20, height = 1, text = "", font = ("Times", 35, "bold"))
val.pack()

bac = Button(calwindow, text = "AC", width = 4, height = 1, font = ("Times", 15, "bold"), bd = 1 , bg = "#fc4552", fg = "skyblue", command = lambda: clear())
bac.place(x = 5, y = 65)

bde = Button(calwindow, text = "DEL", width = 4, height = 1, font = ("Times", 15, "bold"), bd = 1 , bg = "darkorchid", fg = "deeppink", command = lambda: delete())
bde.place(x = 75, y = 65)

bpow = Button(calwindow, text = "^", width = 4, height = 1, font = ("Times", 15, "bold"), bd = 1 , bg = "plum", fg = "darkcyan", command = lambda: show("^"))
bpow.place(x = 145, y = 65)

bdiv = Button(calwindow, text = "/", width = 4, height = 1, font = ("Times", 15, "bold"), bd = 1 , bg = "plum", fg = "darkcyan", command = lambda: show("/"))
bdiv.place(x = 215, y = 65)

b7 = Button(calwindow, text = "7", width = 4, height = 1, font = ("Times", 15, "bold"), bd = 1 , bg = "cyan", fg = "floralwhite", command = lambda: show("7"))
b7.place(x = 5, y = 110)

b8 = Button(calwindow, text = "8", width = 4, height = 1, font = ("Times", 15, "bold"), bd = 1 , bg = "cyan", fg = "floralwhite", command = lambda: show("8"))
b8.place(x = 75, y = 110)

b9 = Button(calwindow, text = "9", width = 4, height = 1, font = ("Times", 15, "bold"), bd = 1 , bg = "cyan", fg = "floralwhite", command = lambda: show("9"))
b9.place(x = 145, y = 110)

bmul = Button(calwindow, text = "*", width = 4, height = 1, font = ("Times", 15, "bold"), bd = 1 , bg = "plum", fg = "darkcyan", command = lambda: show("*"))
bmul.place(x = 215, y = 110)

b4 = Button(calwindow, text = "4", width = 4, height = 1, font = ("Times", 15, "bold"), bd = 1 , bg = "cyan", fg = "floralwhite", command = lambda: show("4"))
b4.place(x = 5, y = 155)

b5 = Button(calwindow, text = "5", width = 4, height = 1, font = ("Times", 15, "bold"), bd = 1 , bg = "cyan", fg = "floralwhite", command = lambda: show("5"))
b5.place(x = 75, y = 155)

b6 = Button(calwindow, text = "6", width = 4, height = 1, font = ("Times", 15, "bold"), bd = 1 , bg = "cyan", fg = "floralwhite", command = lambda: show("6"))
b6.place(x = 145, y = 155)

bsub = Button(calwindow, text = "-", width = 4, height = 1, font = ("Times", 15, "bold"), bd = 1 , bg = "plum", fg = "darkcyan", command = lambda: show("-"))
bsub.place(x = 215, y = 155)

b1 = Button(calwindow, text = "1", width = 4, height = 1, font = ("Times", 15, "bold"), bd = 1 , bg = "cyan", fg = "floralwhite", command = lambda: show("1"))
b1.place(x = 5, y = 200)

b2 = Button(calwindow, text = "2", width = 4, height = 1, font = ("Times", 15, "bold"), bd = 1 , bg = "cyan", fg = "floralwhite", command = lambda: show("2"))
b2.place(x = 75, y = 200)

b3 = Button(calwindow, text = "3", width = 4, height = 1, font = ("Times", 15, "bold"), bd = 1 , bg = "cyan", fg = "floralwhite", command = lambda: show("3"))
b3.place(x = 145, y = 200)

badd = Button(calwindow, text = "+", width = 4, height = 1, font = ("Times", 15, "bold"), bd = 1 , bg = "plum", fg = "darkcyan", command = lambda: show("+"))
badd.place(x = 215, y = 200)

b0 = Button(calwindow, text = "0", width = 4, height = 1, font = ("Times", 15, "bold"), bd = 1 , bg = "cyan", fg = "floralwhite", command = lambda: show("0"))
b0.place(x = 5, y = 245)

bdot = Button(calwindow, text = ".", width = 4, height = 1, font = ("Times", 15, "bold"), bd = 1 , bg = "cyan", fg = "floralwhite", command = lambda: show("."))
bdot.place(x = 75, y = 245)

beq = Button(calwindow, text = "=", width = 4, height = 1, font = ("Times", 15, "bold"), bd = 1 , bg = "greenyellow", fg = "orangered", command = lambda: equal())
beq.place(x = 145, y = 245)

bmod = Button(calwindow, text = "%", width = 4, height = 1, font = ("Times", 15, "bold"), bd = 1 , bg = "plum", fg = "darkcyan", command = lambda: show("%"))
bmod.place(x = 215, y = 245)

calwindow.mainloop()
