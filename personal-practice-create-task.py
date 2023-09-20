#This is the dictionary used to define the terms for the search.

state_fish_list = {"Hawaii": "rectangular triggerfish" , "California": "garibaldi", "The Moon": "anglerfish", "Colorado": "greenback cutthroat trout"}



# This function takes in the dictionary, the search question (q), the message to be printed before the results,
# and the message to be printed between the search term and the definition associated with it. It works
# with any dictionary.

def define(dictionary, q, printmsg1, printmsg2):

  c = "y"
  
  while c == "y":
    word = input(q)
    if dictionary.get(word, 0) != 0:
      print(printmsg1, word, printmsg2, dictionary[word] + ".")
      c = input("Search again? y/n ")
    else:
      print("ERROR")



#This is the function call for state_fish_list, complete with the prompt and print messages.

define(state_fish_list, "Enter state: ", "The state fish of", "is the")