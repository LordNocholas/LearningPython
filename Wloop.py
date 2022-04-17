import random

random_num = random.randrange(100)


while(True):
   response = int(input("Guess the correct number. "))
   if(response < random_num):
          print("Higher")
   elif(response > random_num):
          print("Lower")
   elif(response == random_num):
          print("you guessed correctly the number was {}".format(response))
          break
  

# if(counter == 0):
    #     print("Start")
    #if(counter == 2):
     #    print("End")
 #print("counter : ", counter)
     #print("counter : " + str(counter))
     #print("counter : {} {} {}".format(counter, counter, counter))
