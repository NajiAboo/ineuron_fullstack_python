def length(in_var):
    if type(in_var) == str:
        l = 0
        for c in in_var:
            l+=1
        return l
    else:
        return "Please enter string input"


s = input("Enter the string variable: ")
l = length(s)
print(f"Length of {s} : {l}")
