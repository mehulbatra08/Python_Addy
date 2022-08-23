# If the input is divisible by 3 return Fizz, if the input is divisible by 5 return Buzz and if it is divisible by both 5 and 3 then it is return FizzBuzz

def fizz_buzz(x):

     


        if x%3 == 0 and x%5 == 0:
            return ("FizzBuzz")

        elif x%3 == 0:
            return ("Fizz")

        elif x%5 == 0:
            return ("Buzz")

        else:
            return ("Number is not divisible by anything\n")  

    
print(fizz_buzz(30))










