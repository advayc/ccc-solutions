# Read the input
N = int(input()) # Number of rounds
# Initialize the two numbers
num1 = 1
num2 = 1
# Loop through each round
for i in range(N):
  # Initialize the output strings
  out1 = ""
  out2 = ""
  # Check if num1 is divisible by 7 or 13
  if num1 % 7 == 0:
    out1 += "Fizz"
  if num1 % 13 == 0:
    out1 += "Fuzz"
  # Check if num2 is divisible by 7 or 13
  if num2 % 7 == 0:
    out2 += "Fizz"
  if num2 % 13 == 0:
    out2 += "Fuzz"
  # If out1 is empty, use num1 instead
  if out1 == "":
    out1 = str(num1)
  # If out2 is empty, use num2 instead
  if out2 == "":
    out2 = str(num2)
  # Print the output strings
  print(out1, out2)
  # Update the numbers
  num1 += 1
  num2 += 2
