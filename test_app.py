import unittest
import kalkulator as kal

class TestCalc(unittest.TestCase):
    
    
    
    def test_addition(self):
        TestKal = kal.kalkulator()
        TestKal.field_text="8"
        TestKal.addition()
        self.assertEqual(TestKal.ope_helper, 8)
        self.assertEqual(TestKal.curr_oper,"+")
        self.assertEqual(TestKal.field_text,"")
        
    def test_subtrac(self):
        tkal = kal.kalkulator() 
        tkal.field_text="7"
        tkal.subtraction()
        self.assertEqual(tkal.ope_helper, 7)
        self.assertEqual(tkal.curr_oper,"-")
        self.assertEqual(tkal.field_text, "")
       
    def test_multiplication(self):
        TestKal2 = kal.kalkulator()
        TestKal2.field_text="8"    
        TestKal2.multiply()
        self.assertEqual(TestKal2.ope_helper, 8)
        self.assertEqual(TestKal2.curr_oper,"*")
        self.assertEqual(TestKal2.field_text, "")
        
        
    def test_divide(self):
        TestKal3 = kal.kalkulator()
        TestKal3.field_text="9"    
        TestKal3.division()
        self.assertEqual(TestKal3.ope_helper, 9)
        self.assertEqual(TestKal3.curr_oper,"/")
        self.assertEqual(TestKal3.field_text, "")
        
        
    def test_calculation(self):
        TestKal4 = kal.kalkulator()
        TestKal4.field_text="9"
        TestKal4.ope_helper=6
        TestKal4.curr_oper="+"
        TestKal4.calculate()
        self.assertEqual(TestKal4.field_text, "15")
        TestKal4.field_text="3"
        TestKal4.ope_helper=6
        TestKal4.curr_oper="-"
        TestKal4.calculate()
        self.assertEqual(TestKal4.field_text, "3")
        TestKal4.field_text="2"
        TestKal4.ope_helper=3
        TestKal4.curr_oper="*"
        TestKal4.calculate()
        self.assertEqual(TestKal4.field_text, "6")
        TestKal4.field_text="2"
        TestKal4.ope_helper=6
        TestKal4.curr_oper="/"
        TestKal4.calculate()
        self.assertEqual(TestKal4.field_text, "3")
        
    def test_opand(self):
        TestKal5 = kal.kalkulator()
        TestKal5.field_text="10"
        TestKal5.opand() 
        self.assertEqual(TestKal5.ope_helper, 10)
        self.assertEqual(TestKal5.curr_oper,"and")
        self.assertEqual(TestKal5.field_text, "") 
        
    def test_opor(self):
        TestKal6 = kal.kalkulator()
        TestKal6.field_text="10"
        TestKal6.opor() 
        self.assertEqual(TestKal6.ope_helper, 10)
        self.assertEqual(TestKal6.curr_oper,"or")
        self.assertEqual(TestKal6.field_text, "")
        
        
    def test_opxor(self):
        TestKal7 = kal.kalkulator()
        TestKal7.field_text="11"
        TestKal7.opxor()
        self.assertEqual(TestKal7.ope_helper, 11)
        self.assertEqual(TestKal7.curr_oper,"xor")
        self.assertEqual(TestKal7.field_text, "")
        
        
    def test_opnot(self):
           TestKal8 = kal.kalkulator()
           TestKal8.field_text="12"   
           TestKal8.opnot()
           self.assertEqual(TestKal8.field_text, "-13")
           
    def test_negate(self):
           TestKal10 = kal.kalkulator()
           TestKal10.field_text="12"   
           TestKal10.negate()
           self.assertEqual(TestKal10.field_text, "-13")
           
    #def test_clear(self):
        #TestKal9 = kal.kalkulator()
        #TestCalc.     
          
    def test_conv_deci(self):
        tka2=kal.kalkulator()
        tka2.field_text="0b00110100110"
        tka2.current_format="binary"
        result=tka2.convertDecimal()
        self.assertEqual(result, 934)
        
    def test_conv_bin(self):
        tka3 = kal.kalkulator()
        tka3.field_text="12"
        tka3.current_format="decimal"
        result=tka3.convertDecimal()
        self.assertEqual(result, "0b1100")
    
    
    
    def test_conv_oct(self):
        tka4 = kal.kalkulator()
        tka4.field_text="0b00000001110"
        tka4.current_format="binary"
        result=tka4.convertOctagonal()
        self.assertEqual(result, "16")
        
        
    def test_conv_hex(self):
        tk5 = kal.kalkulator()           
        tk5.field_text="0b00000001110"
        tk5.current_format="binary"
        result=tk5.convertHexagonal()
        self.assertEqual(result, "E")
        
        
    if __name__ == '__main__':
        unittest.main()