#Password Generator

#Write a program, which generates a random password for the user.
#Ask the user how long they want their password to be, and how many letters and numbers they want in their password.
#Have a mix of upper and lowercase letters,
#as well as numbers and symbols. The password should be a minimum of 6 characters long.







import random
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

while True:
    try:
        lenght = int(input('how many characters your password want to be?:'))
        passlen = 6
        if (lenght < passlen):
            print("the pw must be minimum 6 characters")
            lenght = int(input('how many characters your password want to be? remember minumum 6 characters:'))
        p =  "".join(random.sample(s,passlen))
        print ("Here is your password:-->",p)
        break
    except:
        print("try again, number only")
        
    