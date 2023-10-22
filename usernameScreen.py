name = input("Please put in a username. ")

if len(name) < 3:
  print("Name must be at least three characters.")
elif len(name) > 50:
  print("Name must be 50 characters max.")
else:
  print("Done!")
