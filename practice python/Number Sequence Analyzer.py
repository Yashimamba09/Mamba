def get_intro():
    opening = input("  Choose your option: 1.Fibonacci Sequence, 2.Prime Number Check, 3. Prime Number Range, 4.Multiplication Table, 5.Factorial,  6. Collatz Sequence ")
    return opening


intros = get_intro()
print(intros)
def get_value(): 
    value = [  ]
if intros == "1":
 print("Select value between 1-20")

elif intros == "2":
   print("Check if numbers between 1-100 is a prime number  Enter prime number here ")
elif intros == "3":
   print("")