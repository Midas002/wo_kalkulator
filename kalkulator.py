import tkinter as tki
from tkinter import *

class kalkulator:
    def __init__(self):
        self.field_text = "" 
        self.current_format = "decimal"
        self.current_length="qword"
        self.formats = {"binary","oktagonal", "decimal", "hexagonal"}
        
        

    def add_to_field(self, number, field):
        
        self.field_text += str(number)
        field.delete("1.0", "end")
        field.insert("1.0", self.field_text)

    def calculate(self, field):  
        try:
            
            result = str(eval(self.field_text))  
            field.delete("1.0", "end")
            field.insert("1.0", result)
            self.field_text = result  
        except:
            field.delete("1.0", "end")
            field.insert("1.0", "Error")
            self.field_text = ""  

    def clear(self, field):
        
        self.field_text = ""
        field.delete("1.0", "end")

    def makeWindow(self):
        self.window = tki.Tk()
        self.window.geometry("350x400")
        self.window.title("Kalkulator")

        
        field = tki.Text(self.window, height=2, width=21, font=("Segoe UI", 20))
        field.grid(row=1, column=1, columnspan=4)
        field.tag_configure("right", justify="right")  
        field.insert("1.0", "0")  
        
        
        self.format_container = tki.Frame(self.window)
        self.format_container.grid(row=5,column=6, columnspan=3)
        
      
        
        self.onselect()
        

        print(self.formats)

       
        btn_1 = tki.Button(self.window, text="1", command=lambda: self.add_to_field(1, field))
        btn_1.grid(row=2, column=1)

        btn_2 = tki.Button(self.window, text="2", command=lambda: self.add_to_field(2, field))
        btn_2.grid(row=2, column=2)

        btn_3 = tki.Button(self.window, text="3", command=lambda: self.add_to_field(3, field))
        btn_3.grid(row=2, column=3)

        btn_4 = tki.Button(self.window, text="4", command=lambda: self.add_to_field(4, field))
        btn_4.grid(row=3, column=1)

        btn_5 = tki.Button(self.window, text="5", command=lambda: self.add_to_field(5, field))
        btn_5.grid(row=3, column=2)

        btn_6 = tki.Button(self.window, text="6", command=lambda: self.add_to_field(6, field))
        btn_6.grid(row=3, column=3)

        btn_clear = tki.Button(self.window, text="C", command=lambda: self.clear(field))
        btn_clear.grid(row=4, column=1)

        btn_equals = tki.Button(self.window, text="=", command=lambda: self.calculate(field))
        btn_equals.grid(row=4, column=2)

        field.bind("<<Modified>>", lambda event: self.align_text_right(field))
        
        self.window.mainloop()
    
    def onselect(self):
        self.current_format=StringVar()
        x=0
        
        for item in self.formats:
            
            
            checkboxes = Radiobutton(self.format_container, text=item, variable=self.current_format, value=item)
            if item == "decimal":
                checkboxes.select()
            checkboxes.place(x=350,y=0+x)
            x+=20
        
        

        
                
        

    def align_text_right(self, field):
        field.tag_add("right", "1.0", "end")  
        field.edit_modified(False)   
        
        
    def convertTo(self, option):
        # w samych funkcjach konwertowania robimy ro różnie w zależności od aktualnego systemu używanego do wyświetlania
        if option == "bin":
            self.convertBinary()
            self.current_format="bin"
            
        elif option == "dec":
            self.convertDecimal()
            self.current_format="dec" 
             
        elif option == "oct":
            self.convertOctagonal()
            self.current_format="oct"
            
        else:
            self.convertHexagonal() 
            self.current_format="hex"         
            
            
    def convertBinary(self):
        if self.current_format == "dec":
            numTemp=int(self.field_text)
            result=bin(numTemp)
        elif self.current_format == "oct":
            numTemp=int(self.field_text,8)
            result=bin(numTemp)
        elif self.current_format == "hex":
            numTemp=int(self.field_text,16)
            result=bin(numTemp)
        else:
            result=self.field_text
        return result
    
    def convertDecimal(self):
        if self.current_format == "bin":
            numTemp=int(self.field_text)
            result=numTemp
        elif self.current_format == "oct":
            numTemp=int(self.field_text,8)
            result=numTemp
        elif self.current_format == "hex":
            numTemp=int(self.field_text,16)
            result=numTemp
        else:
            result=self.field_text
        return result
    
    def convertOctagonal(self):
        if self.current_format == "dec":
            numTemp=int(self.field_text)
            result=oct(numTemp)
        elif self.current_format == "bin":
            numTemp=int(self.field_text,)
            result=oct(numTemp)
        elif self.current_format == "hex":
            numTemp=int(self.field_text,16)
            result=oct(numTemp)
        else:
            result=self.field_text
        return result
    
    def convertHexagonal(self):
        if self.current_format == "dec":
            numTemp=int(self.field_text)
            result=hex(numTemp)
        elif self.current_format == "oct":
            numTemp=int(self.field_text,8)
            result=hex(numTemp)
        elif self.current_format == "bin":
            numTemp=int(self.field_text)
            result=hex(numTemp)
        else:
            result=self.field_text
        return result
        
    def currentBinary(self):  #funckja do wyświetlacza liczby w formacie binarnym żebyśmy gdzieś mieli
        if self.current_format == "dec":
            numTemp=int(self.field_text)
            result=bin(numTemp)
        elif self.current_format == "oct":
            numTemp=int(self.field_text,8)
            result=bin(numTemp)
        elif self.current_format == "hex":
            numTemp=int(self.field_text,16)
            result=bin(numTemp)
        else:
            result=self.field_text
        return result
    
    def lengthTo(self,option):
        # w funkcjach do ustalania długości robimy to różnie w zależności od aktualnej długości 
        if option=="qword":
            self.toQword()
            self.current_length="qword"
        elif option=="dword":
            self.toDword() 
            self.current_length="dword"
        elif option=="word":
            self.toWord()
            self.current_length="word"
        elif option=="bajt":
            self.toBajt()
            self.current_length="bajt"


    def toQword(self):
        numTemp=self.currentBinary()
        if len(numTemp) == 32:
            helperString=32*"0"
            result=helperString.join(numTemp)
        elif len(numTemp) == 16:
            helperString=48*"0"
            result=helperString.join(numTemp)
        elif len(numTemp) == 8:
            helperString=58*"0"
            result=helperString.join(numTemp)
        return result
    
    def toDword(self):
        numTemp=self.currentBinary()
        if len(numTemp) == 64:
            result=numTemp[-32:]
        elif len(numTemp) == 16:
            helperString=16*"0"
            result=helperString.join(numTemp)
        elif len(numTemp) == 8:
            helperString=24*"0"
            result=helperString.join(numTemp)
        return result
    
    def toWord(self):
        numTemp=self.currentBinary()
        if len(numTemp) > 16:
            result=numTemp[-16:]
        elif len(numTemp) == 8:
            helperString=24*"0"
            result=helperString.join(numTemp)
        return result
    
    def toBajt(self):
        numTemp=self.currentBinary()
        result = numTemp[-8:]    
        return result
    
                  


def main():
    kalk = kalkulator()
    kalk.makeWindow()


if __name__ == '__main__':
    main()
