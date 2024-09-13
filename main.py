print("Math Game!")
print()
multiple = int(input("Name your multiples: "))
print()

score = 0
for i in range(1,11,1):
  multiplication = i * multiple
  print(i, "X", multiple)
  answer = int(input("= "))
  if answer == multiplication:
    print("Great work!")
    print()
    score += 1
  else:
    print("Nope. The answer was", multiplication)
    print()

print("___")
print()
if score == 10:
  print("Wow! A perfect score! 🥳")
else:
  print("You scored", score, "out of 10.")