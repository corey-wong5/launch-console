name = input("What is your name?")
print(f"Welcome to Corey's Launch Console!")

running = True
while running:
  print("1) About Me")
  print("2) My Goals")
  print("3) Exit")
  choice = input("Pick 1-3: ")
  if choice == 1:
    print("Hi, my name is Corey and I am a junior in High School. I am currently in Code2College's Elite 101 class learning more about programming. Some of my hobbies include robotics, running, and playing the viola.")
  elif choice == 2:
    print("My goal is to learn enough about programming to create my own functioning web app.")
  elif choice == 3: 
    print("Goodbye!")
    running = False
    break
  else:
    print("Please pick 1, 2, or 3")
