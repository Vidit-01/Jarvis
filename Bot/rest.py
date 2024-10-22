# importing installed library
import pyjokes

# using get_joke() to generate a single joke
#language is english
#category is neutral
for i in range(30):
    My_joke = pyjokes.get_joke(language="en", category="neutral")

    print(My_joke)
