import random

number = random.randint(1,101)

while True:
   try:
      inputnum = input("Guess the number(q for quit) :")
      if input == 'q':
         break
      gnumber = int(inputnum)
      if number == gnumber:
         print("You Guessed right!")
         break
      elif number > gnumber:
         print("Not Right ! You guessed too small.")
      else :
         print("Not Right ! You guessed too high.")

   except Exception as e:
       print(f"Exception occured : {str(e)}")
    #    raise Exception(f"{str(e)}")
       