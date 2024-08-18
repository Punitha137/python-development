def add(num1, num2):
  
      
  return num1 + num2

def subtract(num1, num2):

  return num1 - num2

def multiply(num1, num2):
  
  return num1 * num2



def divide(num1, num2):
  
  if num2 == 0:
    return "Error: Cannot divide by zero."
  else:
    return num1 / num2

def main():
  
  while True:
    print("Welcome to the Simple Calculator!")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice in ('1', '2', '3', '4'):
      try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
      except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

      if choice == '1':
        result = add(num1, num2)
      elif choice == '2':
        result = subtract(num1, num2)
      elif choice == '3':
        result = multiply(num1, num2)
      else:
        result = divide(num1, num2)
      print("Result:", result)
    elif choice == '5':
      print("Exiting calculator.")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
  main()
