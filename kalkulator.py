import tkinter as tki


class kalkulator():

    def __init__(self):
        pass 

    def makeWindow(self):
        self.window=tki.Tk()
        self.window.mainloop()

    
        


def main():
    kalk=kalkulator()
    kalk.makeWindow()
    

if __name__ =='__main__':
    main()
