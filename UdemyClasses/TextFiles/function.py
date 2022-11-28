""" Practicing functions in python."""
def python_food():
    width = 80
    text = "Spam and Eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)
   

""" Creating centering """

def centre_text(text):
    width = 80
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)
    
    
# call the function
centre_text("spam and eggs")
centre_text("spam, spam, and eggs")
centre_text("spam, spam, spam, and spam")
