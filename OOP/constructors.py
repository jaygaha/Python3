class ComplexNumber:
    "This is docstring(__doc__)"

    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}')

#call docstring
print(ComplexNumber.__doc__)

#create a new ComplexNumber object
num1 = ComplexNumber(2,3)

#call get_data() method
#output: 2+3j
num1.get_data()

#create another ComplexNumber object and create a new attribute 'attr'
num2 = ComplexNumber(5)
num2.attr = 10

#output: (5, 0, 10)
print((num2.real, num2.imag, num2.attr))

#but num1 object doesn't have attribute 'attr'
#AttributeError: 'ComplexNumber' object has no attribute 'attr'
print(num1.attr)