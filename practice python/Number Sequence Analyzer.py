def get_intro():
    opening = input("  Choose your option: FS, PNC, PNR,MT, Factorial, CS ")
    Options  = ["Fibonacci Sequence, Prime Number Check, Prime Number Range, Multiplication Table, Factorial, Collatz Sequence"]
    return opening


intros = get_intro()
print(intros)
def get_value(): 
    value = [  ]
if intros.lower == "FS":
 print("Select value between 1-20")