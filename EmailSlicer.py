This code will seperate the username and domain will be displayed through your entered email ID

def EmailSlicer(email):
    username, _, domain = email.strip().partition("@")
    return "Username\t:"+username+"\nDomain\t\t:"+domain
input = input("Enter Your Email: ")
print(EmailSlicer(input))

