class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr=[]
        for i in range(1,n+1):
            if(i%3 == 0 or i%5 == 0):
                if(i%3==0):
                    out="Fizz"
                if(i%5 == 0):
                    out="Buzz"
                if(i%5 == 0 and i%3 == 0):
                    out="FizzBuzz"    
            else:
                out=str(i)
            arr.append(out)    
        return arr            

        