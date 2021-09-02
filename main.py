from art import logo, vs
import random
from game_data import data 
from replit import clear

score=0
def format_data(account):
  """Format the account data into printable format"""
  account_name = account['name']
  account_desc = account['description']
  account_country = account['country']
  return f"{account_name},a {account_desc},from {account_country}"

def check_answer(guess,a_followers,b_followers):
  """Take the users guess and followers count and return if they guessed right"""
  if a_followers>b_followers:
    return guess=='a'
  else:
    return guess=='b'

# display art 
print(logo)

account_b = random.choice(data)
counter = True
while counter:
  # generater a random account from the game data 
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b=random.choice(data)

  # printing the account details
  print(f"compare A: {format_data(account_a)}")
  print(vs)
  print(f"against B: {format_data(account_b)}")

  # user guessing the account 
  guess = input("Who has more followers? Type 'A' or 'B':").lower()

  # get the followers of the account_a
  a_follower_count = account_a['follower_count']
  b_follower_count = account_b['follower_count']
  is_correct = check_answer(guess,a_follower_count,b_follower_count)
  # clear the screen
  clear()
  print(logo)
  # giving feedback to the users guess
  if is_correct:
    score+=1
    print(f"You are right! current score is {score}")
  else:
    counter = False
    print(f"Sorry that's wrong. Final score {score}")




 



