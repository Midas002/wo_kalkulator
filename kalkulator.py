import tkinter as tki
from tkinter import *

class kalkulator:
    def __init__(self, fieldText="0", currForm="decimal", currLen="qword" , curoper=""):
        
        self.field_text = fieldText 
        self.current_format = currForm
        self.current_length=currLen
        self.formats = ["binary","oktagonal", "decimal", "hexadecimal"]
        self.lengths = ["qword", "dword", "word", "bajt"]
        self.currLimit=64
        self.ope_helper=0
        self.curr_oper=curoper
        self.currBinar="0b0000000000000000000000000000000000000000000000000000000000000000"
        self.savedVal=""
        
        

    def add_to_field(self, number, field):
        if self.field_text == "0" and len(self.field_text)==1:
            self.clear(field)
            return self.add_to_field(number,field)
        temp = self.field_text+str(number)
        tmpbin=bin(int(temp))
        if len(tmpbin)>self.currLimit+2:
            return 0
        else:
            self.field_text += str(number)
            field.delete("1.0", "end")
            field.insert("1.0", self.field_text)
            self.BinDispUpd()
        
    def addition(self,):
        if self.curr_oper=="":
            self.ope_helper= self.convertDecimal()
            self.field_text=""
            self.curr_oper="+"
        # else:
        #     self.calculate(field)
        #     return self.addition()
            
    def subtraction(self):
        if self.curr_oper=="":
            self.ope_helper= self.convertDecimal()
            self.field_text=""
            self.curr_oper="-"
        # else:
        #     self.calculate(field)
        #     return self.subtraction()
        
    def division(self):
        if self.curr_oper=="":
            self.ope_helper= self.convertDecimal()
            self.field_text=""
            self.curr_oper="/"
        # else:
        #     self.calculate(field)
        #     return self.division()
        
    def multiply(self):
        if self.curr_oper=="":
            self.ope_helper= self.convertDecimal()
            self.field_text=""
            self.curr_oper="*"
        # else:
        #     self.calculate(field)
        #     return self.multiply()
    
    def memoSave(self):
        self.savedVal=self.field_text
                
    def memoadd(self):
        self.ope_helper=self.savedVal
        self.curr_oper="+"
        # self.calculate(field)
        
    def memosubs(self):
        self.ope_helper=self.savedVal
        self.curr_oper="-"
        # self.calculate(field)
        
    def memoclear(self):
        self.savedVal=""
    
    def memoshow(self):
        self.field_text=self.savedVal
        # field.insert("1.0",self.field_text)
        
    def opxor(self):
        if self.curr_oper=="":
            self.ope_helper= self.convertDecimal()
            self.field_text=""
            self.curr_oper="xor"
        # else:
        #     self.calculate(field)
        #     return self.opxor()
        
    def opor(self):
        if self.curr_oper=="":
            self.ope_helper= self.convertDecimal()
            self.field_text=""
            self.curr_oper="or"
        # else:
        #     self.calculate(field)
        #     return self.opor()
    
    def opand(self):
        if self.curr_oper=="":
            self.ope_helper= self.convertDecimal()
            self.field_text=""
            self.curr_oper="and"
        # else:
        #     self.calculate(field)
        #     return self.opand()
                
    def negate(self):
        tmp=self.convertDecimal()
        tmp= ~tmp
        self.field_text=str(tmp)
        # self.clearbin(field)
        # field.insert("1.0",self.field_text)
                
    def opnot(self):
        self.negate()
        
    def opnand(self):
        if self.curr_oper=="":
            self.ope_helper= self.convertDecimal()
            self.field_text=""
            self.curr_oper="nand"
        # else:
        #     self.calculate(field)
        #     return self.opnand()
        
    def opnor(self):
        if self.curr_oper=="":
            self.ope_helper= self.convertDecimal()
            self.field_text=""
            self.curr_oper="nor"
        # else:
        #     self.calculate(field)
        #     return self.op()
    
    def calculate(self):  #func for "=" button and not only
        tmpCal=0
        if self.curr_oper=="+":
            temp2=self.convertDecimal()
            self.curr_oper=""
            tmpCal=self.ope_helper+temp2
        elif self.curr_oper=="-":
            temp2=self.convertDecimal()
            self.curr_oper=""
            tmpCal=self.ope_helper-temp2
        elif self.curr_oper=="/":
            temp2=self.convertDecimal()
            self.curr_oper=""
            tmpCal=self.ope_helper/temp2
        elif self.curr_oper=="*":
            temp2=self.convertDecimal()
            self.curr_oper=""
            tmpCal=self.ope_helper*temp2
        elif self.curr_oper=="and":
            temp2=self.convertDecimal()
            self.curr_oper=""
            tmpCal=self.ope_helper & temp2
        elif self.curr_oper=="or":
            temp2=self.convertDecimal()
            self.curr_oper=""
            tmpCal=self.ope_helper | temp2  
        elif self.curr_oper=="xor":
            temp2=self.convertDecimal()
            self.curr_oper=""
            tmpCal=self.ope_helper^temp2  
        elif self.curr_oper=="nor":
            temp2=self.convertDecimal()
            self.curr_oper=""
            tmpCal=~(self.ope_helper*temp2)
        elif self.curr_oper=="nand":
            temp2=self.convertDecimal()
            self.curr_oper=""
            tmpCal=~(self.ope_helper&temp2)
        else:
            return 0
        
        # tmpbin=self.currentBinary(self.field_text)
        # tmpcalbin=self.currentBinary(tmpCal)
        # if len(tmpcalbin)>len(tmpbin):
        #     return 0 
        self.curr_oper=""
        self.ope_helper=""
        self.field_text=str(tmpCal)
        # self.convertTo(self.current_format,field)
        
        # self.clearbin(field)
        # field.insert("1.0",self.field_text)
        # self.BinDispUpd()
        
        
        # try:
            
        #     result = str(eval(self.field_text))  
        #     field.delete("1.0", "end")
        #     field.insert("1.0", result)
        #     self.field_text = result  
        # except:
        #     field.delete("1.0", "end")
        #     field.insert("1.0", "Error")
        #     self.field_text = ""  

    def clearbin(self,field):
        field.delete("1.0","end")
    
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
        field.insert("1.0",self.field_text) 
        
        
        self.frame1 = LabelFrame(self.window, padx=15, pady=15) 
        self.frame1.grid(row= 2, column= 6)
        
        
        self.frame2 = LabelFrame(self.window, padx=15, pady=15) 
        self.frame2.grid(row= 3, column= 6)
        
        self.binaryDispaly = LabelFrame(self.window, padx=15, pady=15)
        self.binaryDispaly.grid(row= 8, column= 6)
        
        
      
        
        self.onSelectFormat(field)
        
        self.onSelectLenForm(field)
        self.BinDisplay(field)
        self.currBinar=self.convertBinary()

        print(self.formats)

        btn_A = tki.Button(self.window, text="A", command=lambda: self.add_to_field(10, field))
        btn_A.grid(row=2, column=7)
        
        btn_B = tki.Button(self.window, text="B", command=lambda: self.add_to_field(11, field))
        btn_B.grid(row=3, column=7)
        
        btn_C = tki.Button(self.window, text="C", command=lambda: self.add_to_field(12, field))
        btn_C.grid(row=4, column=7)
        
        btn_D = tki.Button(self.window, text="D", command=lambda: self.add_to_field(13, field))
        btn_D.grid(row=5, column=7)
        
        btn_E = tki.Button(self.window, text="E", command=lambda: self.add_to_field(14, field))
        btn_E.grid(row=6, column=7)
        
        btn_F = tki.Button(self.window, text="F", command=lambda: self.add_to_field(15, field))
        btn_F.grid(row=7, column=7)
       
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
        
        btn_7 = tki.Button(self.window, text="7", command=lambda: self.add_to_field(7, field))
        btn_7.grid(row=4, column=1)

        btn_8 = tki.Button(self.window, text="8", command=lambda: self.add_to_field(8, field))
        btn_8.grid(row=4, column=2)

        btn_9 = tki.Button(self.window, text="9", command=lambda: self.add_to_field(9, field))
        btn_9.grid(row=4, column=3)
        
        btn_0 = tki.Button(self.window, text="0", command=lambda: self.add_to_field(0, field))
        btn_0.grid(row=5, column=1)
        
        btn_substract = tki.Button(self.window, text="-", command=lambda: self.subtraction(field))
        btn_substract.grid(row=4, column=4)
        
        
        btn_add = tki.Button(self.window, text="+", command=lambda: self.addition(field))
        btn_add.grid(row=5, column=3)
        
        btn_multiply = tki.Button(self.window, text="*", command=lambda: self.multiply(field))
        btn_multiply.grid(row=3, column=4)
        
        btn_divide = tki.Button(self.window, text="/", command=lambda: self.division(field))
        btn_divide.grid(row=2, column=4)
        
        btn_change_sign = tki.Button(self.window, text="+-", command=lambda: self.negate(field))
        btn_change_sign.grid(row=1, column=4)
        
        btn_upside_down = tki.Button(self.window, text="1/x", command=lambda: self.add_to_field(field))
        btn_upside_down.grid(row=5, column=5)
        
        btn_proc = tki.Button(self.window, text="%", command=lambda: self.add_to_field(field))
        btn_proc.grid(row=4, column=5)
        
        btn_square_root = tki.Button(self.window, text="x^2", command=lambda: self.add_to_field(field))
        btn_square_root.grid(row=3, column=5)
        
        btn_equals = tki.Button(self.window, text="=", command=lambda: self.calculate(field))
        btn_equals.grid(row=2, column=5)
        
        btn_and = tki.Button(self.window, text="and", command=lambda: self.opand(field))
        btn_and.grid(row=2, column=6)
        
        btn_or = tki.Button(self.window, text="or", command=lambda: self.opor(field))
        btn_or.grid(row=3, column=6)
        
        btn_nor = tki.Button(self.window, text="not", command=lambda: self.opnot(field))
        btn_nor.grid(row=4, column=6)
        
        btn_xor = tki.Button(self.window, text="xor", command=lambda: self.opxor(field))
        btn_xor.grid(row=5, column=6)
        
        
        
        

        btn_clear = tki.Button(self.window, text="C", command=lambda: self.clear(field))
        btn_clear.grid(row=6, column=1)


        field.bind("<<Modified>>", lambda event: self.align_text_right(field))
        
        
        
        self.window.mainloop()
    
    def onSelectFormat(self,field):
        self.current_format=StringVar()
        x=0
        
        for item in self.formats:
            
            if(item == "binary"):
                checkboxes = Radiobutton(self.frame1, text=item, value=item, width=10, command=lambda: self.convertTo(item,field))
                
            elif(item=="oktagonal"):
                checkboxes = Radiobutton(self.frame1, text=item, value=item, width=10, command=lambda: self.convertTo(item,field))
                
            elif(item=="decimal"):
                checkboxes = Radiobutton(self.frame1, text=item, value=item, width=10, command=lambda: self.convertTo(item,field)) 
                
            elif(item=="hexadecimal"):
                checkboxes = Radiobutton(self.frame1, text=item, value=item, width=10, command=lambda: self.convertTo(item, field))       
                   
            if item == self.current_format:
                checkboxes.select()
            checkboxes.place(x=250,y=0+x)
            checkboxes.pack()
            checkboxes.pack_propagate(0)
            x+=20
            
    def onSelectLenForm(self,field):
        self.current_length=StringVar()
        x=0
        
        for item in self.lengths:
            #label = tki.Label(self.frame2, text="This is a label inside a LabelFrame", anchor="w")
            #label.grid(row=0, column=0, padx=5, pady=5)
            
            checkboxes = Radiobutton(self.frame2, text=item, variable=self.current_length, value=item, width=10)
            if item == "qword":
                checkboxes.select()
            checkboxes.place(x=250,y=0+x)
            checkboxes.pack()
            
            x+=20    
        
        
    #def on_event(event):
       # text=event.textvariable    
    
    # def toggle_label(label, index):
    #     current_value = label_values[index]
    #     new_value = 1 if current_value == 0 else 0
    #     label.config(text=str(new_value))
    #     label_values[index] = new_value
    
        
    def BinDispUpd(self):
        self.index=list(self.currBinar)
        self.index=self.index[2:]
            
    def BinDisplay(self,field):    #do binda: lambda e: self.binarUpade(index[i])
        x = 0       
        self.BinDispUpd()
        for i in range(64):
            
            
            # if((i % 4) != 0 and i<32):
            gen_label=Label(self.binaryDispaly,text="0",font=("Segoe UI", 10))
            gen_label.bind("<Button-1>",lambda event, idx=i,lbl=gen_label:self.binarUpdate(lbl,idx,field))
            gen_label.pack(side="left")
                
               
                
                
            
        
    

    def align_text_right(self, field):
        field.tag_add("right", "1.0", "end")  
        field.edit_modified(False)   
        
        
    def convertTo(self, option):
        # w samych funkcjach konwertowania robimy ro różnie w zależności od aktualnego systemu używanego do wyświetlania
        if option == "binary":
            self.convertBinary()
            self.current_format="binary"
            
        elif option == "decimal":
            self.convertDecimal()
            self.current_format="decimal" 
             
        elif option == "octagonal":
            self.convertOctagonal()
            self.current_format="octagonal"   
        else:
            self.convertHexagonal() 
            self.current_format="hexadecimal" 
             
        # self.clearbin(field)
        # field.insert("1.0",self.field_text)
               
            
            
    def convertBinary(self):
        temp=self.convertDecimal()
        if self.current_format != "binary":
            result=bin(temp)
        else:
            result=self.field_text
        return result
    
    def bintodec(self, conv):
        return int(conv,0)
    
    def convertDecimal(self, conv=""):
        if len(conv)==0:
            conv=self.field_text
        if self.current_format == "binary":
            numTemp=int(conv,0)
            result=numTemp
        elif self.current_format == "octagonal":
            numTemp=int(conv,8)
            result=numTemp
        elif self.current_format == "hexadecimal":
            numTemp=int(conv,16)
            result=numTemp
        else:
            result=int(conv)
        return result
    
    def convertOctagonal(self):
        temp=self.convertDecimal()
        if self.current_format != "octagonal":
            result=oct(temp)
        else:
            result=self.field_text
        return result
    
    def convertHexagonal(self):
        temp=self.convertDecimal()
        if self.current_format != "hexadecimal":
            result=hex(temp)
        else:
            result=self.field_text
        return result
        
    def currentBinary(self,tocon):  #funckja do wyświetlacza liczby w formacie binarnym żebyśmy gdzieś mieli
        tmp=self.convertDecimal(conv=str(tocon))
        if self.current_format !="binary":
            result=bin(tmp)
        else:
            result=self.field_text
        return result
    
    def lengthTo(self,option):
        # w funkcjach do ustalania długości robimy to różnie w zależności od aktualnej długości 
        if option=="qword":
            self.toQword()
            self.current_length="qword"
            self.currLimit=64
        elif option=="dword":
            self.toDword() 
            self.current_length="dword"
            self.currLimit=32
        elif option=="word":
            self.toWord()
            self.current_length="word"
            self.currLimit=16
        elif option=="bajt":
            self.toBajt()
            self.current_length="bajt"
            self.currLimit=8

    def toQword(self):
        if self.currLimit == 32:
            helperString=32*"0"
            self.currBinar="0b"+helperString+self.currBinar
        elif self.currLimit == 16:
            helperString=48*"0"
            self.currBinar="0b"+helperString+self.currBinar
        elif self.currLimit == 8:
            helperString=58*"0"
            self.currBinar="0b"+helperString+self.currBinar
        self.fromBin()
        
    def toDword(self):
        if self.currLimit == 64:
            self.currBinar="0b"+self.currBinar[-32:]
        elif self.currLimit == 16:
            helperString=16*"0"
            self.currBinar="0b"+helperString+self.currBinar
        elif self.currLimit == 8:
            helperString=24*"0"
            self.currBinar="0b"+helperString+self.currBinar
        self.fromBin()
        
    def toWord(self):
        if self.currLimit > 16:
            self.currBinar="0b"+self.currBinar[-16:]
        elif self.currLimit == 8:
            helperString=24*"0"
            self.currBinar="0b"+helperString+self.currBinar
        self.fromBin()
        
    
    def toBajt(self):
        self.currBinar = "0b"+self.currBinar[-8:]
        self.fromBin()
    
    def fromBin(self):
        tmp=self.bintodec(self.currBinar)
        self.field_text=str(tmp)
        # self.clearbin(field)
        # field.insert("1.0",self.field_text)
        
        
        
    def binarUpdate(self,lbl, index):
        curval=int(self.index[index])
        #print(index)
        newval=1 if curval == 0 else 0
        lbl.config(text=str(newval))
        self.index[index]=newval
        self.currBinar="0b"+"".join(map(str,self.index))
        # self.fromBin(field)
        
        
    
                  


# def main():
#     kalk = kalkulator()
#     kalk.makeWindow()


# if __name__ == '__main__':
#     main()
