import secrets
import string

def generate_password(length=12, lowercase=True, uppercase=True, digits=True, punctuation=False):
  
  

  
  char_set = string.ascii_lowercase if lowercase else ''
  char_set += string.ascii_uppercase if uppercase else ''
  char_set += string.digits if digits else ''
  char_set += string.punctuation if punctuation else ''

  
  min_chars = sum([lowercase, uppercase, digits, punctuation])
  if min_chars > len(char_set):
    raise ValueError("Selected criteria require more unique characters than available in the chosen set. Please reduce requirements or expand the character set.")

  
  password = ''.join(secrets.choice(char_set) for _ in range(length))
  return password

def main():
  """Prompts the user for desired password length and character options."""
  try:
    length = int(input("Enter desired password length (minimum 8 characters): "))
    if length < 8:
      raise ValueError("Password length must be at least 8 characters.")

    lowercase = input("Include lowercase letters (y/n)? ").lower() == 'y'
    uppercase = input("Include uppercase letters (y/n)? ").lower() == 'y'
    digits = input("Include digits (y/n)? ").lower() == 'y'
    punctuation = input("Include punctuation characters (y/n)? ").lower() == 'y'

    password = generate_password(length, lowercase, uppercase, digits, punctuation)
    print(f"Your generated password is: {password}")
  except ValueError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()
