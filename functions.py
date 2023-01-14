
#to find square root
def square_root(num):

    square_root=str(num **0.5)
    square_root2='√'+square_root
    return square_root2



#prime or not
def prime_number(a):
    if a <=1:
        return(f"{a} is not a prime number.")
    else:
        b=range(2,a)
        for i in b:
            if a % i==0:
              return(f"{a} is not a prime number.")
            break      
        else:
            return(f"{a} is a prime number.")
# to get the factorial value 
def factorial(a):
    if a == 0 :
        return 1
    return a* factorial(a-1)

