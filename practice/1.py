
    
class EvenNumbers:
    def __init__(self, MaxValue):
        self.MaxValue = MaxValue
        self.current = 2
        
    def __iter__(self):
        return self
	 
    def __next__(self):
        if self.current > self.MaxValue:
            raise StopIteration
        value = self.current
        self.current +=2
        return value
    
evens = EvenNumbers(10)
for num in evens:
    print(num)

