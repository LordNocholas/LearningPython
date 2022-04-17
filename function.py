def verify_user(username, password):
    if( (username.lower() == 'nocholas') and (password=='lol') ):
       print("Hello {},  welcome back".format(username))
       return 1
    else:
       print("no")
       return 0

uname = input("enter your username: ")
pswd = input("enter your password: ")

if(verify_user(uname, pswd)):
   print("session started, you are now logged in")




#def multiply(x,y):
 #   global result
  #  result = x*y
   # return result
    

#multiply(5,6)

#print(result)
