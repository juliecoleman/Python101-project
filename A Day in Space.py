import time, random

# Print game introduction: Choose daily space activities to maintain physical and 
# mental well being.

# Write functions to find out details of the player first.

# Write a function to play the game by choosing space activities. Make sure 
# activities are tracked in new lists. Add random emergencies when no activity can be chosen.

# Write a function to determine the health of the player depending on how they played the game.

print("Welcome space traveler! You are in a spaceship for the next 30 weeks \
  traveling from Earth to Mars.It is important that you maintain your mental \
  and physical health during space travel despite being confined to the spaceship.")
print()
time.sleep(4)

print("You must make good choices for how you spend your free time. However, \
  be warned that emergencies do come up in space! You may not get free time \
  each day. We will see if you are in good health at the end of the week \
  depending on how you spend the free time you do get.")
print()
time.sleep(4)

print("First we would like to learn more about you.")
print()
time.sleep(2)

# Get to know player to add humor and make the game more personable

def astronaut_name():
  """Get name of player and make sure it returns capitalized."""

  name = input("What is your name?")

  return name.title()

print("Welcome!", astronaut_name())
print()
time.sleep(1)


def astronaut_age():
  """Get age of player and make sure it returns as an intenger and not string."""

  age = int(input("What is your age?"))

  if  age < 66:
    print("You are quite the prodigy to be here in space at the young age of", age)

  else:
    print("Wow, you must love being an astronaut to not be retired yet. Good for you!")

astronaut_age() 
print()
time.sleep(2)


def astronaut_spouse():
  """Get marital status of player but if they do not answer yes or no ask again."""

  while True:
    marriage = input("Are you married?").title()

    if marriage == "Yes":
      print("I'm sorry you are having to spend time away from your spouse!")
      break

    elif marriage == "No":
      print("Great! It's wonderful to have freedom to travel, especially to space!")
      break

    else:
      print("Incorrect response. Please type just yes or no to answer.")

astronaut_spouse()
print()
time.sleep(2)


def astronaut_hobbies():
  """Get hobbies of the astronaut and continually ask until they don't give anymore."""

  while True:
    hobbies = input("What is a favorite hobby?")

    if hobbies == "":
        break

    print(hobbies.title(), "sounds great!")
    print()
    print("If you have another favoriate hobby, please share. Otherwise press enter.")

astronaut_hobbies()
print()
time.sleep(2)


# Begin game portion now that know more about player

print("Now that we know more about you, let's see how you will spend your free time this week.")
print()
time.sleep(2)

# A tuple is written to loop over which day of the week it is
weekday = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# A dictionary is written to assign activities based on player answer
activities = {1:"read", 2:"call your family", 3:"watch a guilty pleasure on Netflix", 
4:"run on the treadmill", 5:"ride the exercise bike", 
6:"play a card game with fellow astronauts", 7:"eat a whole box of cookies", 
8:"draw graffiti on the spaceship", 9:"lift weights"}

# Empty lists are written to keep track of activities
good_mental_activities = []
good_physical_activities = []
bad_activities = []


def spend_free_time():
  """Loop over list of each day of the week. For each day, it is randomly 
  chosen whether the player experiences an emergency or gets free time. 
  If they get free time, they choose a number that represents an activity. 
  The activity is appended to its respective list."""
  
  for day in weekday:
      print("Hooray! It's {}.".format(day))
      time.sleep(2)

      rand = random.randint(1,2)

      if rand == 1:
       print("Sorry, there is a spaceship emergency today. You will not get any free time today!")
       print()
       time.sleep(2)

      if rand == 2:
        print("You have free time today! Please choose a number to decide what activity you will do.")
        print("1: read")
        print("2: call your family")
        print("3: watch a guilty pleasure on Netflix")
        print("4: run on the treadmill")
        print("5: ride the exercise bike")
        print("6: play a card game with fellow astronauts")
        print("7: eat a whole box of cookies") 
        print("8: draw graffiti on the spaceship")
        print("9: lift weights")
        choice = int(input("> "))

        if choice == 1 or choice == 2 or choice == 6:
          activity = activities[choice]
          good_mental_activities.append(activity)
          print("Today you have chosen to: {}.".format(activity))

        if choice == 4 or choice == 5 or choice == 9:
          activity = activities[choice]
          good_physical_activities.append(activity)
          print("Today you have chosen to: {}.".format(activity))

        if choice == 3 or choice == 7 or choice == 8:
          activity = activities[choice]
          if not (activity in bad_activities):
            bad_activities.append(activity)
          print("Today you have chosen to: {}.".format(activity))

        print()
        time.sleep(2)


def health_result():
  """Depending on the length of the lists of the activities chosen, player is 
  informed whether they maintained good or bad physical and mental health."""
  
  spend_free_time()
  print()
  print("You have reached the end of the week! Let's check your health")
  print()
  time.sleep(3)

  if len(good_mental_activities) > 1:
    print("Congratulations! Your mental health is good this week!")
    print()

  else:
    print("Sorry, your mental health suffered this week!")
    print()

  if len(good_physical_activities) > 1:
    print("Congratulations! Your physical health is good this week!")
    print()

  else:
    print("Sorry! Your physical health suffered this week!")
    print()

  if len(bad_activities) != 0 and (len(good_mental_activities) <= 1 or 
    len(good_physical_activities) <= 1):
    print("To improve your health try to spend less time doing: {}.".format(
      bad_activities))

health_result()