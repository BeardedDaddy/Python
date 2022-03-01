def multiply(x, y):
      result = x * y
      return result


def is_palindrome(string):
      backwards = string[::-1]
      return backwards == string
      return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
      string =""
      for char in sentence:
            if char.isalnum():
                  string += char
      print(string)
      return string[::-1].casefold() ==string.casefold()
      return is_palindrome(string)

#A function is a block of code which only runs when it is called. You can pass data, known as paraments, into a function. A function can return data as a result.
#Example: def my_function(FirstName, LastName):
#           print(FirstName + "" + LastName)
#         my_function ("Grevy", "Marcelin")

# def my_function(FirstName, LastName):
#       print(FirstName + "" + LastName)
# my_function ("Grevy", "Marcelin")
answer = multiply(18, 3)
print(answer)

# To call the function you have to break out of the print statement (indent)

#def check_age(age):
#  if age < 18:
#    print('oops not an adult')
#  else:
#    print('hooray I am an adult')  

#check_age(18)
#check_age(17)
