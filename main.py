#from additonal files import logo and vs icons and database called data
from art import logo
from art import vs
from game_data import data
from replit import clear

def main():
  #Print logo of the game
  print(logo)

  # Database has elements:
  # print(len(data))
  # how to call on particular data print(data[0]['name'])

  #Define a fucntion that will call upon data from the base in order:
  # name , description, country

  def person(i,version):
    name= data[i]["name"]
    description=data[i]['description']
    country=data[i]['country']
    print(f"Compare {version}: {name}, a {description}, from {country}")

  #Choose a starting point(person) by using randint 
  import random

  i= random.randint(0,49)

  def printout(i):
    version="A"
    person(i, version)
    print(vs)
    if i==49:
      version="B"
      person(0, version)
    else:
      version="B"
      person(i+1, version)

  score=0
  printout(i)
  def check_guess(guess):
    if guess!="A" and guess!="B":
      print("You typed wrong! Try again or game will exit!")
      guess=input("Who has more followers? Type A or B:").upper()
      if guess!="A" or guess!="B":
        exit("Have a nice day!")
    else:
      return guess

  guess=input("Who has more followers? Type A or B:").upper()
  check_guess(guess)
  while i<100:
    if guess=="A":
      if i==49:
        if data[i]['follower_count']>data[0]['follower_count']:
          score+=1
          clear()
          print(logo)
          print(f"You're right! Current score: {score}")
          i+=1
          printout(i)
          guess=input("Who has more followers? Type A or B:").upper()
          check_guess(guess)
        else:
          print(f"Sorry! That's wrong! Current score: {score}")
          i=100
      else:
        if data[i]['follower_count']>data[i+1]['follower_count']:
          score+=1
          clear()
          print(logo)
          print(f"You're right! Current score: {score}")
          i+=1
          printout(i)
          guess=input("Who has more followers? Type A or B:").upper()
          check_guess(guess)
        else:
          print(f"Sorry! That's wrong! Current score: {score}")
          i=100
    elif guess=="B":
      if i==49:
        if data[i]['follower_count']<data[0]['follower_count']:
          score+=1
          clear()
          print(logo)
          print(f"You're right! Current score: {score}")
          i+=1
          printout(i)
          guess=input("Who has more followers? Type A or B:").upper()
          check_guess(guess)
        else:
          print(f"Sorry! That's wrong! Current score: {score}")
          i=100
      else:
        if data[i]['follower_count']<data[i+1]['follower_count']:
          score+=1
          clear()
          print(logo)
          print(f"You're right! Current score: {score}")
          i+=1
          printout(i)
          guess=input("Who has more followers? Type A or B:").upper()
          check_guess(guess)
        else:
          print(f"Sorry! That's wrong! Current score: {score}")
          i=100

main()