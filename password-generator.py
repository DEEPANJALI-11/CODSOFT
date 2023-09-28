import random as rd
import string
def generatepassword(n):
    letters=string.ascii_letters
    digits=string.digits
    special_char=string.punctuation
    letter=letters+digits+special_char
    chosenletter=rd.sample(letter,n)
    password="".join(chosenletter)
    return password
if __name__=="__main__":
    while True:
        userchoice=input("Please Enter Yes , if you want to continue:")
        if userchoice=='no':
            break
        else:
            n=int(input("Enter the length of your password:"))
            password=generatepassword(n)
            print("Your Password is:",password)
