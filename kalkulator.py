import tkinter as tki


class kalkulator:
    def __init__(self):
        self.field_text = ""  

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
    
    def align_text_right(self, field):
        field.tag_add("right", "1.0", "end")  
        field.edit_modified(False)   
        
        
    def convertTo(self, option):
        
        if option == "bin":
            self.convertBinary()
            
        elif option == "dec":
            self.convertDecimal() 
             
        elif option == "oct":
            self.convertOctagonal()
            
        else:
            self.convertHexagonal()          
            
            
    def convertBinary(self):
        return 
    
    def convertDecimal(self):
        return    
    
    def convertOctagonal(self):
        return
    
    def convertHexagonal(self):
        return
        
                  


def main():
    kalk = kalkulator()
    kalk.makeWindow()


if __name__ == '__main__':
    main()
